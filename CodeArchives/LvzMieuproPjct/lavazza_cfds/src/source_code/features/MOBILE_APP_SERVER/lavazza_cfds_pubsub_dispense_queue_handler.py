"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_pubsub_dispense_queue_handler.py
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
import requests

from lavazza_cfds_mobile_app_server_macros import *

sys.path.append(MB_IO_HANDLER_FILE_PATH)

from lavazza_cfds_mb_io_handler_macros import *

logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - Pubsub_Dispense_Handler - %(levelname)s - %(message)s',
                    filename=LAVAZZA_COMMON_LOG_FILE, filemode='a')

# Initializing a queue
dispense_queue = deque()

# Declaring a lock
lock = threading.Lock()

keypad_enable_state = True

system_resources_events = None
device_provision_info = None
configured_product_info = None
input_key_handler_trigger_data = None


def append_dispense_queue(order):
    global dispense_queue, system_resources_events
    try:
        logging.info("<<<<<<Acquiring the lock to access the dispense queue for adding product number>>>>>>")
        logging.info("order - {}".format(order))

        lock.acquire()
        if order["msg_type"] == "order":
            product_num = order["msg"]
            dispense_queue.append(product_num)
            logging.info(system_resources_events)
            if system_resources_events["pubsub_dispense_queue_handler_event"].isSet() is False:
                system_resources_events["pubsub_dispense_queue_handler_event"].set()
                logging.info("Dispense queue handler event is set after an order is received from pubsub")
            logging.info("Order from pubsub for Product Number {} added to the dispense queue".format(product_num))
            
        elif order["msg_type"] == "dispense":
            dispense_permission_event_handler()
    finally:
        lock.release()
        logging.info("Released the lock acquired to access the dispense queue")

    return


def dispense_permission_event_handler():
    global system_resources_events
    system_resources_events["pubsub_dispense_permission_event"].set()
    return


def dispense_queue_handler():
    global dispense_queue, input_key_handler_trigger_data, configured_product_info
    global system_resources_events, device_provision_info, keypad_enable_state

    input_key_handler_trigger_data = {"thread_name": "mobile_app_backend",
                                      "event": system_resources_events["mb_io_event"],
                                      "queue": system_resources_events["/mb_io_queue"],
                                      "event_data": None,
                                      "finished_event": system_resources_events["mb_io_finished_event"],
                                      "response_required": None}

    # logging.debug("Resources in dispense queue handler {}".format(system_resources_events))
    while True:
        if len(dispense_queue) < MIN_QUEUE_LENTH:
            logging.info("Queue is Empty")

            if device_provision_info["device_type"] == PANTRY_TYPE:
                if keypad_enable_state == False:
                    disable_display_data = {"msg_type": DISABLE_POP_UP_MESSAGE_TYPE_ID, "keypad_state": ENABLE}
                    logging.info("=========Enabling keypad state for pantry type==========")
                    pop_up_message_handler(disable_display_data)
                    keypad_enable_state = True

            if system_resources_events["pubsub_dispense_queue_handler_event"].isSet() is True:
                system_resources_events["pubsub_dispense_queue_handler_event"].clear()
                logging.info("Dispense queue handler event is cleared")

            logging.info("Waiting for dispense queue handler event")
            system_resources_events["pubsub_dispense_queue_handler_event"].wait()
            logging.info("Dispense queue handler event received")
        else:
            if device_provision_info["device_type"] != PANTRY_TYPE:
                system_resources_events["/mb_io_event_lock"].acquire()
                logging.info("Motherboard IO event lock acquired")
            else:
                logging.info("Machine is PANTRY TYPE")

            if device_provision_info["device_type"] != PANTRY_TYPE:
                logging.info("Checking if the GUI is in Product dispense window")
                if not system_resources_events["gui_product_dispense_event"].isSet():
                    logging.info("GUI is not in the product dispense window")
                    logging.info("Removing all orders from the queue")
                    dispense_queue.clear()
                    logging.info("All orders from the queue are removed")
                    system_resources_events["/mb_io_event_lock"].release()
                    logging.info("Motherboard IO event lock released")
                    continue
                else:
                    logging.info("GUI is in the product dispense window")

            try:
                logging.info("Acquiring the lock to access the dispense queue")
                lock.acquire()
                product_num = dispense_queue.popleft()
                logging.info("Order for product number {} is taken from the dispense queue".format(product_num))
            finally:
                lock.release()
                logging.info("Released the lock acquired to access the dispense queue")

            if product_num is not None:

                if device_provision_info["device_type"] != PANTRY_TYPE:
                    display_msg_1 = "Please place your cup \nand \nPress Dispense"
                    display_data_1 = {"msg_type": ENABLE_POP_UP_MESSAGE_TYPE_ID, "msg": display_msg_1}

                else:
                    display_data_1 = None

                logging.info("Enabling POPUP display message-1 for product number {}".format(product_num))
                pop_up_message_handler(display_data_1)

                logging.info("Current order for product number {} status changed to --> WAITING TO DISPENSE".format(product_num))
                system_resources_events["pubsub_dispense_permission_event"].clear()

                logging.info("Waiting for user dispense permission event")
                system_resources_events["pubsub_dispense_permission_event"].wait(MAX_ORDER_DISPENSE_WAIT_TIME)

                if system_resources_events["pubsub_dispense_permission_event"].isSet():
                    logging.info("Received the user dispense permission")

                    # Disabling Keypad state
                    if device_provision_info["device_type"] == PANTRY_TYPE:
                        if keypad_enable_state == True:
                            disable_display_data = {"msg_type": DISABLE_POP_UP_MESSAGE_TYPE_ID, "keypad_state": DISABLE}
                            logging.info("=========Disabling keypad state for pantry type==========")
                            pop_up_message_handler(disable_display_data)
                            keypad_enable_state = False

                    product_no = int(product_num)

                    input_key_handler_data = {"service": INPUT_KEY_HANDLER_ID,
                                              "data": {"caller": MOBILE_APP_ID, "key": PRODUCT_KEYS[product_no - 1],
                                                       "state": None}
                                              }

                    logging.info("-------Input key handler Data - {}--------".format(input_key_handler_data))

                    input_key_handler_trigger_data["event_data"] = input_key_handler_data
                    input_key_handler_trigger_data["response_required"] = True
                    logging.info("<<<<<<<Sending input_key_handler_trigger_data to trigger_event_handler_framework>>>>>>>")
                    input_key_handler_response = trigger_event_handler_framework(input_key_handler_trigger_data)

                    logging.info("-------Input key handler Response - {}--------".format(input_key_handler_response))
                
                    if input_key_handler_response == DISPENSING_STATE:
                        # SUCCESS
                        logging.info("Current order for product number {} status changed to --> DISPENSING".format(product_num))

                        if device_provision_info["device_type"] != PANTRY_TYPE:
                            display_msg_2 = "Please collect your\n order"
                            display_data_2 = {"msg_type": ENABLE_POP_UP_MESSAGE_TYPE_ID, "msg": display_msg_2}

                            logging.info("Enabling POPUP display message-2 for product number {}".format(product_num))
                            pop_up_message_handler(display_data_2)

                        #product_info = next((product_info for product_info in configured_product_info if product_info["productNo"] == product_no),None)

                        #logging.info("\n\n")
                        #logging.info("<<<<<<<Current order waiting time - {}>>>>>>>".format(product_info["approxDispenseTime"]))
                        #logging.info("\n\n")
                        
                        #if product_info != None:
                            #time.sleep(product_info["approxDispenseTime"])
                        #else:
                            #time.sleep(20)

                        clean_msg_queue(system_resources_events["/mobile_app_queue"])
                        logging.info("Mobile app queue cleared before waiting for the dispensation started")

                        system_resources_events["dispense_completion_event"].clear()
                        logging.info("Dispense completion event cleared before waiting for the dispensation started")

                        system_resources_events["dispense_completion_event"].wait(MAX_MACHINE_READY_EVENT_WAIT_TIME)

                        if system_resources_events["dispense_completion_event"].isSet():
                            logging.warning("Dispense Completion Event Set Successfully")

                        logging.info("Waiting time completed")

                    else:
                        # MACHINE_ERROR
                        logging.info("Cancelling current order for product number {}".format(product_num))
                        logging.error("Order cancelled because invalid error case occurred during dispensation request")

                        clean_msg_queue(system_resources_events["/mobile_app_queue"])
                        logging.info("Mobile app queue cleared due to error occured while dispensation request")


                        display_msg = "Something went wrong \nPlease try after sometime"

                        if device_provision_info["device_type"] != PANTRY_TYPE:
                            logging.error("Enabling POPUP for invalid case Error message for order number {}".format(product_num))
                            display_data = {"msg_type": ENABLE_POP_UP_MESSAGE_TYPE_ID, "msg": display_msg}
                            pop_up_message_handler(display_data)
                            time.sleep(ERROR_GUI_POP_UP_WAIT_TIME)

                    if device_provision_info["device_type"] != PANTRY_TYPE:
                        disable_display_data = {"msg_type": DISABLE_POP_UP_MESSAGE_TYPE_ID}
                    else:
                        disable_display_data = None

                    logging.info("Disabling POPUP display message-2 or Error message for order number {}".format(product_num))
                    pop_up_message_handler(disable_display_data)

                else:
                    # TIMEOUT_EXPIRED
                    logging.info("Current order is cancelled for product number {} due to dispense timeout expiry".format(product_num))

                    if device_provision_info["device_type"] != PANTRY_TYPE:
                        display_msg = "Dispense permission \nWaiting time Expired"
                        display_data = {"msg_type": ENABLE_POP_UP_MESSAGE_TYPE_ID, "msg": display_msg}

                        logging.error("Enabling POPUP timeout error message for product number {}".format(product_num))
                        pop_up_message_handler(display_data)
                        time.sleep(ERROR_GUI_POP_UP_WAIT_TIME)

                        disable_display_data = {"msg_type": DISABLE_POP_UP_MESSAGE_TYPE_ID}
                        logging.error("Disabling POPUP timeout error message for product number {}".format(product_num))
                    else:
                        disable_display_data = None

                    pop_up_message_handler(disable_display_data)

            # INFORMING REMOTE SERVER THAT MACHINE IS READY TO DISPENSE
            response = api_caller(req_type='POST', req_url=SERVER_URL + 'orderDispensed', payload={'deviceId': device_provision_info['device_id']})
            logging.info("<<<<<<<< Order Dispensed data sent : {} >>>>>>>>>>>>".format(response))

            if device_provision_info["device_type"] != PANTRY_TYPE:
                system_resources_events["/mb_io_event_lock"].release()
                logging.info("Motherboard IO event released after one complete cycle")


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


def configure_system_resources(system_resources, device_provision_info_param, configured_product_info_param):
    global system_resources_events, device_provision_info, configured_product_info

    system_resources_events = system_resources
    device_provision_info = device_provision_info_param
    configured_product_info = configured_product_info_param
    logging.info("Mobile App systems resources configured in pubsub dispense queue handler")
    #logging.info("system_resources_events - {}".format(system_resources_events))

    return
