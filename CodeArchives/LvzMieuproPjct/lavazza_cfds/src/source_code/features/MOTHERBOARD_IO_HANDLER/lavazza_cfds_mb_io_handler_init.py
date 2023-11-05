"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_mb_io_handler_init.py
 * Version        : 1.0
 * Date           : August 10 2020
 *
 * Copyright (C) mieuPro Systems, 2020
 *
 ******************************************************************************
 """

# RPi.GPIO library used to accessing GPIO pins
import RPi.GPIO as GPIO

import lavazza_cfds_input_key_handler
import lavazza_cfds_lcd_output_reader
from lavazza_cfds_mb_io_handler_macros import *

logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - Motherboard_IO_Handler - %(levelname)s - %(message)s',
                    filename=LAVAZZA_COMMON_LOG_FILE, filemode='a')

mb_io_handler_system_resources = {}


# Msg queue handler for the Mother board IO operations.
def mb_io_queue_handler(event_data):
    try:
        response = None

        # INPUT_KEY_HANDLER_ID is used for the input key simulation.
        if event_data["service"] == INPUT_KEY_HANDLER_ID:
            response = lavazza_cfds_input_key_handler.key_press_input_queue_handler(event_data["data"])
        # GUI_CONTROLLER_ID is used to send the msg to GUI.
        elif event_data["service"] == GUI_CONTROLLER_ID:
            response = lavazza_cfds_lcd_output_reader.user_interface_controller(event_data["data"])
        # Invalid request handling.
        else:
            logging.warning("mb_io_queue_handler - Invalid request")

        # If there is any response, send it to the requested service.
        if response is not None:
            logging.info("mb_io_queue_handler - Response - {}. Sending response to the caller.".format(response))
            return response

    except Exception as error:
        logging.exception("mb_io_queue_handler : {}".format(error))


# GPIO pin Setup for the product and function keys in the raspberry pi
def setup_pi_gpio():
    try:
        # The GPIO.BOARD option specifies that we are referring to the pins by the number of the pin the the plug -
        # i.e the numbers printed on the board
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(PRODUCT_KEY1, GPIO.OUT)
        GPIO.setup(PRODUCT_KEY2, GPIO.OUT)
        GPIO.setup(PRODUCT_KEY3, GPIO.OUT)
        GPIO.setup(PRODUCT_KEY4, GPIO.OUT)
        GPIO.setup(PRODUCT_KEY5, GPIO.OUT)
        GPIO.setup(PRODUCT_KEY6, GPIO.OUT)
        GPIO.setup(PRODUCT_KEY7, GPIO.OUT)
        GPIO.setup(PRODUCT_KEY8, GPIO.OUT)

        GPIO.setup(FUNCTION_KEY1, GPIO.OUT)
        GPIO.setup(FUNCTION_KEY2, GPIO.OUT)
        GPIO.setup(FUNCTION_KEY3, GPIO.OUT)
        GPIO.setup(FUNCTION_KEY4, GPIO.OUT)

        GPIO.setup(INTERRUPT_KEY, GPIO.IN)
        GPIO.setup(SYNC_0_KEY, GPIO.OUT)
        GPIO.setup(SYNC_1_KEY, GPIO.OUT)
        GPIO.setup(IOT_BOARD_RESET_KEY, GPIO.OUT)

        # Set the callback function for the interrupt.
        GPIO.add_event_detect(INTERRUPT_KEY, GPIO.RISING, callback=lavazza_cfds_lcd_output_reader.interrupt_handler,
                              bouncetime=INTERRUPT_BOUNCE_TIME)

        return SUCCESS

    except Exception as error:
        logging.exception("setup_pi_gpio : {}".format(error))
        return FAILURE


# Starting function of the Mother board IO Handler service.
def motherboard_io_handler_start():
    logging.info("Motherboard_IO_Handler : Motherboard_IO_Handler process started")

    # Register the MOTHERBOARD_IO_HANDLER to the Diagnostics module to know the run time errors.
    if update_process_id("MOTHERBOARD_IO_HANDLER") == FAILURE:
        logging.exception("Error in update_process_id")

    logging.info("PID : {}".format(os.getpid()))
    # Changing priority of the service. It will increase the performance of the service.
    logging.info("Priority : {}".format(os.nice(MB_IO_HANDLER_SERVICE_PRIORITY)))

    if setup_pi_gpio() == FAILURE:
        raise Exception("setup_pi_gpio failed")
    logging.info("Pi GPIO setup completed")

    # Initializing the MB_IO_HANDLER_SERVICE.
    if initialize_service(mb_io_handler_system_resources, MB_IO_HANDLER_SERVICE) == FAILURE:
        raise Exception("Motherboard io handler initialization failed")
    logging.info("Motherboard io handler service system_resources initialized successfully")

    # Initialize the Lcd Output Reader module.
    if lavazza_cfds_lcd_output_reader.init_lcd_output_reader(mb_io_handler_system_resources) == FAILURE:
        raise Exception("Lcd_Output_Reader initialization failed")
    logging.info("Lcd_Output_Reader initialized successfully")

    # Initialize the Input Key Handler module.
    if lavazza_cfds_input_key_handler.init_input_key_handler(mb_io_handler_system_resources) == FAILURE:
        raise Exception("Input_Key_Handler initialization failed")
    logging.info("Input_Key_Handler initialized successfully")

    mb_io_event_handler_data = {"thread_name": "MB_IO_Handler",
                                "event": mb_io_handler_system_resources["mb_io_event"],
                                "queue": mb_io_handler_system_resources["/mb_io_queue"],
                                "queue_handler_function": mb_io_queue_handler,
                                "finished_event": mb_io_handler_system_resources["mb_io_finished_event"]}

    while True:
        try:
            event_handler_framework(mb_io_event_handler_data)

        except Exception as error:
            logging.exception("Motherboard_IO_Handler : {}".format(error))


motherboard_io_handler_start()
