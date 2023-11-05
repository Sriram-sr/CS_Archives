"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_lcd_output_reader.py
 * Version        : 1.0
 * Date           : August 10 2020
 *
 * Copyright (C) mieuPro Systems, 2020
 *
 ******************************************************************************
 """

# serial library used to read the lcd_data from the uart interface
import RPi.GPIO as GPIO
import serial
from time import sleep

from lavazza_cfds_mb_io_handler_macros import *
import lavazza_cfds_mb_io_handler_variable

# configure the uart port for the lcd_output reading
ser = serial.Serial(port=UART_PORT, baudrate=UART_BAUD_RATE, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS, timeout=UART_READ_TIME_OUT)

mb_io_handler_system_resources = None
gui_event_trigger_data = None
mobile_app_event_trigger_data = None
dispense_completion_state = None


def send_iot_cmd(cmd):
    logging.info("Lcd_Output_Reader : Received cmd is - {}".format(cmd))
    # Set SYNC_0_KEY to HIGH. This will change the iot board to Configuration mode.
    GPIO.output(SYNC_0_KEY, GPIO.HIGH)
    # sleep time before sending the iot cmd
    sleep(KEY_PRESS_PAUSE_TIME)
    # We should flush the output buffer before sending the data.
    # It will get rid of us from the garbage.
    ser.reset_output_buffer()
    # Send command to to the iot board using uart interface.
    ser.write(cmd.encode())
    # IOT board will give response through uart interface.
    # We need to read the response while the SYNC_0_KEY in HIGH state.
    iot_board_cmd_output = pi_uart_reader()
    # After getting the response from the IOT board, We need to change the IOt board mode to lcd reading mode
    # by setting the SYNC_0_KEY to LOW.
    GPIO.output(SYNC_0_KEY, GPIO.LOW)

    return iot_board_cmd_output


def iot_board_handler(cmd):
    # It indicates the iot_board_handler_lock state, whether it is in the acquired state or released state.
    uart_access_lock_status = False
    count = 0
    try:
        # Acquiring lock to avoid race condition at the uart access.
        mb_io_handler_system_resources["/uart_access_lock"].acquire(LOCK_ACQUIRE_TIME_OUT)
        logging.info("Iot_Board_Handler : uart_access_lock acquired")
        uart_access_lock_status = True

        while True:
            iot_board_cmd_output = send_iot_cmd(cmd)

            # In case of any error in uart reading, we won't getting any data.
            if len(iot_board_cmd_output) == 0:
                logging.warning("Lcd_Output_Reader : No reply for the cmd from the iot board")
                count += 1
                if count <= SEND_IOT_CMD_MAX_TRY:
                    sleep(SEND_IOT_CMD_RETRY_WAIT_TIME)
                else:
                    logging.info("Input_Key_Handler : Key simulation max retry finished")
                    return FAILURE

                continue

            elif "ERROR" in iot_board_cmd_output:
                logging.warning("Lcd_Output_Reader : ERROR reply from the iot board")
                count += 1

                # Resetting the micro_controller board
                GPIO.output(IOT_BOARD_RESET_KEY, GPIO.HIGH)
                sleep(KEY_PRESS_PAUSE_TIME)
                GPIO.output(IOT_BOARD_RESET_KEY, GPIO.LOW)
                logging.debug("Lcd_Output_Reader : IOT board reseted successfully")

                if count <= SEND_IOT_CMD_MAX_TRY:
                    sleep(SEND_IOT_CMD_RETRY_WAIT_TIME)
                else:
                    logging.info("Input_Key_Handler : Key simulation max retry finished")
                    return FAILURE

                continue

            else:
                logging.info("Lcd_Output_Reader : iot_board_handler function finished")
                break

        return iot_board_cmd_output

    except Exception as error:
        logging.exception("Lcd_Output_Reader : iot_board_handler - {}".format(error))

    finally:
        # We are using the counting semaphore for the lock. So, we need to maintain it's lock count as 1.
        # Every release call increases it's lock count by 1.
        # So, we need to release the lock only if we were acquired it.
        if uart_access_lock_status:
            mb_io_handler_system_resources["/uart_access_lock"].release()
            logging.info("Iot_Board_Handler : uart_access_lock released")


def user_interface_controller(data):
    if DEVICE_TYPE != PANTRY_TYPE:
        # It indicates the backend_to_gui_event_lock state, whether it is in the acquired state or released state
        backend_to_gui_event_lock_status = False
        try:
            gui_event_trigger_data["event_data"] = data
            logging.info("Lcd_Output_Reader : gui_backend_event triggered")

            # Acquiring lock to avoid race condition at the GUI backend event access.
            mb_io_handler_system_resources["/backend_to_gui_event_lock"].acquire(timeout=LOCK_ACQUIRE_TIME_OUT)
            logging.info("Lcd_Output_Reader : backend_to_gui_event_lock acquired")
            backend_to_gui_event_lock_status = True
            # Send the msg to the GUI.
            trigger_event_handler_framework(gui_event_trigger_data)

        except Exception as error:
            logging.exception("Lcd_Output_Reader : iot_board_handler - {}".format(error))

        finally:
            # We are using the counting semaphore for the lock. So, we need to maintain it's lock count as 1.
            # Every release call increases it's lock count by 1.
            # So, we need to release the lock only if we were acquired it.
            if backend_to_gui_event_lock_status:
                mb_io_handler_system_resources["/backend_to_gui_event_lock"].release()
                logging.info("Lcd_Output_Reader : backend_to_gui_event_lock released")

    else:
        if data["msg_type"] == ENABLE_POP_UP_MESSAGE_TYPE_ID:
            logging.warning("Lcd_Output_Reader : We have disabled this functionality")

        elif data["msg_type"] == DISABLE_POP_UP_MESSAGE_TYPE_ID:
            # lcd_reader_status = iot_board_handler(MB_CONTROL_LCD_DISPLAY_CMD)
            # logging.debug("Lcd_Output_Reader : Lcd_reader_status - {}".format(lcd_reader_status))

            # keypad_status = iot_board_handler(KEYPAD_STATUS_CMD)
            # logging.debug("Lcd_Output_Reader : Current Keypad status Before Set - {}".format(keypad_status))

            if data["keypad_state"] == DISABLE:
                keypad_status = iot_board_handler(DISABLE_KEYPAD_CMD)
                logging.debug("Lcd_Output_Reader : Keypad_status - {}".format(keypad_status))
            elif data["keypad_state"] == ENABLE:
                keypad_status = iot_board_handler(ENABLE_KEYPAD_CMD)
                logging.debug("Lcd_Output_Reader : Keypad_status - {}".format(keypad_status))
            else:
                logging.warning("Lcd_Output_Reader : Invalid value for the Keypad state")

            # keypad_status = iot_board_handler(KEYPAD_STATUS_CMD)
            # logging.debug("Lcd_Output_Reader : Current Keypad status After Set - {}".format(keypad_status))

            # logging.info("Lcd_Output_Reader : For testing purpose we have disabled this functionality")

        else:
            logging.warning("Lcd_Output_Reader : user_interface_controller - Invalid request")


# Lcd data reader to know the current state of the machine by analyzing the lcd data
def lcd_output_reader(lcd_data):

    try:
        logging.info("Lcd_Output_Reader : lcd_output_reader function started")
        global dispense_completion_state

        # Motherboard gives the lcd_data of 32 bytes.
        if len(lcd_data) == LCD_DATA_SIZE:
            if not lcd_data.split():
                logging.warning("Lcd_Output_Reader : We are getting Empty string")
                return FAILURE

            # assign the received_data to the lcd_data for the global accessing within the process
            lavazza_cfds_mb_io_handler_variable.lcd_data = lcd_data

            logging.debug("Lcd_Output_Reader : side display data is : {}".format(
                lavazza_cfds_mb_io_handler_variable.lcd_data))

            '''Get the Machine state by analyzing the lcd_data'''
            # Foamer Off string in the lcd_data tells that the machine is in the Foamer Off state.
            # In this state milk product dispensation will not happen.
            if FOAMER_OFF in lavazza_cfds_mb_io_handler_variable.lcd_data and \
                    lavazza_cfds_mb_io_handler_variable.foamer_state != DISABLE:
                lavazza_cfds_mb_io_handler_variable.foamer_state = DISABLE

            # Foamer On string in the lcd_data tells that the machine is in the Foamer On state.
            # In this state milk product dispensation will happen.
            elif FOAMER_ON in lavazza_cfds_mb_io_handler_variable.lcd_data and \
                    lavazza_cfds_mb_io_handler_variable.foamer_state != ENABLE:
                lavazza_cfds_mb_io_handler_variable.foamer_state = ENABLE

            # MILK_NOT_READY state tells that Milk is not getting reached the dispensing temperature.
            if lavazza_cfds_mb_io_handler_variable.lcd_data == MILK_NOT_READY:
                lavazza_cfds_mb_io_handler_variable.machine_state = MILK_NOT_READY_STATE

            # In DISPENSING_STATE lcd_data will contain the product name.
            # There are some lcd_data which contains the product name in the service card configuration also.
            # So, we need to avoid those lcd_data to identify the DISPENSING_STATE.
            elif [product_name for product_name in PRODUCT_DISPENSING_NAMES if product_name in lavazza_cfds_mb_io_handler_variable.lcd_data] and \
                    not lavazza_cfds_mb_io_handler_variable.service_card_state:
                lavazza_cfds_mb_io_handler_variable.machine_state = DISPENSING_STATE

            # Ready string in the lcd_data tells that Machine is in the READY_TO_DISPENSE_STATE.
            elif READY in lavazza_cfds_mb_io_handler_variable.lcd_data:
                # If we get the Ready string after the DISPENSING_STATE, it shows the dispense completion.
                if lavazza_cfds_mb_io_handler_variable.machine_state == DISPENSING_STATE:
                    dispense_completion_state = True
                lavazza_cfds_mb_io_handler_variable.machine_state = READY_TO_DISPENSE_STATE

            # FOAMER_OFF_ERROR in the lcd_data shows that milk product dispensing is not allowed
            # in the foamer off state.
            elif lavazza_cfds_mb_io_handler_variable.lcd_data == FOAMER_OFF_ERROR:
                lavazza_cfds_mb_io_handler_variable.machine_state = ENABLE_FOAMER_ON

            # Machine will give the msg as Please wait, if boiler not attain it's dispensing temperature.
            # Rinse string in the lcd_data shows that Machine rinsing going now.
            # So, in the above states Machine will not accept the dispense request.
            elif PLEASE_WAIT in lavazza_cfds_mb_io_handler_variable.lcd_data or \
                    lavazza_cfds_mb_io_handler_variable.lcd_data == RINSE:
                lavazza_cfds_mb_io_handler_variable.machine_state = MACHINE_NOT_READY_STATE

            # Service Card string in the lcd_data tells that the machine is the Service Card inserted state.
            # In this state product dispensation will not happen.
            elif SERVICE_CARD in lavazza_cfds_mb_io_handler_variable.lcd_data:
                lavazza_cfds_mb_io_handler_variable.machine_state = MACHINE_NOT_READY_STATE
                lavazza_cfds_mb_io_handler_variable.service_card_state = ENABLE

            # Save data in the lcd_data shows that service card removed from the machine.
            elif SAVE_DATA in lavazza_cfds_mb_io_handler_variable.lcd_data:
                lavazza_cfds_mb_io_handler_variable.machine_state = READY_TO_DISPENSE_STATE
                lavazza_cfds_mb_io_handler_variable.service_card_state = DISABLE

            # Machine error state handling.
            elif [error_state for error_state in ERROR_STATES if error_state in lavazza_cfds_mb_io_handler_variable.lcd_data]:
                if lavazza_cfds_mb_io_handler_variable.machine_state == DISPENSING_STATE:
                    dispense_completion_state = True
                lavazza_cfds_mb_io_handler_variable.machine_state = MACHINE_ERROR_STATE
                logging.info("Lcd_Output_Reader : Machine in the error state")

            # If we didn't get the Ready string after the DISPENSING_STATE, it shows that machine is in the error state.
            elif lavazza_cfds_mb_io_handler_variable.machine_state == DISPENSING_STATE:
                dispense_completion_state = True
                lavazza_cfds_mb_io_handler_variable.machine_state = MACHINE_ERROR_STATE
                logging.info("Lcd_Output_Reader : Machine in the error state while dispensing")

            else:
                logging.warning("Lcd_Output_Reader : Machine state out of scope")
                # UNKNOWN_STATE is the state which is not handled by the lcd_output_reader.
                lavazza_cfds_mb_io_handler_variable.machine_state = UNKNOWN_STATE

            logging.debug("Lcd_Output_Reader : Machine_state - {}".format(lavazza_cfds_mb_io_handler_variable.machine_state))
            logging.debug("Lcd_Output_Reader : Foamer_state - {}".format(lavazza_cfds_mb_io_handler_variable.foamer_state))
            logging.debug("Lcd_Output_Reader : dispense_completion_status - {}".format(dispense_completion_state))

            return SUCCESS

        else:
            logging.warning("Lcd_Output_Reader : Lcd_data size mismatching")
            return FAILURE

    except Exception as error:
        logging.exception("Lcd_Output_Reader : {}".format(error))
        return FAILURE


def lcd_output_reader_handler(lcd_data):
    try:
        global dispense_completion_state
        # Get the current state of the Machine
        if lcd_output_reader(lcd_data) == FAILURE:
            raise Exception("Lcd_Output_Reader : lcd_output_reader error")

        logging.debug("Lcd_Output_Reader : key_simulation_caller - {}".format(
            lavazza_cfds_mb_io_handler_variable.key_simulation_caller))

        # We have to send the dispense completion status for the Mobile app dispensation.
        if dispense_completion_state and lavazza_cfds_mb_io_handler_variable.key_simulation_caller == MOBILE_APP_ID:
            lavazza_cfds_mb_io_handler_variable.key_simulation_caller = None
            mobile_app_event_trigger_data["event_data"] = lavazza_cfds_mb_io_handler_variable.machine_state
            trigger_event_handler_framework(mobile_app_event_trigger_data)
            logging.info("Lcd_Output_Reader : dispense_completion_status sent successfully")

        # We are not handling the lcd_data which are all coming in the service inserted state.
        # Other than the service card inserted state, we need to allow the user key simulation by changing
        # the current machine into READY_TO_DISPENSE_STATE.
        if lavazza_cfds_mb_io_handler_variable.machine_state == UNKNOWN_STATE and \
                not lavazza_cfds_mb_io_handler_variable.service_card_state:
            lavazza_cfds_mb_io_handler_variable.machine_state = READY_TO_DISPENSE_STATE

        # Machine_ready_event is used to know whether the Machine is ready for dispensing or not for Mobile App.
        # We should enable this while machine is in the READY_TO_DISPENSE_STATE.
        if lavazza_cfds_mb_io_handler_variable.machine_state in USER_KEY_SIMULATION_ALLOWED_STATES:
            mb_io_handler_system_resources["machine_ready_event"].set()
            # We should disable the service card state while machine in the user key simulation allowed states.
            if lavazza_cfds_mb_io_handler_variable.service_card_state != DISABLE:
                lavazza_cfds_mb_io_handler_variable.service_card_state = DISABLE

        # We should disable this while machine is not in the READY_TO_DISPENSE_STATE and service card inserted state.
        else:
            mb_io_handler_system_resources["machine_ready_event"].clear()

        logging.debug("Lcd_Output_Reader : machine_ready_event - {}".format(
            mb_io_handler_system_resources["machine_ready_event"].isSet()))
        logging.debug("Lcd_Output_Reader : Service_card_state - {}".format(
            lavazza_cfds_mb_io_handler_variable.service_card_state))

        # Notify the input key handler about the lcd_data change.
        if lavazza_cfds_mb_io_handler_variable.key_simulation_state == ENABLE:
            mb_io_handler_system_resources["lcd_display_event"].set()
            logging.info("Lcd_Output_Reader : lcd_display_event set successfully")

        if DEVICE_TYPE != PANTRY_TYPE:
            # Send the new lcd string and dispense_completion_status to the gui.
            user_interface_controller({"msg_type": TC_TEXT_MESSAGE_TYPE_ID,
                                       "msg": lavazza_cfds_mb_io_handler_variable.lcd_data,
                                       "dispense_completion_status": dispense_completion_state})

    except Exception as error:
        logging.exception("Lcd_Output_Reader : lcd_output_reader_handler - {}".format(error))

    finally:
        # Disabling the dispense_completion_state. This variable used to send the dispense_completion_status
        # to the mobile app server and disable the popup in the GUI.
        dispense_completion_state = False


# Read the data from the uart interface.
def pi_uart_reader():
    try:
        # We need to flush the uart buffer before read it. it will get rid of us from the unwanted data
        ser.reset_input_buffer()
        logging.info("Lcd_Output_Reader : UART_Reader - Waiting for the lcd data")

        # read the data from the uart buffer using serial library.
        # ser.read() is a blocking call. But, We are using timeout for the serial interface.
        # So, ser.read() will getting unblocked once the data came or the timeout occurred.
        # Here, It will read only the first byte of the data.
        received_data = ser.read()
        # Given some time allowance before reading a remaining data.
        sleep(WAIT_TIME_BEFORE_READING_REMAINING_UART_DATA)
        # ser.inWaiting() gives no of remaining bytes in the uart buffer.
        data_left = ser.inWaiting()
        # read the remaining bytes.
        received_data += ser.read(data_left)
        # ser.read() gives data in the bytes format. so, we need to decode it to get the string.
        # Here we use cp932 format for decoding. Because, lcd uses japanese encoding standard.
        # We use rstrip() function to remove the line feeder.
        logging.debug("Lcd_Output_Reader : UART received_data - {}".format(received_data))
        received_data = (received_data.decode('cp932')).rstrip("\r\n")

        return received_data

    except Exception as error:
        logging.exception("Lcd_Output_Reader : UART_Reader - {}".format(error))


# It is a callback function for the interrupt
def interrupt_handler(channel):
    # It indicates the uart_access_lock state, whether it is in the acquired state or released state
    uart_access_lock_state = False
    try:
        logging.info("Lcd_Output_Reader : Interrupt occurred")

        # Using lock to avoid race condition at the uart access.
        mb_io_handler_system_resources["/uart_access_lock"].acquire(LOCK_ACQUIRE_TIME_OUT)
        logging.info("Lcd_Output_Reader : uart_access_lock acquired")
        uart_access_lock_state = True

        # read the lcd_data using uart
        received_data = pi_uart_reader()

        # There may any problem occur in the pi_uart_reader. So, we need to check whether we get data or not.
        if received_data:
            lcd_output_reader_handler(received_data)
        else:
            logging.warning("Lcd_Output_Reader : Interrupt_handler - Didn't received any data from the UART")

    except Exception as error:
        logging.exception("Lcd_Output_Reader : Interrupt_handler - {}".format(error))

    finally:
        # We are using counting semaphore for the lock. So, we need to maintain it's lock count as 1.
        # Every release call increases it's lock count by 1.
        # So, we need to release the lock only if we were acquired it.
        if uart_access_lock_state:
            mb_io_handler_system_resources["/uart_access_lock"].release()
            logging.info("Lcd_Output_Reader : uart_access_lock released")


# initialization function for lcd_output_reader by Motherboard_IO_Handler
def init_lcd_output_reader(system_resources):
    try:
        global mb_io_handler_system_resources, gui_event_trigger_data, mobile_app_event_trigger_data
        # Get the mb_io_handler_system_resources for the inter process communication
        mb_io_handler_system_resources = system_resources
        logging.debug("Lcd_Output_Reader : mb_io_handler_system_resources - {}".format(mb_io_handler_system_resources))

        # Initializing the machine state and machine ready event
        lavazza_cfds_mb_io_handler_variable.machine_state = READY_TO_DISPENSE_STATE
        mb_io_handler_system_resources["machine_ready_event"].set()
        logging.info("Lcd_Output_Reader : Machine state and Machine ready event initialized successfully")

        # set the iot board configuration to get the lcd data from the motherboard
        lcd_reader_status = iot_board_handler(MB_CONTROL_LCD_DISPLAY_CMD)
        logging.debug("Lcd_Output_Reader : Lcd_reader_status - {}".format(lcd_reader_status))

        if DEVICE_TYPE != PANTRY_TYPE:
            # gui_event_trigger_data is used to communicate with the gui
            gui_event_trigger_data = {"thread_name": "lcd_output_reader",
                                      "event": mb_io_handler_system_resources["backend_to_gui_event"],
                                      "queue": mb_io_handler_system_resources["/backend_to_gui_queue"],
                                      "event_data": None,
                                      "finished_event": mb_io_handler_system_resources["backend_to_gui_finished_event"],
                                      "response_required": False}
            logging.debug("Lcd_Output_Reader : gui_event_trigger_data - {}".format(gui_event_trigger_data))

        # mobile_app_event_trigger_data is used send the dispense completion status to the mobile app server
        mobile_app_event_trigger_data = {"thread_name": "lcd_output_reader",
                                         "event": mb_io_handler_system_resources["dispense_completion_event"],
                                         "queue": mb_io_handler_system_resources["/mobile_app_queue"],
                                         "event_data": None,
                                         "finished_event": None,
                                         "response_required": False}
        logging.debug("Lcd_Output_Reader : mobile_app_event_trigger_data - {}".format(mobile_app_event_trigger_data))

        # Get the initial lcd string
        lcd_data = iot_board_handler(GET_LCD_STRING_CMD)
        logging.debug("Lcd_Output_Reader : Initial lcd_data - {}".format(lcd_data))

        # We need to call the lcd_output_reader to analyze the lcd_data.
        if len(lcd_data) == LCD_DATA_SIZE:
            lcd_output_reader_handler(lcd_data)
        else:
            lcd_output_reader(lcd_data[0:32])

        return SUCCESS

    except Exception as error:
        logging.exception("Lcd_Output_Reader : {}".format(error))
        return FAILURE

