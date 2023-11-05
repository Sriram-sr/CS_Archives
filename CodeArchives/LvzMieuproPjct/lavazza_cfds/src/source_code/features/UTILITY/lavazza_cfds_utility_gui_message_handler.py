"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_utility_gui_message_handler.py
 * Version        : 1.1
 * Date           : APRIL 20 2021
 *
 * Copyright (C) mieuPro Systems, 2021
 *
 ******************************************************************************
 """
# def gui_background_change(): - trigger gui periodically for gui_background_change
# device_power_off(msg): - shutdown or reboots the system
# def application_reset(msg): - reset the lavazza_project
# def update_device_provision_info(msg_type,key,value,event_to_peform): - Updates the product names or provision_status in device_provision_info
# def update_hotspot_info(ssid): - updates the ssid in the  hotspot config file
# def update_device_info(msg_type,msg): - updates hotspot config file and device_provision_info

import posix_ipc
import lavazza_cfds_utility_macros
import logging
import re
from filelock import FileLock
import requests


def disable_hotspot():

    try:

        dhcpcd_conf_file_data = []
        if lavazza_cfds_utility_macros.read_from_system_file(dhcpcd_conf_file_data,
                                                             lavazza_cfds_utility_macros.DHCPCD_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            logging.exception("Error occurred while reading dhcpcd conf file")
            return lavazza_cfds_utility_macros.FAILURE
        splitted_dhcpcd_data = dhcpcd_conf_file_data[0].split("\n")

        while "" in splitted_dhcpcd_data:
            splitted_dhcpcd_data.remove("")

        if splitted_dhcpcd_data[-1] == lavazza_cfds_utility_macros.DENY_INTERFACES:
            new_dhcpcd_data = "\n".join(splitted_dhcpcd_data[:-1])
        else:
            new_dhcpcd_data = "\n".join(splitted_dhcpcd_data[:])
        if lavazza_cfds_utility_macros.write_to_system_file(new_dhcpcd_data,
                                                            lavazza_cfds_utility_macros.DHCPCD_CONF_FILE,
                                                            'w+') == lavazza_cfds_utility_macros.FAILURE:
            logging.exception("Error occured while writing to dhcpcd conf file")
            return lavazza_cfds_utility_macros.FAILURE
        if lavazza_cfds_utility_macros.write_to_system_file('', lavazza_cfds_utility_macros.INTERFACE_CONF_FILE,
                                                            'w') == lavazza_cfds_utility_macros.FAILURE:
            logging.exception("Error occured while writing to interface conf file")
            return lavazza_cfds_utility_macros.FAILURE
        if lavazza_cfds_utility_macros.write_to_system_file('', lavazza_cfds_utility_macros.HOSTAPD_CONF_FILE,
                                                            'w') == lavazza_cfds_utility_macros.FAILURE:
            logging.exception("Error occured while writing to hostapd conf file")
            return lavazza_cfds_utility_macros.FAILURE
        cmd_output = {}
        if lavazza_cfds_utility_macros.command_executor(cmd_output,
                                                        lavazza_cfds_utility_macros.DISABLE_CMD) != lavazza_cfds_utility_macros.SUCCESS:
            return lavazza_cfds_utility_macros.FAILURE
        return lavazza_cfds_utility_macros.SUCCESS
    
    except Exception as error:
        logging.exception("error in disable hotspot : {} ".format(error))
        return lavazza_cfds_utility_macros.FAILURE


def enable_hotspot():

    try:

        dhcpcd_conf_file_data = []
        if lavazza_cfds_utility_macros.read_from_system_file(dhcpcd_conf_file_data,
                                                             lavazza_cfds_utility_macros.DHCPCD_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            logging.exception("Error occurred while reading dhcpcd conf file")
            return lavazza_cfds_utility_macros.FAILURE

        splitted_dhcpcd_data = dhcpcd_conf_file_data[0].split("\n")

        while "" in splitted_dhcpcd_data:
            splitted_dhcpcd_data.remove("")

        if splitted_dhcpcd_data[-1] != lavazza_cfds_utility_macros.DENY_INTERFACES:
            splitted_dhcpcd_data.append(lavazza_cfds_utility_macros.DENY_INTERFACES)
        new_dhcpcd_data = "\n".join(splitted_dhcpcd_data[:])

        if lavazza_cfds_utility_macros.write_to_system_file(new_dhcpcd_data,
                                                            lavazza_cfds_utility_macros.DHCPCD_CONF_FILE,
                                                            'w+') == lavazza_cfds_utility_macros.FAILURE:
            logging.exception("Error occurred while writing to dhcpcd conf file")

            return lavazza_cfds_utility_macros.FAILURE
        if lavazza_cfds_utility_macros.write_to_system_file(lavazza_cfds_utility_macros.ALLOW_INTERFACE,
                                                            lavazza_cfds_utility_macros.INTERFACE_CONF_FILE,
                                                            'w') == lavazza_cfds_utility_macros.FAILURE:
            logging.exception("Error occured while writing to interface conf file")
            return lavazza_cfds_utility_macros.FAILURE

        if lavazza_cfds_utility_macros.write_to_system_file(lavazza_cfds_utility_macros.HOSTAPD_ENABLE,
                                                            lavazza_cfds_utility_macros.HOSTAPD_CONF_FILE,
                                                            'w') == lavazza_cfds_utility_macros.FAILURE:
            logging.exception("Error occurred while writing to hostapd conf file")

            return lavazza_cfds_utility_macros.FAILURE
        cmd_output = {}

        if lavazza_cfds_utility_macros.command_executor(cmd_output,
                                                        lavazza_cfds_utility_macros.ENABLE_CMD) != lavazza_cfds_utility_macros.SUCCESS:
            logging.info("Command Output : ", cmd_output)
            return lavazza_cfds_utility_macros.FAILURE
        return lavazza_cfds_utility_macros.SUCCESS

    except Exception as error:
        logging.exception("error in enable hotspot : {} ".format(error))
        return lavazza_cfds_utility_macros.FAILURE


def device_power_off(msg):
    """shutdown or reboots the system based on the input"""
    try:

        logging.debug("Before acquiring shutdown_or_reboot_event_lock")
        with posix_ipc.Semaphore("/shutdown_or_reboot_event_lock"):
            logging.debug("After acquiring shutdown_or_reboot_event_lock")

            input_data = {"thread_name": "utility",
                          "event": lavazza_cfds_utility_macros.utility_system_events_queues["shutdown_or_reboot_event"],
                          "queue": lavazza_cfds_utility_macros.utility_system_events_queues[
                              "/shutdown_or_reboot_event_queue"],
                          "event_data": msg,
                          "finished_event": False, "response_required": False}

            lavazza_cfds_utility_macros.trigger_event_handler_framework(input_data)
            return None

    except:
        logging.exception("device_power_off")
        return None

def reset_wifi_config():

    try:

        logging.info("Before server_communication_event_lock")

        with lavazza_cfds_utility_macros.RaceConditionAvoidance(lavazza_cfds_utility_macros.utility_system_events_queues["/server_communication_event_lock"],
                                                                lavazza_cfds_utility_macros.LOCK_ACQUIRE_TIME_OUT):

            logging.info("After server_communication_event_lock")

            event_data = {"msg_type": lavazza_cfds_utility_macros.RESET_WIFI_CONFIG_FILE_MSG_TYPE_ID}

            server_communication_event_trigger_data = {"thread_name": "utility",
                                                   "event": lavazza_cfds_utility_macros.utility_system_events_queues[
                                                       "server_communication_event"],
                                                   "queue": lavazza_cfds_utility_macros.utility_system_events_queues[
                                                       "/server_communication_queue"],
                                                   "event_data": event_data,
                                                   "finished_event":
                                                       lavazza_cfds_utility_macros.utility_system_events_queues[
                                                           "server_communication_finished_event"],
                                                   "response_required": True}

            response = lavazza_cfds_utility_macros.trigger_event_handler_framework(server_communication_event_trigger_data)
            logging.debug("response - {}".format(response))
    except:
        logging.exception("reset_wifi_config")



def application_reset(msg):

    try:

        device_provision_info = {}

        if lavazza_cfds_utility_macros.read_from_file(device_provision_info, \
                                                      lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("DEVICE_PROVISION_INFO_FILE read error")

        for key in device_provision_info.keys():

            if key != "provision_status" and key != "num_of_stations" and key != "network_mode" and key != "device_mode":
                device_provision_info[key] = None
            elif key == "provision_status":
                device_provision_info[key] = False
            elif key == "num_of_stations":
                device_provision_info[key] = "20"
            elif key == "network_mode":
                device_provision_info[key] = lavazza_cfds_utility_macros.MACHINE_WIFI
            elif key == "device_mode":
                device_provision_info[key] = lavazza_cfds_utility_macros.INTRANET_MODE

        if lavazza_cfds_utility_macros.write_to_file(device_provision_info, \
                                                     lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("DEVICE_PROVISION_INFO_FILE write")

        # wifi info reset
        wifi_info = {}
        if lavazza_cfds_utility_macros.read_from_file(wifi_info, \
                                                      lavazza_cfds_utility_macros.WIFI_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("wifi conf file read error")

        for key in wifi_info:
            wifi_info[key] = None

        if lavazza_cfds_utility_macros.write_to_file(wifi_info, \
                                                     lavazza_cfds_utility_macros.WIFI_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("wifi conf file write error")

        # gsm info reset
        gsm_info = {}
        if lavazza_cfds_utility_macros.read_from_file(gsm_info, \
                                                      lavazza_cfds_utility_macros.GSM_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("gsm conf file read error")

        for gsm_key in gsm_info:
            gsm_info[gsm_key] = None

        if lavazza_cfds_utility_macros.write_to_file(gsm_info, \
                                                     lavazza_cfds_utility_macros.GSM_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("gsm conf file write error")

        if enable_hotspot() == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("Failed to enable the hotspot")
        else:
            logging.debug("Successfully enabled")

        feature_configs = {}
        if lavazza_cfds_utility_macros.read_from_file(feature_configs, \
                                                      lavazza_cfds_utility_macros.FEATURE_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("FEATURE_CONF_FILE read error")

        default_device_ssid = feature_configs["other_parameters"]["default_device_ssid"]
        default_wifi_clients = feature_configs["other_parameters"]["default_wifi_clients"]

        # updates the default ssid in the hotspot config file
        update_hotspot_info(default_device_ssid)

        # updates the default wifi clients in the hotspot config file
        update_station_info(default_wifi_clients)

        reset_wifi_config()
        
        device_power_off(msg)

        remove_qrcode()
        
        return None

    except:
        logging.exception("application_reset")
        return None


def update_hotspot_info(ssid):
    """ Updates the Hotspot conf file with ssid and password(if required) """

    try:

        with FileLock(lavazza_cfds_utility_macros.HOTSPOT_CONF_FILE + ".lock"):
            with open(lavazza_cfds_utility_macros.HOTSPOT_CONF_FILE) as f:
                lines = f.readlines()

        length = len(lines)

        change_ssid_line = "ssid=" + ssid + "\n"

        def check_pattern_and_replace(line_no, pattern_to_check, line_to_replace):

            pattern = re.compile(pattern_to_check)
            match = pattern.match(lines[line_no])
            if match:
                lines[line_no] = line_to_replace
                logging.debug("update_hotspot_info - ssid or pwd changed:", lines[line_no])

        for line_no in range(length):
            if "ssid" in lines[line_no]:
                logging.debug(lines[line_no])
                check_pattern_and_replace(line_no, "ssid", change_ssid_line)

        with FileLock(lavazza_cfds_utility_macros.HOTSPOT_CONF_FILE + ".lock"):
            with open(lavazza_cfds_utility_macros.HOTSPOT_CONF_FILE, "w") as f:
                f.writelines(lines)
    except:
        logging.exception("update_hotspot_info - Hotspot update info error")


def update_station_info(stations):
    """ Updates the Hotspot conf file with number of stations(if required) """

    try:

        with FileLock(lavazza_cfds_utility_macros.HOTSPOT_CONF_FILE + ".lock"):
            with open(lavazza_cfds_utility_macros.HOTSPOT_CONF_FILE) as f:
                lines = f.readlines()

        length = len(lines)

        change_station_line = "max_num_sta=" + str(stations) + "\n"

        def check_pattern_and_replace(line_no, pattern_to_check, line_to_replace):

            pattern = re.compile(pattern_to_check)
            match = pattern.match(lines[line_no])
            if match:
                lines[line_no] = line_to_replace
                logging.debug("update_station_info - Number of station changed:", lines[line_no])

        for line_no in range(length):
            if "max_num_sta" in lines[line_no]:
                logging.debug(lines[line_no])
                check_pattern_and_replace(line_no, "max_num_sta", change_station_line)

        with FileLock(lavazza_cfds_utility_macros.HOTSPOT_CONF_FILE + ".lock"):
            with open(lavazza_cfds_utility_macros.HOTSPOT_CONF_FILE, "w") as f:
                f.writelines(lines)
    except:
        logging.exception("update_station_info - Number of stations update info error")


def update_device_gsm_info(msg_type, value):

    try:
        logging.debug("update_device_gsm_info: {}".format(value))

        gsm_info = {}
        if lavazza_cfds_utility_macros.read_from_file(gsm_info, \
                                                      lavazza_cfds_utility_macros.GSM_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("GSM_CONF_FILE read error")

        if value["APN_name"] is not None:
            gsm_info["APN_name"] = value["APN_name"]

        if value["gsm_status"] is not None:
            gsm_info["gsm_status"] = value["gsm_status"]

        if lavazza_cfds_utility_macros.write_to_file(gsm_info, \
                                                     lavazza_cfds_utility_macros.GSM_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("GSM_CONF_FILE write error")

        msg = [value["network_mode"]]
        if update_device_info(msg_type, msg) != lavazza_cfds_utility_macros.SUCCESS:
            raise Exception("GSM_INFO write error in device provision info")
        
        return lavazza_cfds_utility_macros.SUCCESS
    except:
        logging.exception("update_device_gsm_info")
        return None


def update_device_wifi_info(msg_type, value):
    try:

        wifi_info = {}

        logging.debug("update_device_wifi_info: {}".format(value))

        if lavazza_cfds_utility_macros.read_from_file(wifi_info, \
                                                      lavazza_cfds_utility_macros.WIFI_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("WIFI_INFO_FILE read error")

        if value["SSID"] is not None and value["PSK"] is not None:
            wifi_info["SSID"] = value["SSID"]
            wifi_info["PSK"] = value["PSK"]

            wifi_info["Previous_ssid"] = value["Previous_ssid"]
            wifi_info["Previous_psk"] = value["Previous_psk"]

        if value["wifi_status"] is not None:
            wifi_info["wifi_status"] = value["wifi_status"]

        if lavazza_cfds_utility_macros.write_to_file(wifi_info, \
                                                     lavazza_cfds_utility_macros.WIFI_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("WIFI_INFO_FILE write error")

        msg = [value["SSID"], value["PSK"], value["network_mode"]]
        if update_device_info(msg_type, msg) != lavazza_cfds_utility_macros.SUCCESS:
            raise Exception("WIFI_INFO write error in device provision info")

        return lavazza_cfds_utility_macros.SUCCESS

    except:
        logging.exception("update_device_wifi_info")
        return None


def update_device_provision_info(msg_type, key, value, event_to_peform):
    """Updates the product names or provision_status in device_provision_info """
    try:
        device_provision_info = {}

        if lavazza_cfds_utility_macros.read_from_file(device_provision_info, \
                                                      lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("DEVICE_PROVISION_INFO_FILE read error")

        device_provision_info[key] = value

        if lavazza_cfds_utility_macros.write_to_file(device_provision_info, \
                                                     lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("DEVICE_PROVISION_INFO_FILE write error")

        if msg_type == lavazza_cfds_utility_macros.PRODUCT_NAME_MESSAGE_TYPE_ID:
            logging.debug("product names saved")
            # response_data = {"msg_type": msg_type, "msg": "SUCCESS"}
            return lavazza_cfds_utility_macros.SUCCESS

        if msg_type == lavazza_cfds_utility_macros.INIT_PROVISION_MESSAGE_TYPE_ID:
            logging.debug("provision_message - reboot")
            device_power_off(event_to_peform)  # reboot
            return None

    except:
        logging.exception("update_device_provision_info ")
        return lavazza_cfds_utility_macros.FAILURE


def update_device_info(msg_type, msg):

    try:

        logging.debug("update_device_info - msg_type {}".format(msg_type))
        device_provision_info = {}

        if lavazza_cfds_utility_macros.read_from_file(device_provision_info, \
                                                      lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("update_device_info - DEVICE_PROVISION_INFO_FILE read error")

        if msg_type == lavazza_cfds_utility_macros.WIFI_INFO_MESSAGE_TYPE_ID:

            if msg[0]:
                device_provision_info["ssid"] = msg[0]

            if msg[1]:
                device_provision_info["password"] = msg[1]
            if msg[2]:
                device_provision_info["network_mode"] = msg[2]
                if msg[2] == lavazza_cfds_utility_macros.MACHINE_WIFI:
                    update_hotspot_info(msg[0])

        elif msg_type == lavazza_cfds_utility_macros.DEVICE_INFO_MESSAGE_TYPE_ID:

            if msg[0]:
                device_provision_info["device_name"] = msg[0]
            if msg[1]:
                device_provision_info["device_id"] = msg[1]
            if msg[2]:
                device_provision_info["device_type"] = msg[2]

        elif msg_type == lavazza_cfds_utility_macros.GSM_CONFIG_MESSAGE_TYPE_ID:
            if msg[0]:
                device_provision_info["network_mode"] = msg[0]

        elif msg_type == lavazza_cfds_utility_macros.UPDATE_NUMBER_OF_STATION_MESSAGE_TYPE_ID:

            if msg[0]:
                device_provision_info["num_of_stations"] = msg[0]
            else:
                device_provision_info["num_of_stations"] = "25"

        elif msg_type == lavazza_cfds_utility_macros.DEVICE_MODE_UPDATE_MESSAGE_TYPE_ID:
            if msg["device_mode"] == lavazza_cfds_utility_macros.INTERNET_MODE:
                if disable_hotspot() == lavazza_cfds_utility_macros.FAILURE:
                    raise Exception("update_device_mode - Failed to disable the hotspot")
                else:
                    logging.debug("update_device_mode - Successfully disabled")

            elif msg["device_mode"] == lavazza_cfds_utility_macros.INTRANET_MODE:
                if enable_hotspot() == lavazza_cfds_utility_macros.FAILURE:
                    raise Exception("update_device_mode - Failed to enable the hotspot")
                else:
                    logging.debug("update_device_mode - Successfully enabled")

            device_provision_info["device_mode"] = msg["device_mode"]

        else:
            raise Exception("update_device_mode - Something went wrong")
            
        if lavazza_cfds_utility_macros.write_to_file(device_provision_info, \
                                                     lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("update_device_info - DEVICE_PROVISION_INFO_FILE write error")

        return lavazza_cfds_utility_macros.SUCCESS

    except:
        logging.exception("update_device_info ")
        return lavazza_cfds_utility_macros.FAILURE


def remove_qrcode():

    try:
        
        remove_qrcode_cmd_output = {}

        QR_REMOVE_CMD = ' sudo rm -rf /home/pi/lavazza_cfds/tmp/qr_code.png'

        if lavazza_cfds_utility_macros.command_executor(remove_qrcode_cmd_output, QR_REMOVE_CMD) != lavazza_cfds_utility_macros.SUCCESS:
            logging.debug("remove_qrcode - SUCESS")

        else:
            logging.debug("remove_qrcode - FALIURE")

    except Exception as error:
        logging.exception("remove_qrcode : {}".format(error))


def update_provisioned_product_names(provisioned_product_names):

    try:

        CONFIGURED_PRODUCT_COUNT = 8
        TOTAL_PRODUCT_COUNT = 29

        provisioned_data = {}
        product_data = {}

        if lavazza_cfds_utility_macros.read_from_file(product_data,
                                                 lavazza_cfds_utility_macros.PRODUCT_NAME_CONFIG_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("PRODUCT_NAME_CONFIG_FILE read error")

        product_names = product_data['product_details']

        final_product_names = []

        for i in range(CONFIGURED_PRODUCT_COUNT):
            for j in range(TOTAL_PRODUCT_COUNT):

                if provisioned_product_names[i]["product_name"] == product_names[j]["product_name"]:

                    product_details = {"product_no": provisioned_product_names[i]["product_no"],
                                       'product_name': provisioned_product_names[i]["product_name"],
                                       'pair_order_flag': product_names[j]['pair_order_flag'],
                                       'pair_product_id': product_names[j]['pair_product_id'],
                                       'milk_based_product': product_names[j]['milk_based_product'],
                                       'other_params': product_names[j]['other_params']
                                       }

                    final_product_names.append(product_details)
                    product_details = None
                    break

        return final_product_names

    except Exception as Error:
        logging.exception("update_provisioned_product_names: %s", Error)


def get_device_id(msg_type, device_name):
    """Getting device_id for the machine from the cloud in the pre_provision stage"""
    device_provision_info = {}

    if lavazza_cfds_utility_macros.read_from_file(
            device_provision_info, lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:

        response_to_gui = {"status": "Failure", "code": 0,
                           "message": "Error while getting provision info"}
        return response_to_gui

    try:

        logging.info("get_device_id:device name is: {}".format(device_name))

        if device_provision_info["device_id"] is None:

            url_list = []
            if lavazza_cfds_utility_macros.add_to_url_list(
                    lavazza_cfds_utility_macros.CONFIGURATION_SERVER, url_list, "") == lavazza_cfds_utility_macros.FAILURE:
                response_to_gui = {"status": "Failure", "code": lavazza_cfds_utility_macros.FAILURE,
                                   "message": "Error while adding URL"}
                return response_to_gui

            url = url_list[0]
            headers = {"token": lavazza_cfds_utility_macros.TOKEN, "content-type": "application/json", "device_name": device_name}
            logging.debug(url, headers)

            get_id_response = requests.get(url=url + "/getDeviceId", headers=headers)
            logging.debug("get_id_response :\n")
            logging.debug(get_id_response.status_code)

            if get_id_response.status_code == lavazza_cfds_utility_macros.HTTP_SUCCESS_STATUS_CODE:
                get_id_response_body = get_id_response.json()
                logging.debug("get_id_response_body :\n")
                logging.debug(get_id_response_body)

                if get_id_response_body["code"] == lavazza_cfds_utility_macros.SUCCESS:
                    headers.update({"device_id": get_id_response_body["deviceId"]})
                    ack_response = requests.post(url=url + "/deviceIdAck", headers=headers)
                    logging.debug("ack_response :\n")
                    logging.debug(ack_response.status_code)

                    if ack_response.status_code == lavazza_cfds_utility_macros.HTTP_SUCCESS_STATUS_CODE:
                        ack_response_body = ack_response.json()
                        logging.debug("ack_response_body :\n")
                        logging.debug(ack_response_body)

                        if ack_response_body["code"] == lavazza_cfds_utility_macros.SUCCESS:

                            # Update device provision info json file
                            try:
                                device_provision_info["device_id"] = get_id_response_body["deviceId"]
                                device_provision_info["device_name"] = device_name
                                device_provision_info["device_type"] = get_id_response_body["deviceType"]
                                device_provision_info["pubsub_subscriptions"] = get_id_response_body[
                                    "pubsubSubscriptions"]

                                device_provision_info["product_names"] = get_id_response_body[
                                    "productNames"]

                                device_provision_info["provisioned_product_details"] = update_provisioned_product_names(device_provision_info["product_names"])

                                logging.debug(device_provision_info)

                                if lavazza_cfds_utility_macros.write_to_file(
                                        device_provision_info, lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:
                                    raise Exception("DEVICE_PROVISION_INFO_FILE write error")
                                response_to_gui = ack_response_body

                            except Exception as Error:
                                logging.exception("get_device_id : %s",Error)
                                response_to_gui = {"status": "Failure", "code": lavazza_cfds_utility_macros.FAILURE,
                                                   "message": "Error while saving device id"}
                        else:
                            response_to_gui = ack_response_body
                    else:
                        response_to_gui = {"status": "Failure", "code": lavazza_cfds_utility_macros.FAILURE,
                                           "message": "Something went wrong(Bad Response/Request)....Try again"}
                else:
                    response_to_gui = get_id_response_body
            else:
                response_to_gui = {"status": "Failure", "code": lavazza_cfds_utility_macros.FAILURE,
                                   "message": "Something went wrong(Bad Response/Request ack)"}
        else:
            response_to_gui = {"status": "Failure", "code": lavazza_cfds_utility_macros.FAILURE,
                               "message": "Device has been already registered in the server or "
                                          "reset the device for new registration"}

    except Exception as Error:
        logging.exception("get_device_id: {}".format(Error))
        response_to_gui = {"status": "Failure", "code": lavazza_cfds_utility_macros.FAILURE,
                           "message": "Something went wrong(Connection/connection parameter Issues)"}

    return response_to_gui
