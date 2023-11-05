from time import sleep
from subprocess import Popen, PIPE
import re

from lavazza_cfds_network_connection import *
from lavazza_cfds_server_communication_macros import *
from wifi import Cell

def update_wifi_config_file():
    try:
        if write_to_system_file(WPA_CONFIG_DATA, WPA_CONFIG_FILE, 'w') == FAILURE:
            logging.exception("Error occurred while writing to hostapd conf file")
            return FAILURE

    except Exception as error:
        logging.exception("Error occurred while update_wifi_config_file - {}".format(error))

def available_wifi_list():
    
    data=list(Cell.all('wlan0'))
    wifi_list={'available_wifi':[]}
    for ssid in data:
        wifi_list['available_wifi'].append(re.findall('=(.*)\)',str(ssid))[0].strip())
    try:
       if not (os.path.isfile(AVAILABLE_WIFI_FILE)):

          if write_to_file(wifi_list, AVAILABLE_WIFI_FILE) == -1:
             raise Exception("File write error: %s", AVAILABLE_WIFI_FILE)
       else:

          if write_to_file(wifi_list, AVAILABLE_WIFI_FILE) == -1:
             raise Exception("File write error: %s", AVAILABLE_WIFI_FILE)
    except Exception as error :
          logging.exception(error)


def turn_on_wifi():
    logging.info("Wifi_Connection : turn_on_wifi function started")

    # Initializing WIFI
    wifi_on_cmd_output = {}
    if command_executor(wifi_on_cmd_output, WIFI_ON_CMD) != SUCCESS:
        logging.exception("Wifi turn on Command Output : process code failed")
        return FAILURE

    sleep(MIN_TIME_TO_IFACE_ON)
    logging.info("Wifi_Connection : turn_on_wifi function finished")
    return SUCCESS


def terminate_wifi():
    logging.info("Wifi_Connection : terminate_wifi function started")
    # Terminating WIFI Connection
    wifi_off_cmd_output = {}
    if command_executor(wifi_off_cmd_output, WIFI_OFF_CMD) != SUCCESS:
        logging.exception("Wifi turn on Command Output : process code failed")
        return FAILURE

    sleep(MIN_TIME_TO_IFACE_OFF)
    logging.debug("Wifi_Connection : terminate_wifi function finished")
    return SUCCESS


def get_wifi_enable_status():
    try:
        # Get WLAN enable status
        wifi_enable_status = {}
        if command_executor(wifi_enable_status, GET_WIFI_ENABLE_STATUS_CMD) != SUCCESS:
            logging.exception("Get wifi enable status Command Output : process code failed")
            return False
        return True
    except Exception as error:
        logging.exception("Error occurred while getting wifi status - {}".format(error))
        return FAILURE


def get_wifi_ip_address():
    """To get wifi interface ip address
       return SUCCESS :: if successfully get ip_address
              FAILURE :: if unable to get ip_address"""

    ip_address = None
    try:
        # Get WLAN IP ADDRESS
        get_ipaddress_cmd_output = {}
        if command_executor(get_ipaddress_cmd_output, GET_IPADDRESS_CMD) != SUCCESS:
            logging.exception("Get wifi ip address Command Output : process code failed")
            return FAILURE, ip_address
        for key in get_ipaddress_cmd_output:
            ip_address = get_ipaddress_cmd_output[key].decode()
            ip_address = ip_address.strip('\n')
            logging.info("Ip address: {}".format(ip_address))
        return SUCCESS, ip_address
    except Exception as error:
        logging.exception("Error occured while getting IP")
        return FAILURE, ip_address


def reconnect_wifi():
    logging.info("Wifi_Connection : reconnect_wifi function started")
    try:
        if not get_wifi_enable_status():
            if turn_on_wifi() == FAILURE:
                return False

        wifi_reconnect_cmd_output = {}
        if command_executor(wifi_reconnect_cmd_output, WIFI_RECONNECT_CMD) != SUCCESS:
            logging.exception("Wifi reconnect Command Output : process code failed")
            return False

        sleep(MIN_TIME_TO_WIFI_RECONNECT)

        wifi_status = check_connectivity(WIFI_INTERFACE_NAME)
        logging.debug("reconnect wifi status : %s", wifi_status)
        return wifi_status

    except Exception as error:
        logging.exception("Wifi_Connection : connect_wifi : %s", error)
        return False


def connect_wifi(wifi_name, wifi_password):
    try:
        logging.info("Wifi_Connection : connect_wifi function started")
        update_wifi_config_file()
        turn_on_wifi()

        wifi_connect_cmd = 'echo ' + wifi_password + ' | wpa_passphrase "' + wifi_name + '" | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf > /dev/null'

        wifi_connect_cmd_output = {}
        if command_executor(wifi_connect_cmd_output, wifi_connect_cmd) != SUCCESS:
            logging.exception("Wifi connect Command Output : process code failed")
            return False

        # os.system(wifi_connect_cmd)
        sleep(MIN_TIME_TO_WIFI_CONNECT)

        wifi_reconnect_cmd_output = {}
        if command_executor(wifi_reconnect_cmd_output, WIFI_RECONNECT_CMD) != SUCCESS:
            logging.exception("Wifi reconnect Command Output : process code failed")
            return False

        # os.system(WIFI_RECONNECT_CMD)
        sleep(MIN_TIME_TO_WIFI_RECONNECT)

        wifi_status = check_connectivity("wlan0")
        logging.debug("Wifi_Connection : wifi connection status : %s", wifi_status)
        return wifi_status

    except Exception as error:
        logging.exception("Wifi_Connection : connect_wifi : %s", error)
        return False


def check_wifi_availability(new_wifi_name):

    try:
        process = Popen(AVAILABLE_WIFI_LIST_CMD, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        stdout = stdout.decode("utf-8")
        wifi_list = re.findall('"(.+?)"', stdout)

        logging.debug("wifi_list - {}".format(wifi_list))

        for wifi in wifi_list:
            if new_wifi_name == wifi:
                logging.info("wifi is available")
                return True
        
        return False

    except Exception as error:
        logging.exception("update_wifi - {}", format(error))
