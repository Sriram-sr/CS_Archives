"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_utility_keep_alive_handler.py
 * Version        : 1.1
 * Date           : MAY 04 2021
 *
 * Copyright (C) mieuPro Systems, 2021
 *
 ******************************************************************************
 """

import time
import threading
from datetime import datetime
from subprocess import Popen, PIPE
from lavazza_cfds_utility_keep_alive_handler_macros import *

import lavazza_cfds_utility_macros
import logging,codecs

keep_alive_current_msg_id = 0

def ip_finder():
    try:
        output={}
        command="ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'"
        process=Popen(command,shell=True,stdout=PIPE,stderr=PIPE)
        stdout,stderr=process.communicate()
        stdout=(codecs.decode(stdout,'unicode_escape')).replace("\n","")
        output.update({"ip_address":codecs.decode(stdout,"unicode_escape")})
        logging.info("ip_address is {}".format(stdout))
        if stdout:
            return output
        else:
            output={}
            output["ip_address"]="not found"
            return output
    except Exception as error:
        output={}
        output["ip_address"]="not found"
        logging.exception("ip_address : {}".format(error))
        return output


def get_cpu_mem_info():

    try:

        cpu_idle_time = {}
        total_memory = {}
        available_memory = {}

        if lavazza_cfds_utility_macros.command_executor(
                total_memory, TOTAL_MEMORY_CMD) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("command_executor error")

        total_memory = float(total_memory['stdout'].decode("utf-8"))

        if lavazza_cfds_utility_macros.command_executor(available_memory, AVAILABLE_MEMORY_CMD) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("command_executor error")
        available_memory = float(available_memory['stdout'].decode("utf-8"))

        if lavazza_cfds_utility_macros.command_executor(cpu_idle_time, CPU_IDLE_TIME_CMD) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("command_executor error")

        cpu_idle_time = float(cpu_idle_time['stdout'].decode("utf-8"))
        logging.info("total_memory={}".format(total_memory))
        logging.info("available_memory={}".format(available_memory))
        logging.info("cpu_idle_time={}".format(cpu_idle_time))

        cpu_usage = "%s%s" % ((100 - cpu_idle_time), '%')
        memory_usage = "%s%s" % (((total_memory - available_memory)/80), '%')

        cpu_mem_info = {"cpu_utilization": cpu_usage, "memory_utilization": memory_usage}

        return cpu_mem_info
    except Exception as error:
        logging.exception("get_cpu_mem_info : {}".format(error))


def get_network_status():

    network_status = {}
    if lavazza_cfds_utility_macros.read_from_file(
            network_status, lavazza_cfds_utility_macros.NETWORK_STATUS_FILE) == lavazza_cfds_utility_macros.FAILURE:
        raise Exception("File reading error in " + lavazza_cfds_utility_macros.NETWORK_STATUS_FILE)

    return network_status


def get_system_last_time_sync():

    logging.info("LOG Keep_Alive_Handler : inside get_system_last_time_sync")
    output = {}
    system_last_time_sync = None

    try:
        if lavazza_cfds_utility_macros.command_executor(output, GET_NTP_MESSAGE_CMD) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("command_executor error")

        ntp_message = output['stdout'].decode()
        ref = ntp_message.find("DestinationTimestamp")
        t1 = ntp_message[ref + NTP_MESSAGE_DATETIME_STRING_STARTING_INDEX: ref + NTP_MESSAGE_DATETIME_STRING_ENDING_INDEX]
        t1 = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
        t1_sec = time.mktime(t1.timetuple())
        t2 = datetime.now()
        t2_sec = time.mktime(t2.timetuple())
        system_last_time_sync = str(t2_sec - t1_sec)
        logging.info("LOG Keep_Alive_Handler : Last time sync occurred before {} secs".format(system_last_time_sync))
        if system_last_time_sync == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("get_system_last_time_sync error")

        system_last_time_sync = {"time_sync":system_last_time_sync}
        return system_last_time_sync

    except Exception as error:
        logging.exception("ERROR get_system_last_time_sync: {}".format(error))
        return lavazza_cfds_utility_macros.FAILURE


def keep_alive_handler():

    try:

        logging.debug("Keep_Alive_Handler")
        url_list = []
        device_provision_details = {}
        wifi_info = {}

        if lavazza_cfds_utility_macros.read_from_file(
            wifi_info, lavazza_cfds_utility_macros.WIFI_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("File reading error in " + lavazza_cfds_utility_macros.WIFI_CONF_FILE)

        logging.debug("wifi_status - {}".format(wifi_info["wifi_status"]))

        if wifi_info["wifi_status"]:
                      
            if lavazza_cfds_utility_macros.read_from_file(
                    device_provision_details, lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:
                raise Exception("File reading error in " + lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE)

            if device_provision_details["provision_status"]:

                logging.debug("Keep_Alive_Handler : keep alive handler getting started")
                last_time_sync_payload = get_system_last_time_sync()
                cpu_mem_payload = get_cpu_mem_info()
                ip_address = ip_finder()                
                payload = {**last_time_sync_payload, **cpu_mem_payload, **ip_address}
                logging.debug(payload)

                if lavazza_cfds_utility_macros.write_to_file(payload,lavazza_cfds_utility_macros.KEEP_ALIVE_FILE) < 0:
                    raise Exception("write_to_file error in" + lavazza_cfds_utility_macros.KEEP_ALIVE_FILE)

                if lavazza_cfds_utility_macros.add_to_url_list(
                        lavazza_cfds_utility_macros.KEEP_ALIVE_SERVER, url_list, KEEP_ALIVE_SERVER_PATH) < 0:
                    raise Exception("get_url_list error in keep_alive")

                server_upload_data = {"file_type": "keep_alive", "file_path": lavazza_cfds_utility_macros.KEEP_ALIVE_FILE,
                                      "url_list": url_list, "retry_on_error": False,
                                      "delete_on_success": False}

                if lavazza_cfds_utility_macros.add_to_upload_data_list(
                        lavazza_cfds_utility_macros.utility_system_events_queues["server_upload_event"], server_upload_data) == lavazza_cfds_utility_macros.FAILURE:
                    raise Exception("add_to_upload_data_list error in keep_alive")

                return None
        
    except Exception as error:
        logging.exception("ERROR Keep_Alive_Handler: {}".format(error))

    finally:
        start_keep_alive_timer()


def start_keep_alive_timer():

    try:

        if lavazza_cfds_utility_macros.read_from_file(
                lavazza_cfds_utility_macros.feature_configs, lavazza_cfds_utility_macros.FEATURE_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("File reading error in " + lavazza_cfds_utility_macros.FEATURE_CONF_FILE)

        logging.info("feature_configs :{}".format(lavazza_cfds_utility_macros.feature_configs))

        keep_alive_interval = lavazza_cfds_utility_macros.feature_configs["keep_alive"]["keep_alive_interval"]
        
        logging.info("Keep_Alive_Handler : start_keep_alive_timer getting started")
        logging.info("keep_alive_interval - {}".format(keep_alive_interval))
        keep_alive_timer = threading.Timer(keep_alive_interval, keep_alive_handler)
        keep_alive_timer.start()

    except Exception as error:
        logging.exception("ERROR start_keep_alive_timer: {}".format(error))


def update_device_info_to_server():
    try:
        logging.debug("update_device_info_to_server")

        url_list = []
        device_provision_details = {}

        if lavazza_cfds_utility_macros.read_from_file(
                device_provision_details,
                lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("File reading error in " + lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE)

        if device_provision_details["provision_status"]:

            if lavazza_cfds_utility_macros.add_to_url_list(
                    lavazza_cfds_utility_macros.CONFIGURATION_SERVER, url_list, PROVISION_UPDATE_SERVER_PATH) < 0:
                raise Exception("get_url_list error in update_device_info_to_server")

            server_upload_data = {"file_type": "provision_update", "file_path": lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE,
                                  "url_list": url_list, "retry_on_error": False,
                                  "delete_on_success": False}

            if lavazza_cfds_utility_macros.add_to_upload_data_list(
                    lavazza_cfds_utility_macros.utility_system_events_queues["server_upload_event"], server_upload_data) == lavazza_cfds_utility_macros.FAILURE:
                raise Exception("add_to_upload_data_list error in update_device_info_to_server")

            return None

    except Exception as error:
        logging.exception("ERROR update_device_info_to_server: {}".format(error))
