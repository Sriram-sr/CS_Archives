"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_mobile_app_server.py
 * Version        : 1.1
 * Date           : APRIL 20 2021
 *
 * Copyright (C) mieuPro Systems, 2021
 *
 ******************************************************************************
 """
import logging
import threading
import time

from flask import Flask, request, jsonify, Blueprint
from lavazza_cfds_mobile_app_server_macros import *
import lavazza_cfds_mobile_app_server_macros

# Registering the technician app server url paths to be a part of mobile app server
tech_app = Blueprint('tech_app', __name__)

# Declaring a lock
lock = threading.Lock()

# Product and Device provision info
product_details = None
device_provision_info = None
device_type_info = None
all_products = []
internet_mode = False

# Mobile app server system resources passed from the mobile app server to access events and locks
mobile_app_server_system_resources = None

# configuration_status holds the configuration state of the three important configurations,
# Wi-fi configuration, Device configuration and Products configuration
# Initially all the states are marked as FALSE
# When a technician configures all the necessary parameters using the technician app, all three states
# will be changed to TRUE
# A Provision updater thread will be running to look for this change, so when all three states changed to TRUE,
# the thread will change the device provision status to TRUE by calling the UTILITY function
configuration_status = {"wifi_info": False, "device_info": False, "product_info": False}

init_configuration_status = {"wifi_info": False, "device_info": False, "product_info": False}
init_configuration_data = {}

# LOG_LEVEL & LAVAZZA_COMMON_LOG_FILE are declared in lavazza_prontobar_common_macros
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - Mobile_App_Backend - %(levelname)s - %(message)s',
                    filename=LAVAZZA_COMMON_LOG_FILE, filemode='a')


# TechApp API endpoint to return the configured device info
@tech_app.route('/techapp/deviceInfo', methods=['GET'])
def configured_device_info_handler():
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            configuredDeviceInfo = {}
            try:
                logging.info("Acquiring lock to access device_provision_info")
                lock.acquire()
                configuredDeviceInfo["deviceName"] = device_provision_info["device_name"]
                configuredDeviceInfo["deviceId"] = device_provision_info["device_id"]
                configuredDeviceInfo["deviceType"] = device_provision_info["device_type"]
                configuredDeviceInfo["allDeviceTypes"] = device_type_info
            finally:
                lock.release()
                logging.info("Released the lock acquired to access device_provision_info")

            logging.info("----Device information sent successfully----")
            return jsonify(status="Success", data=configuredDeviceInfo,
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Device Info Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to return the configured product info
@tech_app.route('/techapp/productInfo', methods=['GET'])
def configured_product_info_handler():
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            product = "Product"
            configuredProductInfo = {}
            product_num = 1

            try:
                logging.info("Acquiring lock to access device_provision_info")
                lock.acquire()
                # Sending the products configured in the device to the technician app
                # If nothing is configured, NULL will be sent
                if device_provision_info["provision_status"] == True:
                    for provisioned_product_info in device_provision_info["provisioned_product_details"]:
                        product_id = product + str(product_num)
                        configuredProductInfo[product_id] = provisioned_product_info["product_name"]
                        product_num += 1
                else:
                    if PRONTO_BAR_TYPE in device_type_info:
                        max_product = 9
                    else:
                        max_product = 8

                    for i in range(0, max_product):
                        product_id = product + str(product_num)
                        configuredProductInfo[product_id] = None
                        product_num += 1
            finally:
                lock.release()
                logging.info("Released the lock acquired to access device_provision_info")

            logging.info("----Product information sent successfully----")
            return jsonify(status="Success", data=configuredProductInfo,
                           allProducts=all_products,
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Product Info Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401

# TechApp API endpoint to return the list of available wifi
@tech_app.route('/techapp/getWifiDevices', methods=['GET'])
def get_available_wifi_devices_handler():
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lvz_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            availableWifiDevicesInfo={}
            data = {}
            try:
                logging.info("Acquiring lock to access available_wifi_devices")
                lock.acquire()
                read_from_file(data,lavazza_cfds_mobile_app_server_macros.AVAILABLE_WIFI)
                availableWifiDevicesInfo["availableWifiDevices"] = data["available_wifi"]
            finally:
                lock.release()
                logging.info("Released the lock acquired to access available_wifi_devices")

            logging.info("----Device information sent successfully----")
            return jsonify(status="Success", data=availableWifiDevicesInfo,
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Device Info Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to return the configured wifi info
@tech_app.route('/techapp/wifiInfo', methods=['GET'])
def configured_wifi_info_handler():
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            configuredWifiInfo = {}

            try:
                logging.info("Acquiring lock to access device_provision_info")
                lock.acquire()
                # Sending the configured SSID name to the technician app
                # Or else default SSID name will be sent
                configuredWifiInfo["wifi_mode"] = device_provision_info["network_mode"]
                configuredWifiInfo["ssid"] = device_provision_info["ssid"]
                configuredWifiInfo["mac_address"] = getMAC('wlan0')
                if device_provision_info["network_mode"] == MACHINE_WIFI:
                    configuredWifiInfo["password"] = None
                else:
                    configuredWifiInfo["password"] = device_provision_info["password"]
            finally:
                lock.release()
                logging.info("Released the lock acquired to access device_provision_info")

            logging.info("----Wifi information sent successfully----")
            return jsonify(status="Success", data=configuredWifiInfo,
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Wi-fi Info Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to reboot the device
@tech_app.route('/techapp/reboot', methods=['GET'])
def device_reboot_handler():
    global init_configuration_status

    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":

            # REBOOT_MESSAGE_TYPE_ID is declared in lavazza_prontobar_common_macros
            reboot_data = {"msg_type": REBOOT_MESSAGE_TYPE_ID, "msg": "reboot"}

            # Initiating a thread to communicate with the UTILITY functionality to reboot the device
            # To avoid the delay to send response to the request,  mobile_app_server_to_utility_commn
            # function is spawned as a thread
            if device_provision_info["provision_status"] == False:

                if False not in init_configuration_status.values():
                    logging.info("All Init configuration parameter changed as True")
                    logging.info("Init Provision configuration sent to utility")
                    init_conf_handler_t = threading.Thread(target=init_configuration_handler, args=())
                    init_conf_handler_t.start()
                else:
                    logging.info("Reboot failed because device is not provisioned")
                    return jsonify(status="Failure", infoText="config error",
                                   provisionStatus=device_provision_info["provision_status"]), 401
            else:
                logging.info("Reboot message sent to utility")
                reboot_t = threading.Thread(target=mobile_app_server_to_utility_commn,
                                            args=(reboot_data, None, False))
                reboot_t.start()

            logging.info("----Reboot information sent successfully----")
            return jsonify(status="Success", infoText="Device will be rebooted shortly",
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Reboot Info Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to reset the device
@tech_app.route('/techapp/reset', methods=['GET'])
def device_reset_handler():
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":

            # REBOOT_MESSAGE_TYPE_ID is declared in lavazza_prontobar_common_macros
            reset_data = {"msg_type": APPLICATION_RESET_MESSAGE_TYPE_ID, "msg": "reset"}

            # Initiating a thread to communicate with the UTILITY functionality to reboot the device
            # To avoid the delay to send response to the request,  mobile_app_server_to_utility_commn
            # function is spawned as a thread
            if device_provision_info["provision_status"] == False:
                logging.info("Reset failed because device is not provisioned")
                return jsonify(status="Failure", infoText="config error",
                               provisionStatus=device_provision_info["provision_status"]), 401
            else:
                logging.info("Reset message sent to utility")
                reset_t = threading.Thread(target=mobile_app_server_to_utility_commn,
                                           args=(reset_data, None, False))
                reset_t.start()

            logging.info("----Reset information sent successfully----")
            return jsonify(status="Success", infoText="Device is getting reset",
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Reset Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to configure the device info
@tech_app.route('/techapp/configureDeviceInfo', methods=['POST'])
def device_configuration_handler():
    global init_configuration_data, init_configuration_status
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            device_configuration = request.get_json()

            configured_device_info = [None, None, None]

            # Formatting the data received from the technician app as expected by the UTILITY functionality
            configured_device_info[0] = device_configuration["data"]["deviceName"]
            configured_device_info[1] = device_configuration["data"]["deviceId"]
            configured_device_info[2] = device_configuration["data"]["deviceType"]

            # DEVICE_INFO_MESSAGE_TYPE_ID is declared in lavazza_prontobar_common_macros
            device_configuration_data = {"msg_type": DEVICE_INFO_MESSAGE_TYPE_ID, "msg": configured_device_info}

            # Initiating a thread to communicate with the UTILITY functionality to configure the device info
            # as per the configuration received from tech app
            # To avoid the delay to send response to the request,  mobile_app_server_to_utility_commn
            # function is spawned as a thread
            if device_provision_info["provision_status"] == False:
                logging.info("Device configuration saved to init_configuration_data")
                device_conf_data = [device_configuration_data, "device_info", True]
                init_configuration_data["device_info"] = device_conf_data
                init_configuration_status["device_info"] = True
            else:
                logging.info("Device configuration sent to utility")
                device_configuration_t = threading.Thread(target=mobile_app_server_to_utility_commn,
                                                          args=(device_configuration_data, "device_info", True))
                device_configuration_t.start()

            logging.info("----Device configuration saved successfully----")
            return jsonify(status="Success", infoText="Device info configured successfully",
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Device Info Configuration Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to configure the product info
@tech_app.route('/techapp/configureProductInfo', methods=['POST'])
def product_configuration_handler():
    global init_configuration_data, init_configuration_status
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            product_configuration = request.get_json()

            logging.info("Configured Product Info: {}".format(product_configuration))

            configured_product_info = []
            product = "Product"

            try:
                logging.info("Acquiring lock to access product_details")
                lock.acquire()
                for product_num in range(1, len(product_configuration["data"].keys()) + 1):
                    product_key = product + str(product_num)
                    logging.info("Product Key: {}".format(product_key))

                    # Checking if the product names received from tech app is same as the available products name
                    product_info = next((product_info for product_info in
                                         product_details["product_details"] if
                                         product_info["product_name"] == product_configuration["data"][product_key]),
                                        None)

                    product_info["product_no"] = int(product_num)
                    logging.info("Product : {}".format(product_info))
                    configured_product_info.append(product_info)
            finally:
                lock.release()
                logging.info("Released the lock acquired to access product_details")

            # PRODUCT_NAME_MESSAGE_TYPE_ID is declared in lavazza_prontobar_common_macros
            product_configuration_data = {"msg_type": PRODUCT_NAME_MESSAGE_TYPE_ID, "msg": configured_product_info}

            # Initiating a thread to communicate with the UTILITY functionality to configure the product info
            # as per the configuration received from tech app
            # To avoid the delay to send response to the request,  mobile_app_server_to_utility_commn
            # function is spawned as a thread

            if device_provision_info["provision_status"] == False:
                logging.info("Product configuration saved to init_configuration_data")
                product_conf_data = [product_configuration_data, "product_info", True]
                init_configuration_data["product_info"] = product_conf_data
                init_configuration_status["product_info"] = True
            else:
                logging.info("Product configuration sent to utility")
                product_configuration_t = threading.Thread(target=mobile_app_server_to_utility_commn,
                                                           args=(product_configuration_data, "product_info", True))
                product_configuration_t.start()

            logging.info("----Product configuration saved successfully----")
            return jsonify(status="Success", infoText="Products info configured successfully",
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Product Info Configuration Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to configure the wifi ssid
@tech_app.route('/techapp/configureWifiInfo', methods=['POST'])
def wifi_configuration_handler():
    global init_configuration_data, init_configuration_status
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            wifi_configuration = request.get_json()

            configured_device_info = [None, None, None, None, None, None]

            configured_device_info[0] = wifi_configuration["data"]["ssid"]

            # DEVICE_INFO_MESSAGE_TYPE_ID is declared in lavazza_prontobar_common_macros
            wifi_configuration_data = {"msg_type": DEVICE_INFO_MESSAGE_TYPE_ID, "msg": configured_device_info}

            # Initiating a thread to communicate with the UTILITY functionality to configure the wifi info
            # as per the configuration received from tech app
            # To avoid the delay to send response to the request,  mobile_app_server_to_utility_commn
            # function is spawned as a thread
            if device_provision_info["provision_status"] == False:
                logging.info("Wifi configuration saved to init_configuration_data")
                wifi_conf_data = [wifi_configuration_data, "wifi_info", True]
                init_configuration_data["wifi_info"] = wifi_conf_data
                init_configuration_status["wifi_info"] = True
            else:
                logging.info("Wifi configuration sent to utility")
                wifi_configuration_t = threading.Thread(target=mobile_app_server_to_utility_commn,
                                                        args=(wifi_configuration_data, "wifi_info", True))
                wifi_configuration_t.start()

            logging.info("----Wifi configuration saved successfully----")
            return jsonify(status="Success", infoText="Wifi info configured successfully",
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Wi-fi Configuration Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to configure the wifi info for AMZN Models
@tech_app.route('/techapp/configureWifiInfoVer2', methods=['POST'])
def wifi_configuration_handler_ver2():
    global init_configuration_data, init_configuration_status
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            wifi_configuration = request.get_json()

            """
            wifi_mode_info = {"wifi_mode": wifi_configuration["data"]["wifi_mode"]}

            # WIFI_MODE_UPDATE_MESSAGE_TYPE_ID is declared in lavazza_prontobar_common_macros
            wifi_mode_data = {"msg_type": WIFI_INFO_MESSAGE_TYPE_ID, "msg": wifi_mode_info}
            """

            if wifi_configuration["data"]["wifi_mode"] == MACHINE_WIFI:
                #wifi_info = {"SSID": wifi_configuration["data"]["ssid"], "PSK": None, "Previous_ssid": None,
                #             "Previous_psk": None, "MAC": None, "ip_address": None}
                wifi_info = {"SSID": wifi_configuration["data"]["ssid"], "PSK": None,"Previous_ssid": None,
                             "Previous_psk": None, "network_mode": wifi_configuration["data"]["wifi_mode"], "wifi_status": None}
            else:
                #wifi_info = {"SSID": wifi_configuration["data"]["ssid"], "PSK": wifi_configuration["data"]["password"],
                #             "Previous_ssid": None, "Previous_psk": None, "MAC": None, "ip_address": None}
                wifi_info = {"SSID": wifi_configuration["data"]["ssid"], "PSK": wifi_configuration["data"]["password"],
                             "Previous_ssid": None, "Previous_psk": None, "network_mode": wifi_configuration["data"]["wifi_mode"],
                             "wifi_status": None}

            # WIFI_INFO_MESSAGE_TYPE_ID is declared in lavazza_prontobar_common_macros
            wifi_configuration_data = {"msg_type": WIFI_INFO_MESSAGE_TYPE_ID, "msg": wifi_info}

            # Initiating a thread to communicate with the UTILITY functionality to configure the wifi info
            # as per the configuration received from tech app
            # To avoid the delay to send response to the request,  mobile_app_server_to_utility_commn
            # function is spawned as a thread
            if device_provision_info["provision_status"] == False:
                logging.info("Wifi configuration saved to init_configuration_data")

                #wifi_mode_conf_data = [wifi_mode_data, None, True]
                #init_configuration_data["wifi_mode_info"] = wifi_mode_conf_data

                wifi_conf_data = [wifi_configuration_data, "wifi_info", True]
                init_configuration_data["wifi_info"] = wifi_conf_data
                init_configuration_status["wifi_info"] = True
            else:
                #logging.info("Wifi mode configuration sent to utility")
                #wifi_mode_configuration_t = threading.Thread(target=mobile_app_server_to_utility_commn,
                #                                             args=(wifi_mode_data, None, True))
                #wifi_mode_configuration_t.start()
                #time.sleep(1)

                logging.info("Wifi configuration sent to utility")
                wifi_configuration_t = threading.Thread(target=mobile_app_server_to_utility_commn,
                                                        args=(wifi_configuration_data, "wifi_info", True))
                wifi_configuration_t.start()

            logging.info("----Wifi configuration saved successfully----")
            return jsonify(status="Success", infoText="Wifi info configured successfully",
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Wi-fi Configuration Version 2 Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to configure the device info
@tech_app.route('/techapp/configureInternetDeviceInfo', methods=['POST'])
def internet_mode_device_configuration_handler():
    global init_configuration_data, init_configuration_status, configuration_status, internet_mode
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            device_configuration = request.get_json()

            configured_device_info = [None, None, None]

            # Formatting the data received from the technician app as expected by the UTILITY functionality
            configured_device_info[0] = device_configuration["data"]["deviceName"]
            configured_device_info[2] = device_configuration["data"]["deviceType"]

            device_mode_configuration_data = {"msg_type": DEVICE_MODE_UPDATE_MESSAGE_TYPE_ID,
                                              "msg": {"device_mode": INTERNET_MODE}}
            device_configuration_data = {"msg_type": DEVICE_INFO_MESSAGE_TYPE_ID, "msg": configured_device_info}

            # Initiating a thread to communicate with the UTILITY functionality to configure the device info
            # as per the configuration received from tech app
            # To avoid the delay to send response to the request,  mobile_app_server_to_utility_commn
            # function is spawned as a thread
            if device_provision_info["provision_status"] == False:
                logging.info("Device configuration saved to init_configuration_data")
                device_conf_data = [device_configuration_data, "device_info", True]
                init_configuration_data["device_info"] = device_conf_data
                init_configuration_data["device_mode_info"] = [device_mode_configuration_data, None, True]
                init_configuration_status["device_info"] = True
                init_configuration_status["product_info"] = True
                configuration_status["product_info"] = True
            else:
                logging.info("Device configuration Failed, Device is not provisioned")
                return jsonify(status="Failure", infoText="Device info configuration Failed",
                               provisionStatus=device_provision_info["provision_status"]), 200

            internet_mode = True
            logging.info("----Device configuration saved successfully----")
            return jsonify(status="Success", infoText="Device info configured successfully",
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Device Info Configuration Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to configure the wifi ssid
@tech_app.route('/techapp/configureInternetConnInfo', methods=['POST'])
def internet_mode_conn_configuration_handler():
    global init_configuration_data, init_configuration_status
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            device_conn_configuration = request.get_json()
            device_conn_config_data = None

            if device_conn_configuration["data"]["apnName"] is None:
                device_conn_data = {"SSID": device_conn_configuration["data"]["ssid"],
                                    "PSK": device_conn_configuration["data"]["password"],
                                    "Previous_ssid": None, "Previous_psk": None,
                                    "network_mode": ORGANIZATION_WIFI, "wifi_status": None}

                device_conn_config_data = {"msg_type": WIFI_INFO_MESSAGE_TYPE_ID, "msg": device_conn_data}

            elif device_conn_configuration["data"]["apnName"] is not None:
                device_conn_data = {"APN_name": device_conn_configuration["data"]["apnName"],
                                    "network_mode": GSM, "gsm_status": None}

                device_conn_config_data = {"msg_type": GSM_CONFIG_MESSAGE_TYPE_ID, "msg": device_conn_data}

            # Initiating a thread to communicate with the UTILITY functionality to configure the wifi info
            # as per the configuration received from tech app
            # To avoid the delay to send response to the request,  mobile_app_server_to_utility_commn
            # function is spawned as a thread
            if device_provision_info["provision_status"] == False:
                logging.info("Wifi configuration saved to init_configuration_data")
                init_configuration_data["wifi_info"] = [device_conn_config_data, "wifi_info", True]
                init_configuration_status["wifi_info"] = True
            else:
                logging.info("Device conn configuration Failed, Device is not provisioned")
                return jsonify(status="Failure", infoText="Device Conn info configuration Failed",
                               provisionStatus=device_provision_info["provision_status"]), 200

            logging.info("----Device conn configuration saved successfully----")
            return jsonify(status="Success", infoText="Conn info configured successfully",
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Connection Configuration Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to return the configured station info
@tech_app.route('/techapp/stationInfo', methods=['GET'])
def configured_station_info_handler():
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            configuredStationInfo = {}

            try:
                logging.info("Acquiring lock to access device_provision_info")
                lock.acquire()
                # Sending the configured station count to the technician app
                configuredStationInfo["station"] = device_provision_info["num_of_stations"]
            finally:
                lock.release()
                logging.info("Released the lock acquired to access device_provision_info")

            logging.info("----Station information sent successfully----")
            return jsonify(status="Success", data=configuredStationInfo,
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Station Info Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# TechApp API endpoint to configure the wifi stations
@tech_app.route('/techapp/configureStationInfo', methods=['POST'])
def station_configuration_handler():
    global init_configuration_data, init_configuration_status
    try:
        # Extracting the token id from the request header
        token_id = request.headers.get("tokenId")
        # Verifying the token id
        # TOKEN is declared in lavazza_prontobar_mobile_app_server_macros
        if token_id == MOBILE_APP_TOKEN or token_id == "secret":
            station_configuration = request.get_json()

            num_of_sta = int(station_configuration["data"]["station"])
            if num_of_sta >= 5 and num_of_sta <= 35:

                configured_device_info = [None, None, None, None, None, None]

                configured_device_info[5] = station_configuration["data"]["station"]
            else:
                return jsonify(status="Failure", infoText="Invalid config"), 401

            # DEVICE_INFO_MESSAGE_TYPE_ID is declared in lavazza_prontobar_common_macros
            station_configuration_data = {"msg_type": DEVICE_INFO_MESSAGE_TYPE_ID, "msg": configured_device_info}

            # Initiating a thread to communicate with the UTILITY functionality to configure the wifi info
            # as per the configuration received from tech app
            # To avoid the delay to send response to the request,  mobile_app_server_to_utility_commn
            # function is spawned as a thread
            logging.info("Station configuration sent to utility")
            station_configuration_t = threading.Thread(target=mobile_app_server_to_utility_commn,
                                                       args=(station_configuration_data, None, True))
            station_configuration_t.start()

            logging.info("----Station configuration saved successfully----")
            return jsonify(status="Success", infoText="Station info configured successfully",
                           provisionStatus=device_provision_info["provision_status"]), 200
        else:
            return jsonify(status="Failure", infoText="Invalid token"), 401

    except Exception as error:
        logging.info("Tech App Station Configuration Error : {}".format(error))
        return jsonify(status="Failure", infoText="Exception occurred"), 401


# Function to send the configuration data received from tech app to UTILITY to change the device configurations
def mobile_app_server_to_utility_commn(configuration_data, configuration_type, response_required):
    global configuration_status
    try:
        logging.info("Triggering utility to configure {}".format(configuration_type))
        logging.info("Before acquiring utility_event_lock")

        # Acquiring the "utility_event_lock" lock
        with posix_ipc.Semaphore("utility_event_lock"):

            logging.info("utility_event_lock Acquired")

            utility_event_data = {"thread_name": "mobile_app_backend",
                                  "event": mobile_app_server_system_resources["utility_event"],
                                  "queue": mobile_app_server_system_resources["/utility_queue"],
                                  "event_data": configuration_data,
                                  "finished_event": mobile_app_server_system_resources["utility_finished_event"],
                                  "response_required": response_required}

            # Common API(lavazza_prontobar_common_apis) functionality to send the configuration data to the UTILITY queue
            # and set the UTILITY event
            event_response = trigger_event_handler_framework(utility_event_data)

        logging.info("utility_event_lock Released")

        # If the configuration is successful, update the respective configuration_status
        # SUCCESS is declared in lavazza_prontobar_common_macros
        if event_response == SUCCESS:
            # NONE type is checked to avoid configurations other than device, product and wifi
            if configuration_type is not None:
                if device_provision_info["provision_status"] == False:
                    logging.info("Provision status is False")
                    try:
                        logging.info("Acquiring lock to access configuration_status")
                        lock.acquire()
                        configuration_status[configuration_type] = True
                        logging.info("{} configured as true".format(configuration_type))
                    finally:
                        lock.release()
                        logging.info("Released the lock acquired to access configuration_status")
        else:
            logging.info("Failed to configure {}".format(configuration_type))

        return

    except Exception as error:
        logging.info("Mobile App Server to utility communication Error, {}".format(error))
        return


# BG thread to update the Device Provision status
# This function will be spawned as a thread from the lavazza_prontobar_mobile_app_server,
# which will run until the device provision status turns to be TRUE
def update_provision_status():
    global configuration_status

    logging.info("Provision status updater thread initiated")
    while True:
        # Check if device provision status is FALSE
        # If not then the device is already provisioned, so the initiated thread will stop
        if device_provision_info["provision_status"] == False:
            time.sleep(0.5)
            # When configuration status for wifi, device and product info are changed as TRUE,
            # server to utility communication is initiated to change provision status as TRUE
            try:
                lock.acquire()
                # logging.info("Acquiring lock to access configuration_status")
                # Check if all the three configurations are TRUE
                if False not in configuration_status.values():
                    logging.info("All configuration parameter changed as True")
                    logging.info("Provision configuration sent to utility")
                else:
                    continue
            finally:
                lock.release()
                # logging.info("Releasing the lock acquired to access configuration_status")

            if internet_mode == True:
                # Message format expected by UTILITY
                reboot_data = {"msg_type": REBOOT_MESSAGE_TYPE_ID, "msg": "reboot"}
                mobile_app_server_to_utility_commn(reboot_data, None, False)
            else:
                # Message format expected by UTILITY
                provision_data = {"msg_type": INIT_PROVISION_MESSAGE_TYPE_ID, "msg": "reboot"}
                mobile_app_server_to_utility_commn(provision_data, None, False)

            return
        else:
            logging.info("Device is already provisioned")
            return


def init_configuration_handler():
    global init_configuration_data, init_configuration_status

    logging.info("----Init Provision status updater initiated----")

    for key in init_configuration_data:
        conf_data = init_configuration_data[key]
        logging.info("Init Configuration data")
        logging.info(key)
        logging.info(conf_data)
        configuration_t = threading.Thread(target=mobile_app_server_to_utility_commn,
                                           args=(conf_data[0], conf_data[1], conf_data[2]))
        configuration_t.start()
        time.sleep(1)

    return


# Function to configure the resources, product and device configuration info received from the mobile app
# server in this tech app module
def configure_product_and_device_info(system_resource_param, product_detail_param, device_provision_info_param,
                                      device_type_info_param):
    global product_details, device_provision_info, device_type_info, mobile_app_server_system_resources, all_products

    mobile_app_server_system_resources = system_resource_param
    product_details = product_detail_param
    device_provision_info = device_provision_info_param
    device_type_info = device_type_info_param

    for product_info in product_details["product_details"]:
        all_products.append(product_info["product_name"])

    return
