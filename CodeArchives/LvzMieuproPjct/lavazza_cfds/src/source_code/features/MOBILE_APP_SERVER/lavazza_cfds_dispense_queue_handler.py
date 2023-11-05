"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_dispense_queue_handler.py
 * Version        : 1.1
 * Date           : APRIL 20 2021
 *
 * Copyright (C) mieuPro Systems, 2021
 *
 ******************************************************************************
 """

import json
import logging
import threading
import time
from collections import deque

from lavazza_cfds_mobile_app_server_macros import *

sys.path.append(MB_IO_HANDLER_FILE_PATH)

from lavazza_cfds_mb_io_handler_macros import *

logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - Mobile_App_Backend - %(levelname)s - %(message)s',
                    filename=LAVAZZA_COMMON_LOG_FILE, filemode='a')

# Initializing a queue
dispense_queue = deque()

# Declaring a lock
lock = threading.Lock()

# List maintaining current, dispensed and cancelled order status
current_order_status = {"orderId": None, "orderNo": None, "state": None}
current_order_info = None
dispensed_orders = []
cancelled_orders = []
dispensed_and_cancelled_orders_cleaner_flag = False
keypad_enable_state = True

mobile_app_server_system_resources = None
device_provision_info = None
input_key_handler_trigger_data = None


def append_dispense_queue(orders):
    global dispense_queue, order_num
    try:
        logging.info("Acquiring the lock to access the dispense queue")
        lock.acquire()
        for order_info in orders:
            dispense_queue.append(order_info)
            logging.info("Order No {} added to the dispense queue".format(order_info["orderNo"]))
        approx_wait_time = int(len(dispense_queue)) * int(MIN_PER_USER_WAIT_TIME)
    finally:
        lock.release()
        logging.info("Released the lock acquired to access the dispense queue")

    return approx_wait_time


def dispense_queue_handler():
    global dispensed_orders, cancelled_orders, dispense_permission_event, current_order_status, input_key_handler_trigger_data
    global mobile_app_server_system_resources, device_provision_info, current_order_info, keypad_enable_state

    input_key_handler_trigger_data = {"thread_name": "mobile_app_backend",
                                      "event": mobile_app_server_system_resources["mb_io_event"],
                                      "queue": mobile_app_server_system_resources["/mb_io_queue"],
                                      "event_data": None,
                                      "finished_event": mobile_app_server_system_resources["mb_io_finished_event"],
                                      "response_required": None}

    # logging.debug("Resources in dispense queue handler {}".format(mobile_app_server_system_resources))
    while True:
        if len(dispense_queue) < MIN_QUEUE_LENTH:
            logging.info("Queue is Empty")

            if device_provision_info["device_type"] == PANTRY_TYPE:
                if keypad_enable_state == False:
                    disable_display_data = {"msg_type": DISABLE_POP_UP_MESSAGE_TYPE_ID, "keypad_state": ENABLE}
                    logging.info("=========Enabling keypad state for pantry type==========")
                    pop_up_message_handler(disable_display_data)
                    keypad_enable_state = True

            if mobile_app_server_system_resources["dispense_queue_handler_event"].isSet() is True:
                mobile_app_server_system_resources["dispense_queue_handler_event"].clear()
                logging.info("Dispense queue handler event is cleared")

            if dispensed_and_cancelled_orders_cleaner_flag is not True:
                logging.info("Initiating cleaning functionality for dispensed and cancelled orders")
                dispensed_and_cancelled_orders_cleaner = threading.Thread(target=clean_dispensed_and_cancelled_orders,
                                                                          args=())
                dispensed_and_cancelled_orders_cleaner.start()

            logging.info("Waiting for dispense queue handler event")
            mobile_app_server_system_resources["dispense_queue_handler_event"].wait()
            logging.info("Dispense queue handler event received")
        else:
            if device_provision_info["device_type"] != PANTRY_TYPE:
                mobile_app_server_system_resources["/mb_io_event_lock"].acquire()
                logging.info("Motherboard IO event lock acquired")
            else:
                logging.info("Machine is PANTRY TYPE")

            if device_provision_info["device_type"] != PANTRY_TYPE:
                logging.info("Checking if the GUI is in Product dispense window")
                if not mobile_app_server_system_resources["gui_product_dispense_event"].isSet():
                    logging.info("GUI is not in the product dispense window")
                    logging.info("Removing all orders from the queue")
                    empty_dispense_queue()
                    logging.info("All orders from the queue are removed")
                    mobile_app_server_system_resources["/mb_io_event_lock"].release()
                    logging.info("Motherboard IO event lock released")
                    continue
                else:
                    logging.info("GUI is in the product dispense window")

            try:
                logging.info("Acquiring the lock to access the dispense queue")
                lock.acquire()
                order_info = dispense_queue.popleft()
                current_order_info = order_info
                logging.info("Order {} is taken from the dispense queue".format(order_info["orderNo"]))
            finally:
                lock.release()
                logging.info("Released the lock acquired to access the dispense queue")

            time.sleep(MIN_NEXT_ORDER_DISP_TIME)

            if order_info is not None:

                if device_provision_info["device_type"] != PANTRY_TYPE:
                    display_msg_1 = "Order No : {} \nPlease place your cup \nand \nPress Dispense".format(
                        order_info["orderNo"])
                    display_data_1 = {"msg_type": ENABLE_POP_UP_MESSAGE_TYPE_ID, "msg": display_msg_1}

                else:
                    display_data_1 = None

                logging.info("Enabling POPUP display message-1 for order {}".format(order_info["orderNo"]))
                pop_up_message_handler(display_data_1)

                try:
                    logging.info("Acquiring the lock to access the current_order_status")
                    lock.acquire()
                    current_order_status["orderId"] = order_info["orderId"]
                    current_order_status["orderNo"] = order_info["orderNo"]
                    current_order_status["state"] = WAITING_TO_DISPENSE
                    logging.info("Current order {} status changed to --> WAITING TO DISPENSE".format(order_info["orderNo"]))
                    mobile_app_server_system_resources["dispense_permission_event"].clear()
                finally:
                    lock.release()
                    logging.info("Released the lock acquired to access the current_order_status")

                logging.info("Waiting for user dispense permission event")
                mobile_app_server_system_resources["dispense_permission_event"].wait(MAX_ORDER_DISPENSE_WAIT_TIME)

                if mobile_app_server_system_resources["dispense_permission_event"].isSet():
                    logging.info("Received the user dispense permission")

                    # Disabling Keypad state
                    if device_provision_info["device_type"] == PANTRY_TYPE:
                        if keypad_enable_state == True:
                            disable_display_data = {"msg_type": DISABLE_POP_UP_MESSAGE_TYPE_ID, "keypad_state": DISABLE}
                            logging.info("=========Disabling keypad state for pantry type==========")
                            pop_up_message_handler(disable_display_data)
                            keypad_enable_state = False

                    product_no = int(order_info["productNo"])

                    input_key_handler_data = {"service": INPUT_KEY_HANDLER_ID,
                                              "data": {"caller": MOBILE_APP_ID, "key": PRODUCT_KEYS[product_no - 1],
                                                       "state": None}
                                              }

                    input_key_handler_trigger_data["event_data"] = input_key_handler_data
                    input_key_handler_trigger_data["response_required"] = True
                    logging.info("Sending input_key_handler_trigger_data to trigger_event_handler_framework")
                    input_key_handler_response = trigger_event_handler_framework(input_key_handler_trigger_data)

                    logging.info("-------Input key handler Response - {}--------".format(input_key_handler_response))
                    if input_key_handler_response == DISPENSING_STATE:

                        if device_provision_info["device_mode"] == INTERNET_MODE:
                            # INFORMING REMOTE SERVER THAT MACHINE IS BUSY
                            response = api_caller(req_type='POST', req_url=SERVER_URL + 'markAsBusy', payload={'deviceId': device_provision_info['device_id']})
                            logging.info("<<<<<<<< Machine Busy data sent : {} >>>>>>>>>>>>".format(response))
                        
                        try:
                            logging.info("Acquiring the lock to access the current_order_status")
                            lock.acquire()
                            current_order_status["state"] = DISPENSING
                            logging.info("Current {} order status changed to --> DISPENSING".format(order_info["orderNo"]))
                            logging.info("-----CURRENT ORDER STATUS - {}-------".format(current_order_status["state"]))
                        finally:
                            lock.release()
                            logging.info("Released the lock acquired to access the current_order_status")

                        if device_provision_info["device_type"] != PANTRY_TYPE:
                            display_msg_2 = "Order No : {} \nPlease collect your\n{}".format(order_info["orderNo"],
                                                                                             order_info["productName"])
                            display_data_2 = {"msg_type": ENABLE_POP_UP_MESSAGE_TYPE_ID, "msg": display_msg_2}

                            logging.info("Enabling POPUP display message-2 for order {}".format(order_info["orderNo"]))
                            pop_up_message_handler(display_data_2)

                        #time.sleep(order_info["approxDispenseTime"])

                        clean_msg_queue(mobile_app_server_system_resources["/mobile_app_queue"])
                        logging.info("Mobile app queue cleared before waiting for the dispensation started")

                        mobile_app_server_system_resources["dispense_completion_event"].clear()
                        logging.info("Dispense completion event cleared before waiting for the dispensation started")

                        logging.info("Waiting for Dispense completion event")
                        mobile_app_server_system_resources["dispense_completion_event"].wait(MAX_MACHINE_READY_EVENT_WAIT_TIME)

                        if not mobile_app_server_system_resources["dispense_completion_event"].isSet():
                            logging.warning("Dispense Completion Event Time maxed out during product dispense")

                            status = MACHINE_NOT_READY
                            cancel_order(order_info, status)

                            empty_dispense_queue()
                            logging.info("All orders from the queue are removed")

                            if device_provision_info["device_type"] != PANTRY_TYPE:
                                disable_display_data = {"msg_type": DISABLE_POP_UP_MESSAGE_TYPE_ID}
                                logging.info("Disabling POP UP for display message 2 because Machine is not ready")

                                mobile_app_server_system_resources["/mb_io_event_lock"].release()
                                logging.info("Motherboard IO event lock released during product dispense")
                            else:
                                """
                                disable_display_data = {"msg_type": DISABLE_POP_UP_MESSAGE_TYPE_ID,
                                                        "keypad_state": ENABLE}
                                logging.info("Enabling the keypad state because Machine is not ready")
                                """
                                disable_display_data = None

                            pop_up_message_handler(disable_display_data)
                            continue

                        else:
                            logging.info("Dispense completion event occurred after the dispensation started")
                            mobile_app_server_system_resources["dispense_completion_event"].clear()
                            logging.info("Dispense completion event cleared after the dispensation started")
                            logging.info("Reading message from the /mobile_app_queue")
                            
                            dispense_comp_state = json.loads(mobile_app_server_system_resources["/mobile_app_queue"].receive(timeout=MSG_QUEUE_TIME_OUT)[0])
                            logging.info("-----------Dispense completion status : {} ---------------".format(dispense_comp_state))

                            if dispense_comp_state == READY_TO_DISPENSE_STATE:
                                logging.info("Checking to update the current order status for pair orders")

                                if order_info["pairOrderFlag"] == False:
                                   update_current_order_status()
                                   logging.info("Updated the current order for pair orders")

                                try:
                                   logging.info("Acquiring the lock to access the dispensed_orders")
                                   lock.acquire()
                                   dispensed_order_info = {}
                                   dispensed_order_info.__setitem__("orderId", order_info["orderId"])
                                   dispensed_order_info.__setitem__("productName", order_info["productName"])
                                   dispensed_orders.append(dispensed_order_info)
                                   logging.info("Current order {} status changed to --> DISPENSED".format(order_info["orderNo"]))
                                finally:
                                   lock.release()
                                   logging.info("Releasing the lock acquired to access the dispensed_orders")

                            elif dispense_comp_state == MACHINE_ERROR_STATE:
                                status = MACHINE_ERROR
                                cancel_order(order_info, status)
                                logging.info("Cancelling current order {} due to MACHINE ERROR".format(order_info["orderNo"]))
                            else:
                                status = MACHINE_NOT_READY
                                cancel_order(order_info, status)
                                logging.info("Cancelling current order {} due to unknown MACHINE ERROR or MACHINE NOT READY".format(order_info["orderNo"]))

                    elif input_key_handler_response in DISPENSE_ERROR_STATE:
                        logging.info("Input_key_handler_response is in DISPENSE_ERROR_STATE")
                        #update_current_order_status()
                        status = DISPENSE_ERROR_STATE[input_key_handler_response]["status"]
                        cancel_order(order_info, status)
                        logging.info("Cancelling current order {}".format(order_info["orderNo"]))
                        logging.info("Order cancelled because {}".format(DISPENSE_ERROR_STATE[input_key_handler_response]["debug_msg"]))

                        if DISPENSE_ERROR_STATE[input_key_handler_response]["empty_dispense_queue_flag"] == True:
                            empty_dispense_queue()

                        display_msg = DISPENSE_ERROR_STATE[input_key_handler_response]["display_msg"]

                        if device_provision_info["device_type"] != PANTRY_TYPE:
                            logging.info("Enabling POP UP for Error message")
                            display_data = {"msg_type": ENABLE_POP_UP_MESSAGE_TYPE_ID, "msg": display_msg}
                            pop_up_message_handler(display_data)
                            time.sleep(ERROR_GUI_POP_UP_WAIT_TIME)

                    else:
                        status = MACHINE_NOT_READY
                        cancel_order(order_info, status)
                        logging.info("Cancelling current order {}".format(order_info["orderNo"]))
                        logging.error("Order cancelled because invalid error case occurred during dispensation request")

                        empty_dispense_queue()
                        logging.error("Emptying dispense queue because invalid error case occured")

                        display_msg = "Something went wrong \nPlease try after sometime"

                        if device_provision_info["device_type"] != PANTRY_TYPE:
                            logging.error("Enabling POPUP for invalid case Error message for order {}".format(order_info["orderNo"]))
                            display_data = {"msg_type": ENABLE_POP_UP_MESSAGE_TYPE_ID, "msg": display_msg}
                            pop_up_message_handler(display_data)
                            time.sleep(ERROR_GUI_POP_UP_WAIT_TIME)

                    if device_provision_info["device_type"] != PANTRY_TYPE:
                        disable_display_data = {"msg_type": DISABLE_POP_UP_MESSAGE_TYPE_ID}
                    else:
                        disable_display_data = None

                    logging.info("Disabling POPUP display message-2 or Error message for order {}".format(order_info["orderNo"]))
                    pop_up_message_handler(disable_display_data)

                else:
                    status = TIMEOUT_EXPIRED
                    cancel_order(order_info, status)
                    logging.info("Cancelling current order {} due to dispense timeout expiry".format(order_info["orderNo"]))

                    if device_provision_info["device_type"] != PANTRY_TYPE:
                        display_msg = "Dispense permission \nWaiting time Expired"
                        display_data = {"msg_type": ENABLE_POP_UP_MESSAGE_TYPE_ID, "msg": display_msg}

                        logging.error("Enabling POPUP timeout error message for order {}".format(order_info["orderNo"]))
                        pop_up_message_handler(display_data)
                        time.sleep(ERROR_GUI_POP_UP_WAIT_TIME)

                        disable_display_data = {"msg_type": DISABLE_POP_UP_MESSAGE_TYPE_ID}
                        logging.error("Disabling POPUP timeout error message for order {}".format(order_info["orderNo"]))
                    else:
                        disable_display_data = None

                    pop_up_message_handler(disable_display_data)

            if device_provision_info["device_mode"] == INTERNET_MODE:
                # INFORMING REMOTE SERVER THAT MACHINE IS READY TO DISPENSE
                response = api_caller(req_type='POST', req_url=SERVER_URL + 'orderDispensed', payload={'deviceId': device_provision_info['device_id']})
                logging.info("<<<<<<<< Order Dispensed data sent : {} >>>>>>>>>>>>".format(response))

            if device_provision_info["device_type"] != PANTRY_TYPE:
                mobile_app_server_system_resources["/mb_io_event_lock"].release()
                logging.info("Motherboard IO event released after one complete cycle")


def machine_ready_event_status_handler(release_mb_io_lock):
    global mobile_app_server_system_resources

    if not mobile_app_server_system_resources["machine_ready_event"].isSet():  # change to function
        logging.info("Waiting for Machine Ready Event")
        mobile_app_server_system_resources["machine_ready_event"].wait(MAX_MACHINE_READY_EVENT_WAIT_TIME)

        if not mobile_app_server_system_resources["machine_ready_event"].isSet():
            empty_dispense_queue()  # remove all orders
            logging.warning("Machine Ready Event Timed out")

            if release_mb_io_lock == True:
                if device_provision_info["device_type"] != PANTRY_TYPE:
                    mobile_app_server_system_resources["/mb_io_event_lock"].release()
                    logging.info("Motherboard IO event lock released after Motherboard IO event lock acquired")

            return FAILURE
        else:
            logging.info("Machine Ready Event occurred")
            return SUCCESS
    else:
        logging.info("Machine is in the Ready state")
        return SUCCESS


def update_current_order_status():
    global dispense_event, current_order_status, mobile_app_server_system_resources
    try:
        logging.info("Acquiring lock to access current_order_status")
        lock.acquire()
        current_order_status["orderId"] = None
        current_order_status["orderNo"] = None
        current_order_status["state"] = None
        mobile_app_server_system_resources["dispense_permission_event"].clear()
    finally:
        lock.release()
        logging.info("Released the lock acquired to access current_order_status")
    return


def cancel_order(order_info, status):
    global cancelled_orders, dispense_queue

    update_current_order_status()
    logging.info("Current order status updated from cancel order")

    try:
        logging.info("Acquiring lock to access cancelled_order_status")
        orders_to_be_cancelled = []
        orders_to_be_cancelled.append(order_info)

        lock.acquire()

        if order_info["pairOrderFlag"] == True:
            pair_order = dispense_queue.popleft()
            orders_to_be_cancelled.append(pair_order)
            logging.info("Cancelling pair order")

        for order in orders_to_be_cancelled:
            cancelled_order_info = {}
            cancelled_order_info.__setitem__("orderId", order["orderId"])
            cancelled_order_info.__setitem__("productName", order["productName"])
            cancelled_order_info.__setitem__("status", status)
            cancelled_orders.append(cancelled_order_info)
    finally:
        lock.release()
        logging.info("Released the lock acquired to access cancelled_order_status")

    logging.info("Orders to be cancelled :")
    logging.info(orders_to_be_cancelled)

    return


def clean_dispensed_and_cancelled_orders():
    global dispensed_and_cancelled_orders_cleaner_flag, dispensed_orders, cancelled_orders
    dispensed_and_cancelled_orders_cleaner_flag = True
    logging.info("Started cleaning dispensed and cancelled orders")
    try:
        logging.info("Getting the current orders in dispensed and cancelled orders list")
        logging.info("Acquiring lock to access dispensed and cancelled orders list")
        lock.acquire()
        current_dispensed_orders_count = len(dispensed_orders)
        current_cancelled_orders_count = len(cancelled_orders)
    finally:
        lock.release()
        logging.info("Released the lock acquired to access dispensed and cancelled orders list")

    time.sleep(MAX_DISP_AND_CANC_ORDERS_CLEAN_WAIT_TIME)

    try:
        logging.info("Acquiring lock to access dispensed and cancelled orders list")
        lock.acquire()
        del dispensed_orders[0:current_dispensed_orders_count]
        del cancelled_orders[0:current_cancelled_orders_count]
    finally:
        lock.release()
        logging.info("Released the lock acquired to access dispensed and cancelled orders list")

    dispensed_and_cancelled_orders_cleaner_flag = False
    logging.info("Finished cleaning dispensed and cancelled orders")
    return


def empty_dispense_queue():
    global dispense_queue, cancelled_orders
    logging.info("Starting to Emptying the dispense queue")

    update_current_order_status()
    logging.info("Current order status updated from empty dispense queue")

    status = MACHINE_NOT_READY
    try:
        logging.info("Acquiring lock to access dispense queue")
        lock.acquire()
        for order_info in dispense_queue:
            cancelled_order_info = {}
            cancelled_order_info.__setitem__("orderId", order_info["orderId"])
            cancelled_order_info.__setitem__("productName", order_info["productName"])
            cancelled_order_info.__setitem__("status", status)
            cancelled_orders.append(cancelled_order_info)
        dispense_queue.clear()
        logging.info("Dispense queue is Emptied")
    finally:
        lock.release()
        logging.info("Released the lock acquired to access dispense queue")
    return


def pop_up_message_handler(display_data):
    global input_key_handler_trigger_data

    if display_data != None:
        logging.info("Sending display data to trigger event handler framework")
        input_key_handler_data = {"service": GUI_CONTROLLER_ID, "data": display_data}

        input_key_handler_trigger_data["event_data"] = input_key_handler_data
        input_key_handler_trigger_data["response_required"] = None
        trigger_event_handler_framework(input_key_handler_trigger_data)
        logging.info("Display data successfully sent to trigger event handler framework")

    return


def configure_system_resources(system_resources, device_provision_info_param):
    global mobile_app_server_system_resources, device_provision_info

    mobile_app_server_system_resources = system_resources
    device_provision_info = device_provision_info_param
    logging.info("Mobile App systems resources configured in dispense queue handler")

    return
