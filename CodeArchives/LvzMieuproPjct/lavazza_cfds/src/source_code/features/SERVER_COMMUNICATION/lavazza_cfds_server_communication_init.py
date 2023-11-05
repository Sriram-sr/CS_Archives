import threading
from datetime import datetime
import re
##import time
from lavazza_cfds_server_upload_handler import *
from lavazza_cfds_wifi_connection import *
from lavazza_cfds_network_connection import *
from lavazza_cfds_server_communication_macros import *
import lavazza_cfds_signal_strength

logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - Server_Communication - %(levelname)s - %(message)s',
                    filename=LAVAZZA_COMMON_LOG_FILE, filemode='a')

server_communication_system_resources = {}
gui_event_trigger_data = {}
utility_event_data = {}
server_communication_event_handler_data = {}
wifi_of_time = None
wifi_wait_minus = None
default_wifi_mode = False
previous_wifi_name = None
previous_wifi_password = None


def change_machine_wifi_mode(device_mode, wifi_mode):
    try:
        logging.info("change_machine_wifi_mode - wifi_mode :{}".format(wifi_mode))
        logging.info("change_machine_wifi_mode - device_mode :{}".format(device_mode))

        # CHANGE DEVICE MODE
        msg = {"device_mode": device_mode}

        utility_event_data["event_data"] = {"msg_type": DEVICE_MODE_UPDATE_MESSAGE_TYPE_ID, "msg": msg}
        utility_event_data["response_required"] = True

        status = trigger_event(utility_event_data, "/utility_event_lock")

        if status == SUCCESS:
            logging.debug("SUCCESSFULLY changed to DEVICE mode")

            # CHANGE WIFI MODE
            msg = {"SSID": None, "PSK": None, "Previous_ssid": None,
                             "Previous_psk": None,
                             "network_mode": wifi_mode, "wifi_status":None}

            utility_event_data["event_data"] = {"msg_type": WIFI_INFO_MESSAGE_TYPE_ID, "msg": msg}
            utility_event_data["response_required"] = True

            wifi_mode_update_status = trigger_event(utility_event_data, "/utility_event_lock")

            if wifi_mode_update_status == SUCCESS:
                utility_event_data["event_data"] = {"msg_type": REBOOT_MESSAGE_TYPE_ID}
                utility_event_data["response_required"] = True

                status = trigger_event(utility_event_data, "/utility_event_lock")

        else:
            logging.debug("ERROR in change WIFI mode")

    except Exception as error:
        logging.exception("change_machine_wifi_mode - {}".format(error))


def trigger_event(event_trigger_data, lock):
    # It indicates the event_lock state, whether it is in the acquired state or released state
    event_lock_status = False
    try:
        logging.info("trigger_event - event triggered({})".format(lock))

        # Acquiring lock to avoid race condition at the event access.
        if(lock != "/backend_to_gui_event_lock" and DEVICE_TYPE != PANTRY_TYPE):
            server_communication_system_resources[lock].acquire(timeout=LOCK_ACQUIRE_TIME_OUT)
            logging.info("trigger_event - {} event_lock acquired".format(lock))
            event_lock_status = True
            event_response = trigger_event_handler_framework(event_trigger_data)

            if event_trigger_data["response_required"]:
                return event_response

    except Exception as error:
        logging.exception("trigger_event - lock name - {} :{}".format(lock, error))

    finally:
        # We are using the counting semaphore for the lock. So, we need to maintain it's lock count as 1.
        # Every release call increases it's lock count by 1.
        # So, we need to release the lock only if we were acquired it.
        if event_lock_status:
            server_communication_system_resources[lock].release()
            logging.info("trigger_event - {} event_lock released".format(lock))


def get_current_time():
    try:

        global wifi_of_time, wifi_wait_minus
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        time = re.split(':', current_time)

        if wifi_of_time is None:
            wifi_of_time = current_time
            logging.debug("wifi_of_time - {}".format(wifi_of_time))
            wifi_of_time = re.split(":", wifi_of_time)

            current_minus = int(wifi_of_time[1])

            wifi_off_minus = current_minus

            logging.debug("wifi_off_minus - {}".format(wifi_off_minus))
            wifi_wait_minus = wifi_off_minus + MAX_WIFI_WAIT_TIME

            if wifi_wait_minus >= 60:
                wifi_wait_minus = wifi_wait_minus - 60

            logging.debug("wifi_wait_minus - {}".format(wifi_wait_minus))

        minus = time[1]

        return minus

    except Exception as error:
        logging.exception("trigger_event - lock name - {} :{}".format(error))


def update_wifi_status():
    try:
        global gui_event_trigger_data, server_communication_event_handler_data, utility_event_data, wifi_of_time, wifi_wait_minus
        global default_wifi_mode, previous_wifi_name, previous_wifi_password

        wifi_info = get_wifi_info()

        device_provision_info = {}
        if read_from_file(device_provision_info, \
                          DEVICE_PROVISION_INFO_FILE) == FAILURE:
            logging.debug("DEVICE_PROVISION_INFO_FILE read error")
            return

        if wifi_info["Previous_ssid"] is None or device_provision_info["network_mode"] == ORGANIZATION_WIFI:

            wifi_config_data = {}

            logging.debug("----------update_wifi_status function started -------")

            if read_from_file(wifi_config_data, WIFI_CONF_FILE) == FAILURE:
                raise Exception("update_wifi_status : File reading error in " + WIFI_CONF_FILE)

            wifi_conn_status = check_connectivity(WIFI_INTERFACE_NAME)

            if wifi_conn_status:
                wifi_data = {"SSID": wifi_config_data["SSID"], "PSK": wifi_config_data["PSK"], "Previous_ssid": None,
                             "Previous_psk": None,
                             "network_mode": None, "wifi_status": True}

                utility_event_data["event_data"] = {"msg_type": WIFI_INFO_MESSAGE_TYPE_ID,
                                                    "msg": wifi_data}
                utility_event_data["response_required"] = True

                status = trigger_event(utility_event_data, "/utility_event_lock")
                logging.info("save_status for current wifi details to previous wifi details - {}".format(status))

            if not wifi_conn_status:

                logging.warning(" -*-*-*-*-*- wifi not connected -*-*-*-*-*-")

                #if previous_wifi_name is None and wifi_config_data["Previous_ssid"] is None:
                wifi_data = {"SSID": wifi_config_data["SSID"], "PSK": wifi_config_data["PSK"],
                             "Previous_ssid": wifi_config_data["SSID"], "Previous_psk": wifi_config_data["PSK"],
                             "network_mode": None, "wifi_status": False}

                utility_event_data["event_data"] = {"msg_type": WIFI_INFO_MESSAGE_TYPE_ID,
                                                    "msg": wifi_data}
                utility_event_data["response_required"] = True

                status = trigger_event(utility_event_data, "/utility_event_lock")
                logging.info("save_status for current wifi details to previous wifi details - {}".format(status))

                previous_wifi_name = wifi_config_data["SSID"]
                previous_wifi_password = wifi_config_data["PSK"]

                terminate_wifi()
                wifi_reconn_status = connect_wifi(wifi_config_data["SSID"], wifi_config_data["PSK"])

                #if wifi_reconn_status:
                wifi_data = {"SSID": wifi_config_data["SSID"], "PSK": wifi_config_data["PSK"],
                             "Previous_ssid": wifi_config_data["SSID"], "Previous_psk": wifi_config_data["PSK"],
                             "network_mode": None, "wifi_status": wifi_reconn_status}

                utility_event_data["event_data"] = {"msg_type": WIFI_INFO_MESSAGE_TYPE_ID,
                                                    "msg": wifi_data}
                utility_event_data["response_required"] = True

                status = trigger_event(utility_event_data, "/utility_event_lock")
                logging.info("save_status for current wifi details to previous wifi details - {}".format(status))

                if wifi_reconn_status == False:

                    current_minus = get_current_time()
                    logging.info("update_wifi_status - wifi_wait_minus - {}".format(wifi_wait_minus))
                    logging.info("update_wifi_status - current_minus - {}".format(current_minus))

                    if wifi_wait_minus == int(current_minus) or int(current_minus) > wifi_wait_minus:

                        logging.warning(" -*-*-*-*-*- wifi not connected in long time -*-*-*-*-*-")

                        default_wifi_mode = True
                        logging.info("change wifi to DEVICE-WIFI mode")

                        default_wifi_config_data = {}
                        if read_from_file(default_wifi_config_data, FEATURE_CONF_FILE) == FAILURE:
                            raise Exception("update_wifi_status : File reading error in " + FEATURE_CONF_FILE)

                        ssid = default_wifi_config_data['other_parameters']['default_device_ssid']

                        logging.info("defaul ssid - {}".format(ssid))

                        wifi_data = {"SSID": wifi_config_data["SSID"], "PSK": wifi_config_data["PSK"], "Previous_ssid": wifi_config_data["SSID"],
                                     "Previous_psk": wifi_config_data["PSK"],
                                     "network_mode": None, "wifi_status": False}
                        utility_event_data["event_data"] = {"msg_type": WIFI_INFO_MESSAGE_TYPE_ID,
                                                            "msg": wifi_data}
                        utility_event_data["response_required"] = True
                        status = trigger_event(utility_event_data, "/utility_event_lock")
                        logging.info("save_status for default ssid details - {}".format(status))

                        if status == SUCCESS:
                            logging.info("successfully configured default ssid and password")

                            wifi_of_time = None
                            wifi_wait_minus = None

                            change_machine_wifi_mode(INTRANET_MODE, MACHINE_WIFI)

                if wifi_reconn_status == FAILURE:
                    logging.exception("Error occurred while turn on the wlan0 interface")

            logging.debug("update_wifi_status - wifi_connection_status : %s", wifi_conn_status)

            if device_provision_info["provision_status"]:

                if wifi_conn_status and not server_communication_system_resources["wifi_connection_status_event"].isSet():
                    server_communication_system_resources["wifi_connection_status_event"].set()
                    if DEVICE_TYPE != PANTRY_TYPE:
                        gui_event_trigger_data["event_data"] = {"msg_type": WIFI_STATUS_MESSAGE_TYPE_ID, "msg": True}
                        trigger_event(gui_event_trigger_data, "/backend_to_gui_event_lock")
                elif not wifi_conn_status and server_communication_system_resources["wifi_connection_status_event"].isSet():
                    server_communication_system_resources["wifi_connection_status_event"].clear()
                    if DEVICE_TYPE != PANTRY_TYPE:
                        gui_event_trigger_data["event_data"] = {"msg_type": WIFI_STATUS_MESSAGE_TYPE_ID, "msg": False}
                        trigger_event(gui_event_trigger_data, "/backend_to_gui_event_lock")
                else:
                    logging.debug("update_wifi_status - same wifi state")

        elif wifi_info["Previous_ssid"] is not None:

            logging.info("Checking previous_wifi availability")
            wifi_available_status = check_wifi_availability(wifi_info["Previous_ssid"])
            logging.info(
                "previous_wifi {} available status - {}".format(wifi_info["Previous_ssid"], wifi_available_status))

            if wifi_available_status:
                default_wifi_mode = False
                logging.info("Go back to previous_wifi - {}".format(wifi_info["Previous_ssid"]))

                wifi_data = {"SSID": wifi_info["Previous_ssid"], "PSK": wifi_info["Previous_psk"],
                             "Previous_ssid": None, "Previous_psk": None,
                             "network_mode": None, "wifi_status": True}
                utility_event_data["event_data"] = {"msg_type": WIFI_INFO_MESSAGE_TYPE_ID,
                                                    "msg": wifi_data}
                utility_event_data["response_required"] = True
                save_status = trigger_event(utility_event_data, "/utility_event_lock")

                logging.debug("save_status for previous_wifi details - {}".format(save_status))

                if save_status == SUCCESS:
                    change_machine_wifi_mode(INTERNET_MODE, ORGANIZATION_WIFI)

    except Exception as error:
        logging.exception("update_wifi_status - : {}".format(error))

    finally:
        # pass
        logging.debug("----------update_wifi_status function finished -------")


def server_communication_queue_handler(input_data):
    try:

        pass

        response = None

        if input_data['msg_type'] == WIFI_STATUS_MESSAGE_TYPE_ID:
            update_wifi_status()

        elif input_data['msg_type'] == CONNECT_WIFI_MESSAGE_TYPE_ID:
            wifi_health_status = connect_wifi(input_data["msg"][0], input_data["msg"][1])
            response = {"msg_type": CONNECT_WIFI_MESSAGE_TYPE_ID, "msg": wifi_health_status}

        elif input_data['msg_type'] == RESET_WIFI_CONFIG_FILE_MSG_TYPE_ID:
            logging.debug("RESET_WIFI_CONFIG_FILE_MSG_TYPE_ID")
            update_wifi_config_file()
            response = {"msg_type": RESET_WIFI_CONFIG_FILE_MSG_TYPE_ID, "msg": True}

        elif input_data['msg_type'] == WIFI_AVAILABILITY_MESSAGE_TYPE_ID:
            wifi_available_status = check_wifi_availability(input_data["msg"][0])
            response = {"msg_type": WIFI_AVAILABILITY_MESSAGE_TYPE_ID, "msg": wifi_available_status}

        elif input_data['msg_type'] == GSM_AVAILABILITY_MESSAGE_TYPE_ID:
            gsm_available_status = check_connectivity(GSM_INTERFACE_NAME)
            response = {"msg_type": GSM_AVAILABILITY_MESSAGE_TYPE_ID, "msg": gsm_available_status}

        else:
            logging.warning("server_communication_queue_handler : Invalid msg_type")

        if response is not None:
            logging.info("server_communication_queue_handler response is :{}".format(response))
            return response
    except Exception as error:
        logging.exception("server_communication_queue_handler -  {}".format(error))


def update_gsm_status():

    try:
        global gui_event_trigger_data, server_communication_event_handler_data, utility_event_data, wifi_of_time, wifi_wait_minus
        global default_wifi_mode, previous_wifi_name, previous_wifi_password

        logging.debug("update_gsm_status")
        device_provision_info = {}

        if read_from_file(device_provision_info, \
                          DEVICE_PROVISION_INFO_FILE) == FAILURE:
            logging.debug("DEVICE_PROVISION_INFO_FILE read error")
            return

        logging.debug("check_connectivity - gsm")
        gsm_conn_status = check_connectivity(GSM_INTERFACE_NAME)
        logging.debug("check_connectivity - gsm_conn_status - {}".format(gsm_conn_status))

        gsm_data = {"APN_name": None, "server_ip": None, "gsm_status": gsm_conn_status, "network_mode": GSM}

        utility_event_data["event_data"] = {"msg_type": GSM_INFO_MESSAGE_TYPE_ID,
                                            "msg": gsm_data}
        utility_event_data["response_required"] = True

        status = trigger_event(utility_event_data, "/utility_event_lock")
        logging.info("save_status for current gsm details - {}".format(status))

        if device_provision_info["provision_status"]:

            if gsm_conn_status and not server_communication_system_resources["wifi_connection_status_event"].isSet():
                server_communication_system_resources["wifi_connection_status_event"].set()
                if DEVICE_TYPE == RETRO_FIT_TYPE:
                    gui_event_trigger_data["event_data"] = {"msg_type": GSM_STATUS_MESSAGE_TYPE_ID, "msg": True}
                    trigger_event(gui_event_trigger_data, "/backend_to_gui_event_lock")
            elif not gsm_conn_status and server_communication_system_resources["wifi_connection_status_event"].isSet():
                server_communication_system_resources["wifi_connection_status_event"].clear()
                if DEVICE_TYPE == RETRO_FIT_TYPE:
                    gui_event_trigger_data["event_data"] = {"msg_type": GSM_STATUS_MESSAGE_TYPE_ID, "msg": False}
                    trigger_event(gui_event_trigger_data, "/backend_to_gui_event_lock")
            else:
                logging.debug("update_gsm_status - same gsm state")

            if not gsm_conn_status:

                logging.debug("GSM not Available")

                current_minus = get_current_time()
                logging.info("update_wifi_status - wifi_wait_minus - {}".format(wifi_wait_minus))
                logging.info("update_wifi_status - current_minus - {}".format(current_minus))

                if wifi_wait_minus == int(current_minus) or int(current_minus) > wifi_wait_minus:

                    logging.warning(" -*-*-*-*-*- gsm not connected in long time -*-*-*-*-*-")

                    default_wifi_mode = True
                    logging.info("change wifi to DEVICE-WIFI mode")

                    default_wifi_config_data = {}
                    if read_from_file(default_wifi_config_data, FEATURE_CONF_FILE) == FAILURE:
                        raise Exception("update_wifi_status : File reading error in " + FEATURE_CONF_FILE)

                    ssid = default_wifi_config_data['other_parameters']['default_device_ssid']

                    logging.info("defaul ssid - {}".format(ssid))

                    wifi_data = {"SSID": ssid, "PSK": None, "Previous_ssid": None,
                                 "Previous_psk": None,
                                 "network_mode": None, "wifi_status": False}
                    utility_event_data["event_data"] = {"msg_type": WIFI_INFO_MESSAGE_TYPE_ID,
                                                        "msg": wifi_data}
                    utility_event_data["response_required"] = True
                    status = trigger_event(utility_event_data, "/utility_event_lock")
                    logging.info("save_status for default ssid details - {}".format(status))

                    if status == SUCCESS:
                        logging.info("successfully configured default ssid and password")

                        wifi_of_time = None
                        wifi_wait_minus = None

                        change_machine_wifi_mode(INTRANET_MODE, MACHINE_WIFI)

        wifi_config_data = {}

        if read_from_file(wifi_config_data, WIFI_CONF_FILE) == FAILURE:
            raise Exception("update_wifi_status : File reading error in " + WIFI_CONF_FILE)

        if wifi_info["Previous_ssid"] is not None:

            logging.info("Checking previous_wifi availability")
            gsm_available_status = check_connectivity(GSM_INTERFACE_NAME)
            logging.info(
                "previous_gsm available status - {}".format(gsm_available_status))

            if gsm_available_status:
                default_wifi_mode = False
                logging.info("Go back to previous_wifi - {}".format(wifi_info["Previous_ssid"]))

                wifi_data = {"SSID": None, "PSK": None,
                             "Previous_ssid": None, "Previous_psk": None,
                             "network_mode": None, "wifi_status": False}
                utility_event_data["event_data"] = {"msg_type": WIFI_INFO_MESSAGE_TYPE_ID,
                                                    "msg": wifi_data}
                utility_event_data["response_required"] = True
                save_status = trigger_event(utility_event_data, "/utility_event_lock")

                logging.debug("save_status for previous_wifi details - {}".format(save_status))

                if save_status == SUCCESS:

                    gsm_data = {"APN_name": None, "server_ip": None, "gsm_status": True, "network_mode": GSM}

                    utility_event_data["event_data"] = {"msg_type": GSM_INFO_MESSAGE_TYPE_ID,
                                                        "msg": gsm_data}
                    utility_event_data["response_required"] = True

                    status = trigger_event(utility_event_data, "/utility_event_lock")
                    logging.info("save_status for current gsm details - {}".format(status))

                    change_machine_wifi_mode(INTERNET_MODE, ORGANIZATION_WIFI)

    except Exception as error:
        logging.exception("update_gsm -  {}".format(error))


def update_gsm():
    try:
        server_communication_event_lock_status = None

        server_communication_system_resources["/server_communication_event_lock"].acquire(
            timeout=LOCK_ACQUIRE_TIME_OUT)
        logging.debug("update_wifi_status : server_communication_event_lock acquired")
        server_communication_event_lock_status = True

        update_gsm_status()

    except Exception as error:
        logging.exception("update_gsm -  {}".format(error))

    finally:
        if server_communication_event_lock_status:
            server_communication_system_resources["/server_communication_event_lock"].release()
            logging.info("update_gsm_status : server_communication_event_lock released")

        start_update_gsm_status_timer()


def update_wifi_connection():
    try:
        logging.debug("update_wifi_connection")
        server_communication_event_lock_status = None

        server_communication_system_resources["/server_communication_event_lock"].acquire(
            timeout=LOCK_ACQUIRE_TIME_OUT)
        logging.debug("update_wifi_status : server_communication_event_lock acquired")
        server_communication_event_lock_status = True

        update_wifi_status()

    except Exception as error:
        logging.exception("update_wifi -  {}".format(error))

    finally:
        if server_communication_event_lock_status:
            server_communication_system_resources["/server_communication_event_lock"].release()
            logging.info("update_wifi_connection : server_communication_event_lock released")

        start_update_wifi_status_timer()


def start_update_gsm_status_timer():
    try:
        update_gsm_status_timer = threading.Timer(WIFI_STATUS_CHECK_INTERVAL, update_gsm)
        update_gsm_status_timer.start()
    except Exception as error:
        logging.exception("start_update_gsm_status_timer -  {}".format(error))


def start_update_wifi_status_timer():
    try:
        logging.debug("start_update_wifi_status_timer")
        update_wifi_status_timer = threading.Timer(WIFI_STATUS_CHECK_INTERVAL, update_wifi_connection)
        update_wifi_status_timer.start()
    except Exception as error:
        logging.exception("start_update_wifi_status_timer -  {}".format(error))


def server_communication_event_handler():
    logging.info("server_communication_event_handler - Server_Communication process started")
    global gui_event_trigger_data, server_communication_event_handler_data, utility_event_data

    try:
        
        available_wifi_list()
        device_provision_info = {}
        if read_from_file(device_provision_info, \
                          DEVICE_PROVISION_INFO_FILE) == FAILURE:
            logging.debug("DEVICE_PROVISION_INFO_FILE read error")
            return

        wifi_info = get_wifi_info()
        logging.debug("Previous_ssid - {}".format(wifi_info["Previous_ssid"]))
        logging.debug("device_mode - {}".format(device_provision_info["device_mode"]))
        
        #if device_provision_info["device_mode"] == INTERNET_MODE or wifi_info["Previous_ssid"] is not None:

        # Register the Server_Communication to the Diagnostics module to know the run time errors.
        if update_process_id("Server_Communication") == FAILURE:
            logging.exception("server_communication_event_handler - Error in update_process_id")

        # Initializing the MB_IO_HANDLER_SERVICE.
        if initialize_service(server_communication_system_resources, SERVER_COMMUNICATION_SERVICE) == FAILURE:
            raise Exception("Server_Communication initialization failed")
        logging.info(
            "server_communication_event_handler - Server_Communication service system_resources initialized successfully")
        logging.info("server_communication_system_resources - {}".format(server_communication_system_resources))

        utility_event_data = {"thread_name": "Server_Communication",
                              "event": server_communication_system_resources["utility_event"],
                              "queue": server_communication_system_resources["/utility_queue"], "event_data": None,
                              "finished_event": server_communication_system_resources["utility_finished_event"],
                              "response_required": None}

        logging.debug(
            "server_communication_event_handler - utility_event_trigger_data - {}".format(utility_event_data))

        device_type = device_provision_info["device_type"]

        # PRE PROVISION STAGE
        if not device_provision_info["provision_status"]:
            logging.debug("-------call wifi connection function started ----------")

            if device_provision_info["network_mode"] == ORGANIZATION_WIFI:
                update_wifi_status()
                
            elif device_provision_info["network_mode"] == GSM:
                pass

            device_name = device_provision_info["device_name"]
            logging.debug("device_name - {}".format(device_name))

            if device_name is not None:
                utility_event_data["response_required"] = True
                utility_event_data["event_data"] = {"msg_type": GET_DEVICE_ID_MESSAGE_TYPE, "msg": device_name}

                # WAIT AND GET EVENT RESPONSE
                utility_event_data_response = trigger_event(utility_event_data, "/utility_event_lock")

                logging.info(
                    "GET_DEVICE_ID_MESSAGE_TYPE : utility_event_data_response - {}".format(
                        utility_event_data_response))

                code = utility_event_data_response['code']

                if code == SUCCESS:
                    logging.debug("--------- SUCCESSFULLY GET DEVICE DETAILS ---------")
                    utility_event_data["event_data"] = {"msg_type": INIT_PROVISION_MESSAGE_TYPE_ID, "msg": "reboot"}
                    utility_event_data_response = trigger_event(utility_event_data, "/utility_event_lock")

                else:
                    logging.debug("--------- FAILED TO GET DEVICE DETAILS ---------")

                    update_wifi_config_file()

                    utility_event_data["event_data"] = {"msg_type": APPLICATION_RESET_MESSAGE_TYPE_ID}

                    # WAIT AND GET EVENT RESPONSE
                    utility_event_data_response = trigger_event(utility_event_data, "/utility_event_lock")

                    logging.info(
                        "APPLICATION_RESET_MESSAGE_TYPE_ID : utility_event_data_response - {}".format(
                            utility_event_data_response))

            logging.debug("-------call wifi connection function finished ----------")

        # POST PROVISION STAGE
        if device_provision_info["provision_status"]:

            try:
                if device_provision_info["device_mode"]=="Inter_Mode":
                    strength_finder_thread=threading.Thread(target=lavazza_cfds_signal_strength.start_signal_strength)
                    strength_finder_thread.start()

                server_communication_event_handler_data = {"thread_name": "Server_Communication",
                                                           "event": server_communication_system_resources[
                                                               "server_communication_event"],
                                                           "queue": server_communication_system_resources[
                                                               "/server_communication_queue"],
                                                           "queue_handler_function": server_communication_queue_handler,
                                                           "finished_event": server_communication_system_resources[
                                                               "server_communication_finished_event"]}
                logging.debug(
                    "server_communication_event_handler - server_communication_event_handler_data {}".format(
                        server_communication_event_handler_data))

                if device_type != PANTRY_TYPE:
                    # gui_event_trigger_data is used to communicate with the gui
                    gui_event_trigger_data = {"thread_name": "Server_Communication",
                                              "event": server_communication_system_resources[
                                                  "backend_to_gui_event"],
                                              "queue": server_communication_system_resources[
                                                  "/backend_to_gui_queue"],
                                              "event_data": None,
                                              "finished_event": server_communication_system_resources[
                                                  "backend_to_gui_finished_event"],
                                              "response_required": False}
                    logging.debug(
                        "server_communication_event_handler - gui_event_trigger_data - {}".format(
                            gui_event_trigger_data))

            except Exception as error:
                logging.exception("server_communication_event_handler - {}".format(error))

            if device_provision_info["network_mode"] == ORGANIZATION_WIFI:
                logging.debug("-------call update_wifi_status function start first time ----------")
                update_wifi_status()
                logging.debug("-------call update_wifi_status function finish first time ----------")

            elif device_provision_info["network_mode"] == GSM:
                logging.debug("-------call update_gsm_status function start first time ----------")
                update_gsm_status()
                logging.debug("-------call update_gsm_status function finish first time ----------")

            server_upload_handler_thread = threading.Thread(
                target=upload_to_server_event_handler,
                args=[server_communication_system_resources])

            wifi_info = get_wifi_info()

            if device_provision_info["network_mode"] == MACHINE_WIFI and wifi_info["Previous_ssid"] is None:
                logging.debug("Machine is in 'machine' wifi mode.....no need to run server communication")
                return

            if device_provision_info["network_mode"] == ORGANIZATION_WIFI or wifi_info["Previous_ssid"] is not None:
                logging.debug("------------------- ORGANIZATION_WIFI ------------------")
                start_update_wifi_status_timer()
                
            elif device_provision_info["network_mode"] == GSM:
                logging.debug("------------------- GSM ------------------")
                start_update_gsm_status_timer()

            
            if device_provision_info["network_mode"] == ORGANIZATION_WIFI or device_provision_info["network_mode"] == GSM:
                server_upload_handler_thread.start()

            while True:
                try:
                    logging.info("server_communication_event_handler - Waiting for the server communication event")
                    event_handler_framework(server_communication_event_handler_data)
                    logging.info(
                        "server_communication_event_handler - server_communication_event_handler function finished")

                except Exception as error:
                    logging.exception("server_communication_event_handler - {}".format(error))

    except Exception as error:
        logging.exception("server_communication_event_handler - {}".format(error))


server_communication_event_handler()
