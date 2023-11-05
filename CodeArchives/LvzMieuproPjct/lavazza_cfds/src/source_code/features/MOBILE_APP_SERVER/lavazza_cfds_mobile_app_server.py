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
import sys
import json
import logging
import uuid
import time
from threading import Thread, Lock

from flask import Flask, request, jsonify, Response, send_file, render_template
from flask_cors import CORS

from lavazza_cfds_mobile_app_server_macros import *

sys.path.append(APP_SERVER)

import lavazza_cfds_dispense_queue_handler
import lavazza_cfds_mobile_app_tech_server
import lavazza_cfds_src_update_server

import lavazza_cfds_pubsub_dispense_queue_handler

sys.path.append(MB_IO_HANDLER_FILE_PATH)
from lavazza_cfds_mb_io_handler_macros import *

# Declaring a lock
lock = Lock()

# Mobile App Server Systems Resources
mobile_app_server_system_resources = {}

# Product and Device provision info
product_details = {}
device_provision_info = {}
device_type_info = {}
mobile_app_product_info = []
enable_pwa = None

# Order number
order_number = MIN_ORDER_NUM
order_number_handler = lambda order_no: order_no + 1 if order_no < MAX_ORDER_NUM else MIN_ORDER_NUM + 1

logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - Mobile_App_Backend - %(levelname)s - %(message)s',
                    filename=LAVAZZA_COMMON_LOG_FILE, filemode='a')

app = Flask(__name__)
app.register_blueprint(lavazza_cfds_mobile_app_tech_server.tech_app)
app.register_blueprint(lavazza_cfds_src_update_server.src_update)
CORS(app)


@app.route('/pwa_status', methods=['GET'])
def pwa_status():
    try:
        token_id = request.headers.get("tokenId")

        if token_id == MOBILE_APP_TOKEN:
            return jsonify(status=SUCCESS, data=enable_pwa), 200
        else:
            return jsonify(status=FAILURE), 401

    except Exception as error:
        logging.info("Pwa Status error : {}".format(error))
        return Response(status=401)


@app.route('/pwa_config', methods=['GET'])
def pwa_config():
    pwa_config = request.args.get("config")
    token = request.args.get("token")

    if token == PWA_TOKEN:
        if pwa_config == "enable" or pwa_config == "disable":
            pwa_config_handler(pwa_config)
            return jsonify(status=SUCCESS), 200
        else:
            return jsonify(status=FAILURE), 401
    else:
        return jsonify(status=FAILURE), 401


@app.route('/', methods=['GET'])
def webapp():
    if enable_pwa == True:
        if device_provision_info["network_mode"] == MACHINE_WIFI:
            return render_template("webapp_wo_fb.html", ip="192.168.5.1:9876", wifi_mode="CORP")
        elif device_provision_info["network_mode"] == ORGANIZATION_WIFI:
            wifi_config = {}
            if read_from_file(wifi_config, WIFI_CONF_FILE) == FAILURE:
                logging.exception("WIFI_CONFIG_FILE read error")
                return "<h1>Something went wrong <br> Error : may be config file read error !!</h1>"
            return render_template("webapp_wo_fb.html", ip=wifi_config["ip_address"] + ":9876", wifi_mode="CORP")
        else:
            return "<h1> Invalid wifi mode configured !!</h1>"
    else:
        return "<h1>File not Found !!</h1>"


@app.route('/img')
def image():
    try:
        img_name = request.args.get("image")
        path = APP_SERVER + "static/webapp_images/" + img_name
        # For debugging purpose
        # logging.info("Image Path : {}".format(path))
        return send_file(open(path, 'rb'), mimetype='image/gif')

    except Exception as error:
        logging.exception("Image error : {}".format(error))
        return Response(status=401)


@app.route('/productInfo', methods=['GET'])
def product_info_handler():
    global mobile_app_product_info, device_provision_info
    try:
        logging.info("MObile App Product Info : {}".format(mobile_app_product_info))
        token_id = request.headers.get("tokenId")
        logging.info("Token ID : {}".format(token_id))
        # logging.info("Device Info : {}".format(device_provision_info))
        logging.info("TOKEN Info : {}".format(MOBILE_APP_TOKEN))

        if token_id == MOBILE_APP_TOKEN:
            logging.info("Token is verified")
            if device_provision_info["provision_status"] == True:
                logging.info("Product and device details sent successfully")
                return jsonify(data=mobile_app_product_info,
                               machineName=device_provision_info["device_name"],
                               machineId=device_provision_info["device_id"],
                               ssid=device_provision_info["ssid"],
                               status=SUCCESS), 200
            else:
                return jsonify(status=FAILURE, orderStatus=MACHINE_NOT_READY), 200
        else:
            return jsonify(status=FAILURE, orderStatus=INVALID_TOKEN), 401

    except Exception as error:
        logging.exception("Product Info Error : {}".format(error))
        return jsonify(status=FAILURE, orderStatus=EXCEPTION_OCCURRED), 401


@app.route('/order', methods=['GET'])
def dispense_order_handler():
    global order_number
    try:
        token_id = request.headers.get("tokenId")
        machine_name = request.headers.get("machineName")
        machine_id = request.headers.get("machineId")

        if token_id == MOBILE_APP_TOKEN:
            if device_provision_info["provision_status"] == True:
                if device_provision_info["device_type"] != PANTRY_TYPE:
                    logging.info("Checking if the GUI is in Product dispense window")
                    if not mobile_app_server_system_resources["gui_product_dispense_event"].isSet():
                        logging.info("Order cancelled as the GUI is not in Product dispense window")
                        return jsonify(status=FAILURE, orderStatus=MACHINE_NOT_READY), 200

                if machine_name == device_provision_info["device_name"] and machine_id == device_provision_info[
                    "device_id"]:
                    orders = []
                    product_id_list = []

                    product_id_list.append(request.args.get("productId"))
                    pair_order_flag = request.args.get("pairOrderFlag")

                    try:
                        logging.info("Acquiring the lock to get the order number")
                        lock.acquire()
                        order_number = order_number_handler(order_number)
                    finally:
                        lock.release()
                        logging.info("Released the lock acquired to get the order number")

                    order_id = str(uuid.uuid4())
                    is_pair_order = False

                    logging.info("Order Received - {} {}".format(product_id_list[0], pair_order_flag))
                    logging.info("OrderId - {}, OrderNo - {}".format(order_id, order_number))

                    for product_id in product_id_list:
                        for product in mobile_app_product_info:
                            if product["productId"] == int(product_id):
                                order_info = {}
                                order_info.__setitem__("orderNo", order_number)
                                order_info.__setitem__("productNo", product["productNo"])
                                order_info.__setitem__("productName", product["productName"])
                                order_info.__setitem__("isPairOrder", is_pair_order)
                                order_info.__setitem__("orderId", order_id)
                                #order_info.__setitem__("approxDispenseTime", product["approxDispenseTime"])
                                if pair_order_flag == "true":
                                    if product["pairOrderFlag"] == True:
                                        order_info.__setitem__("pairOrderFlag", True)
                                        product_id_list.append(product["pairProductId"])
                                        is_pair_order = True
                                        pair_order_flag = "false"
                                    else:
                                        order_info.__setitem__("pairOrderFlag", False)
                                else:
                                    order_info.__setitem__("pairOrderFlag", False)
                                orders.append(order_info)
                                break

                    logging.info(orders)

                    if len(orders) > 0:
                        approx_wait_time = lavazza_cfds_dispense_queue_handler.append_dispense_queue(orders)
                        logging.info("Order added to the dispense queue")

                        if mobile_app_server_system_resources["dispense_queue_handler_event"].isSet() is False:
                            mobile_app_server_system_resources["dispense_queue_handler_event"].set()
                            logging.info("Dispense queue handler event is set after an order is received")

                        if lavazza_cfds_dispense_queue_handler.current_order_status["orderId"] == None:
                            current_order_num = order_number
                        else:
                            current_order_num = lavazza_cfds_dispense_queue_handler.current_order_status["orderNo"]

                        logging.info("Order received response sent successfully")
                        logging.info("OrderId - {}, OrderNo - {}".format(order_id, order_number))

                        return jsonify(status=SUCCESS, orderStatus=ORDER_RECEIVED_OR_INQUEUE,
                                       orderId=order_id, orderNo=order_number,
                                       approxWaitTime=approx_wait_time,
                                       currentOrder=current_order_num), 200
                    else:
                        return jsonify(status=FAILURE, orderStatus=MACHINE_DETAIL_MISMATCH), 200
                else:
                    return jsonify(status=FAILURE, orderStatus=MACHINE_DETAIL_MISMATCH), 200
            else:
                return jsonify(status=FAILURE, orderStatus=MACHINE_NOT_READY), 200
        else:
            return jsonify(status=FAILURE, orderStatus=INVALID_TOKEN), 401

    except Exception as error:
        logging.info("Order Error : {}".format(error))
        return jsonify(status=FAILURE, orderStatus=EXCEPTION_OCCURRED), 401


@app.route('/orderStatus', methods=['GET'])
def order_status_handler():
    try:
        token_id = request.headers.get("tokenId")
        machine_name = request.headers.get("machineName")
        machine_id = request.headers.get("machineId")

        if token_id == MOBILE_APP_TOKEN:
            if device_provision_info["provision_status"] == True:
                if machine_name == device_provision_info["device_name"] and machine_id == device_provision_info[
                    "device_id"]:
                    order_id = request.args.get("orderId")
                    cancelled_order_info = next((cancelled_order_info for cancelled_order_info in
                                                 lavazza_cfds_dispense_queue_handler.cancelled_orders if
                                                 cancelled_order_info["orderId"] == order_id), None)

                    if order_id == lavazza_cfds_dispense_queue_handler.current_order_status["orderId"]:
                        return jsonify(status=SUCCESS,
                                       orderStatus=lavazza_cfds_dispense_queue_handler.current_order_status[
                                           "state"]), 200

                    elif next((dispensed_order_info for dispensed_order_info in
                               lavazza_cfds_dispense_queue_handler.dispensed_orders if
                               dispensed_order_info["orderId"] == order_id), None):
                        return jsonify(status=SUCCESS, orderStatus=DISPENSED), 200

                    elif cancelled_order_info is not None:
                        return jsonify(status=FAILURE, orderStatus=cancelled_order_info["status"]), 200

                    else:
                        return jsonify(status=SUCCESS, orderStatus=ORDER_RECEIVED_OR_INQUEUE,
                                       currentOrder=lavazza_cfds_dispense_queue_handler.current_order_status["orderNo"]
                                       ), 200
                else:
                    return jsonify(status=FAILURE, orderStatus=MACHINE_DETAIL_MISMATCH), 200
            else:
                return jsonify(status=FAILURE, orderStatus=MACHINE_NOT_READY), 200
        else:
            return jsonify(status=FAILURE, orderStatus=INVALID_TOKEN), 401

    except Exception as error:
        logging.info("Order Status Error : {}".format(error))
        return jsonify(status=FAILURE, orderStatus=EXCEPTION_OCCURRED), 401


@app.route('/dispense', methods=['GET'])
def order_dispense_handler():
    try:
        token_id = request.headers.get("tokenId")
        machine_name = request.headers.get("machineName")
        machine_id = request.headers.get("machineId")

        if token_id == MOBILE_APP_TOKEN:
            if device_provision_info["provision_status"] == True:
                if machine_name == device_provision_info["device_name"] and machine_id == device_provision_info[
                    "device_id"]:
                    order_id = request.args.get("orderId")

                    if order_id == lavazza_cfds_dispense_queue_handler.current_order_status["orderId"]:
                        mobile_app_server_system_resources["dispense_permission_event"].set()
                        time.sleep(1)
                        return jsonify(status=SUCCESS, orderStatus=DISPENSING), 200
                    else:
                        return jsonify(status=FAILURE, orderStatus=FAILURE), 200
                else:
                    return jsonify(status=FAILURE, orderStatus=MACHINE_DETAIL_MISMATCH), 200
            else:
                return jsonify(status=FAILURE, orderStatus=MACHINE_NOT_READY), 200
        else:
            return jsonify(status=FAILURE, orderStatus=INVALID_TOKEN), 401

    except Exception as error:
        logging.info("Dispense Error : {}".format(error))
        return jsonify(status=FAILURE, orderStatus=EXCEPTION_OCCURRED), 401


# PWA config handler
def pwa_config_handler(enable=False):
    global enable_pwa

    logging.info("Reading from pwa config file")
    with open(PWA_CONFIG_FILE) as file:
        pwa_config = json.load(file)

    if enable == False:
        enable_pwa = pwa_config["enable_pwa"]

    elif enable == "enable":
        logging.info("PWA feature is enabled")
        enable_pwa = True

        pwa_config["enable_pwa"] = True

        with open(PWA_CONFIG_FILE, 'w') as outfile:
            json.dump(pwa_config, outfile)

    elif enable == "disable":
        logging.info("PWA feature is disabled")
        enable_pwa = False

        pwa_config["enable_pwa"] = False

        with open(PWA_CONFIG_FILE, 'w') as outfile:
            json.dump(pwa_config, outfile)

    return


# Reading device provision configuration info (testing purpose)
def device_provision_info_handler():
    global device_provision_info, device_type_info
    try:
        if read_from_file(device_provision_info, DEVICE_PROVISION_INFO_FILE) == SUCCESS:
            logging.info("DEVICE_PROVISION_INFO_FILE read successfully")

        if read_from_file(device_type_info, DEV_TYPE_CONFIG_FILE) == SUCCESS:
            logging.info("DEV_TYPE_CONFIG_FILE read successfully")

        device_type_info = list(device_type_info.values())

        logging.info("Device Provision Info : ----------------")
        logging.info(device_provision_info)

        logging.info("Device Provision Info acquired successfully")

    except Exception as error:
        logging.info("Device provision info reading error : {}".format(error))

    return


# Reading product configuration info
def mobile_app_info_handler():
    global product_details, device_provision_info, mobile_app_product_info
    try:
        if read_from_file(product_details, PRODUCT_NAME_CONFIG_FILE) == SUCCESS:
            logging.info("PRODUCT_NAME_CONFIG_FILE read successfully")

    except Exception as error:
        logging.info("Product Details reading error : {}".format(error))

    device_provision_info_handler()

    if device_provision_info["provision_status"] == True:
        mobile_app_product_info = []

        try:
            lock.acquire()
            for provisioned_product_info in device_provision_info["provisioned_product_details"]:
                if provisioned_product_info["product_name"] != "NONE":
                    product_info = next((product_info for product_info in
                                         product_details["product_details"] if
                                         product_info["product_name"] == provisioned_product_info["product_name"]),
                                        None)

                    mobile_app_product = {}
                    mobile_app_product["productName"] = provisioned_product_info["product_name"]
                    mobile_app_product["productNo"] = int(provisioned_product_info["product_no"])
                    mobile_app_product["productId"] = product_info["product_id"]
                    mobile_app_product["pairOrderFlag"] = product_info["pair_order_flag"]
                    mobile_app_product["pairProductId"] = product_info["pair_product_id"]
                    #mobile_app_product["approxDispenseTime"] = product_info["other_params"]["approx_dispense_time"]
                    mobile_app_product_info.append(mobile_app_product)
        finally:
            lock.release()

        logging.info("Mobile app products info formed successfully")

    return


def mobile_app_order():
    try:

        global mobile_app_server_system_resources

        while True:
            # logging.info("mobile_app_order")
            input_data = {"thread_name": "mobile_app",
                          "event": mobile_app_server_system_resources["mobile_app_order_event"],
                          "queue": mobile_app_server_system_resources["/mobile_app_order_queue"],
                          "queue_handler_function": lavazza_cfds_pubsub_dispense_queue_handler.append_dispense_queue,
                          "finished_event": None}

            event_handler_framework(input_data)
            time.sleep(1)
        logging.info("waiting for mobile app server handler event")

    except Exception as error:
        logging.exception("error in mobile app server order event -{}".format(error))


def init_mobile_app_server():
    # Initializing mobile app backend resources
    global mobile_app_server_system_resources

    if update_process_id("MOBILE_APP_SERVER") == FAILURE:
        logging.error("MOBILE_APP_SERVER : updating process id")

    logging.info("Getting mobile app server system resources")

    initialize_service(mobile_app_server_system_resources, "lavazza_cfds_mobile_app_backend.service")

    logging.info("Resources : {}".format(mobile_app_server_system_resources))
    logging.info("Mobile app server system resources acquired successfully")

    # Initializing mobile app resources
    mobile_app_info_handler()

    # Reading pwa configuration
    pwa_config_handler()

    logging.info("Configuring tech app system resources")
    lavazza_cfds_mobile_app_tech_server.configure_product_and_device_info(mobile_app_server_system_resources,
                                                                          product_details, device_provision_info,
                                                                          device_type_info)

    # Initializing provision status updater
    logging.info("Provision status updater thread initiated")
    provision_status_update_t = Thread(target=lavazza_cfds_mobile_app_tech_server.update_provision_status, args=())
    provision_status_update_t.start()

    logging.info("Configuring dispense queue handler resources")
    lavazza_cfds_dispense_queue_handler.configure_system_resources(mobile_app_server_system_resources,
                                                                   device_provision_info)

    logging.info("Configuring pubsub dispense queue handler resources")
    lavazza_cfds_pubsub_dispense_queue_handler.configure_system_resources(mobile_app_server_system_resources,
                                                                          device_provision_info, mobile_app_product_info)

    if device_provision_info["provision_status"] == True:
        logging.info("Dispense queue handler thread initiated")
        # Initiating queue handler
        dispense_queue_handler_t = Thread(target=lavazza_cfds_dispense_queue_handler.dispense_queue_handler, args=())
        dispense_queue_handler_t.start()
    else:
        logging.info("Dispense queue handler thread is not initiated because provision_status is FALSE")

    if device_provision_info["provision_status"] == True:
        logging.info("Pubsub Dispense queue handler thread initiated")
        # Initiating Pubsub queue handler
        pubsub_dispense_queue_handler_t = Thread(
            target=lavazza_cfds_pubsub_dispense_queue_handler.dispense_queue_handler, args=())
        apporder__queue_handler_t = Thread(target=mobile_app_order, args=())

        pubsub_dispense_queue_handler_t.start()
        apporder__queue_handler_t.start()

    else:
        logging.info("Pubsub Dispense queue handler thread is not initiated because provision_status is FALSE")

    lavazza_cfds_src_update_server.read_update_config(device_provision_info)

    # Initiating mobile app server
    app.run(debug=False, host=HOST, port=PORT)


# Initializing mobile app server
init_mobile_app_server()
