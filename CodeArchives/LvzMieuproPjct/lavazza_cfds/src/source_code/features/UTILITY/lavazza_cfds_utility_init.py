"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_utility_init.py
 * Version        : 1.1
 * Date           : APRIL 20 2021
 *
 * Copyright (C) mieuPro Systems, 2021
 *
 ******************************************************************************
 """
# def utility_handler(received_data): - Invoking utility event handlers based on the msg_type from the received data
# def utility_init(): - Waiting for utility event, Receives events from other modules
# def main(): - updates process_id and calls the utility_init

import lavazza_cfds_utility_macros
import lavazza_cfds_utility_gui_message_handler as gui_message_handler
import logging
from lavazza_cfds_utility_keep_alive_handler import keep_alive_handler, update_device_info_to_server

from lavazza_cfds_utility_server_communication_msg_handler import generate_qr_code

gui_event_trigger_data = {}
server_communication_event_trigger_data = {}
dev_type = None
logging.basicConfig(level=lavazza_cfds_utility_macros.LOG_LEVEL,
                    format='%(asctime)s - UTILITY - %(levelname)s - %(message)s',
                    filename=lavazza_cfds_utility_macros.LAVAZZA_COMMON_LOG_FILE, filemode='a')#lavazza_cfds_utility_macros.LAVAZZA_COMMON_LOG_FILE


def trigger_event(event_trigger_data, lock):
    # It indicates the backend_to_gui_event_lock state, whether it is in the acquired state or released state
    try:
        event_lock_status = False
        response = None

        # gui_event_trigger_data["event_data"] = event_data
        logging.info("gui_backend_event triggered")

        # Acquiring lock to avoid race condition at the GUI backend event access.
        lavazza_cfds_utility_macros.utility_system_events_queues[lock].acquire(
            timeout=lavazza_cfds_utility_macros.LOCK_ACQUIRE_TIME_OUT)
        logging.info("{} event_lock acquired".format(lock))
        event_lock_status = True

        # Send the msg to the GUI.
        response = lavazza_cfds_utility_macros.trigger_event_handler_framework(event_trigger_data)

    except Exception as error:
        logging.exception("trigger_event - {}".format(error))
        response = lavazza_cfds_utility_macros.FAILURE

    finally:
        # We are using the counting semaphore for the lock. So, we need to maintain it's lock count as 1.
        # Every release call increases it's lock count by 1.
        # So, we need to release the lock only if we were acquired it.
        if event_lock_status:
            lavazza_cfds_utility_macros.utility_system_events_queues[lock].release()
            logging.info("trigger_event : {} event_lock released".format(lock))
    return response


def get_mobile_order(msg_type, msg):

    try:

        mobile_app_event_trigger_data = {"thread_name": "mobile_app",
                          "event": lavazza_cfds_utility_macros.utility_system_events_queues[
                              "mobile_app_order_event"],
                          "queue": lavazza_cfds_utility_macros.utility_system_events_queues[
                              "/mobile_app_order_queue"],
                          "event_data": None,
                          "finished_event": None,
                          "response_required": False}

        if msg is not None:
            
            mobile_app_event_trigger_data["event_data"] = {"msg_type": msg_type, "msg":msg}
            logging.info("send mobile_app_event_trigger_data {}".format(mobile_app_event_trigger_data))

            logging.info("mobile_app_event_trigger_data - {}".format(mobile_app_event_trigger_data))

            trigger_event(mobile_app_event_trigger_data,"/mobile_app_order_event_lock")                
            logging.debug("successfully send mobile_app_event_trigger_data")
                          
        return None

    except Exception as Error:
        logging.exception("get_mobile_order: {}".format(Error))


def utility_handler(received_data):
    """Invoking utility event handlers based on the msg_type from the received data """

    try:

        global dev_type
        response = None

        msg_type = received_data['msg_type']

        if 'msg' in received_data.keys():
            msg = received_data['msg']

        # DEVICE INFO MSG TYPE
        if msg_type == lavazza_cfds_utility_macros.DEVICE_INFO_MESSAGE_TYPE_ID:
            response = gui_message_handler.update_device_info(msg_type, msg)

        # DEVICE MODE MSG TYPE
        if msg_type == lavazza_cfds_utility_macros.DEVICE_MODE_UPDATE_MESSAGE_TYPE_ID:
            response = gui_message_handler.update_device_info(msg_type, msg)

        # GSM INFO MSG TYPE
        elif msg_type == lavazza_cfds_utility_macros.GSM_CONFIG_MESSAGE_TYPE_ID:
            response = gui_message_handler.update_device_gsm_info(msg_type, msg)

        # WIFI CONFIG MSG TYPE
        elif msg_type == lavazza_cfds_utility_macros.WIFI_INFO_MESSAGE_TYPE_ID:
            response = gui_message_handler.update_device_wifi_info(msg_type, msg)

        # PRODUCT CONFIGURE MSG TYPE
        elif msg_type == lavazza_cfds_utility_macros.PRODUCT_NAME_MESSAGE_TYPE_ID:
            response = gui_message_handler.update_device_provision_info(msg_type, "provisioned_product_details", msg,
                                                                        None)

        # PROVISIONED MSG TYPE
        elif msg_type == lavazza_cfds_utility_macros.INIT_PROVISION_MESSAGE_TYPE_ID:
            response = gui_message_handler.update_device_provision_info(msg_type, "provision_status", True, "reboot")

        # REBOOT MSG TYPE
        elif msg_type == lavazza_cfds_utility_macros.REBOOT_MESSAGE_TYPE_ID:
            response = gui_message_handler.device_power_off("reboot")

        # SHUTDOWN MSG TYPE
        elif msg_type == lavazza_cfds_utility_macros.SHUTDOWN_MESSAGE_TYPE_ID:
            response = gui_message_handler.device_power_off("shutdown")

        # APPLICATION RESET MSG TYPE
        elif msg_type == lavazza_cfds_utility_macros.APPLICATION_RESET_MESSAGE_TYPE_ID:
            response = gui_message_handler.application_reset("reboot")

        # QR UPDATE MSG TYPE
        elif msg_type == lavazza_cfds_utility_macros.QR_CODE_UPDATE_STATUS_MESSAGE_TYPE_ID:

            if generate_qr_code() == lavazza_cfds_utility_macros.SUCCESS:

                if dev_type == lavazza_cfds_utility_macros.RETRO_FIT_TYPE:
                    gui_event_trigger_data["event_data"] = {
                        "msg_type": lavazza_cfds_utility_macros.QR_CODE_UPDATE_STATUS_MESSAGE_TYPE_ID}
                    logging.info("gui event trigger data {}".format(gui_event_trigger_data))

                    if trigger_event(gui_event_trigger_data,
                                     "/backend_to_gui_event_lock") == lavazza_cfds_utility_macros.SUCCESS:

                        pass
                    else:
                        logging.debug("Failed to show qr in gui")
            else:
                logging.debug("Failed to generate qr")

        elif msg_type == lavazza_cfds_utility_macros.GET_DEVICE_ID_MESSAGE_TYPE:
            response = gui_message_handler.get_device_id(msg_type, msg)

        elif msg_type == "order" or msg_type == "dispense":
            get_mobile_order(msg_type, msg)

    except Exception as error:
        logging.debug("Error in utility handler {} ".format(error))
    finally:
        logging.debug(" response - {}".format(response))
        if response is not None:
            logging.debug(" response - {}".format(response))
            return response


def utility_init():
    """Waiting for utility event, Receives events from other modules"""
    global gui_event_trigger_data, dev_type, server_communication_event_trigger_data
    try:

        if lavazza_cfds_utility_macros.initialize_service(lavazza_cfds_utility_macros.utility_system_events_queues,
                                                       "lavazza_cfds_utility.service") == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("utility_service initialization failed")

        logging.debug("------------- utility service init successfully ----------------- ")
        
        device_info = {}
        # read the DEVICE_PROVISION_INFO_FILE to get the device type info
        if lavazza_cfds_utility_macros.read_from_file(device_info,
                                                      lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("File reading error in ", lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE)

        dev_type = device_info["device_type"]
        if device_info["provision_status"]:

            generate_qr_code()

            if device_info["device_mode"] == lavazza_cfds_utility_macros.INTERNET_MODE:
                keep_alive_handler()
                update_device_info_to_server()

                server_communication_event_trigger_data = {"thread_name": "utility",
                                          "event": lavazza_cfds_utility_macros.utility_system_events_queues[
                                              "server_communication_event"],
                                          "queue": lavazza_cfds_utility_macros.utility_system_events_queues[
                                              "/server_communication_queue"],
                                          "event_data": None,
                                          "finished_event": lavazza_cfds_utility_macros.utility_system_events_queues[
                                              "server_communication_finished_event"],
                                          "response_required": None}

                logging.info("Keep alive handler initialized successfully")
            if dev_type == lavazza_cfds_utility_macros.RETRO_FIT_TYPE:

                gui_event_trigger_data = {"thread_name": "utility",
                                          "event": lavazza_cfds_utility_macros.utility_system_events_queues[
                                              "backend_to_gui_event"],
                                          "queue": lavazza_cfds_utility_macros.utility_system_events_queues[
                                              "/backend_to_gui_queue"],
                                          "event_data": None,
                                          "finished_event": lavazza_cfds_utility_macros.utility_system_events_queues[
                                              "backend_to_gui_finished_event"],
                                          "response_required": True}
        logging.info("Waiting for utility event")

    except:
        logging.exception("utility_init - Utility resources initialization")

    try:

        while True:
            input_data = {"thread_name": "utility",
                          "event": lavazza_cfds_utility_macros.utility_system_events_queues["utility_event"],
                          "queue": lavazza_cfds_utility_macros.utility_system_events_queues["/utility_queue"],
                          "queue_handler_function": utility_handler,
                          "finished_event": lavazza_cfds_utility_macros.utility_system_events_queues[
                              "utility_finished_event"]}

            lavazza_cfds_utility_macros.event_handler_framework(input_data)

    except:
        logging.exception("utility_init - utility event error ")


def main():
    if lavazza_cfds_utility_macros.update_process_id("UTILITY") == lavazza_cfds_utility_macros.FAILURE:
        logging.error("UTILITY : updating process id")

    utility_init()


main()
