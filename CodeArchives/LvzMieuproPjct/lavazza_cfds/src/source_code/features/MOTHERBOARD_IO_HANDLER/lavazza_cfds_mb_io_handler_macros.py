"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_mb_io_handler_macros.py
 * Version        : 1.0
 * Date           : August 10 2020
 *
 * Copyright (C) mieuPro Systems, 2020
 *
 ******************************************************************************
 """

import os
from sys import path

BASE_DIRECTORY = os.path.abspath("../../../../") + "/"
COMMON_CODE_FILE_PATH = BASE_DIRECTORY + "src/source_code/common_code/"

path.append(COMMON_CODE_FILE_PATH)
from lavazza_cfds_common_apis import *

device_info = {}
# read the DEVICE_PROVISION_INFO_FILE to get the device type info
if read_from_file(device_info, DEVICE_PROVISION_INFO_FILE) == FAILURE:
    raise Exception("File reading error in ", DEVICE_PROVISION_INFO_FILE)

DEVICE_TYPE = device_info['device_type']
MB_IO_HANDLER_SERVICE = "lavazza_cfds_motherboard_io_handler.service"
MB_IO_HANDLER_SERVICE_PRIORITY = -10

# Raspberry pi configuration
PRODUCT_KEY1 = 29
PRODUCT_KEY2 = 15
PRODUCT_KEY3 = 40
PRODUCT_KEY4 = 38
PRODUCT_KEY5 = 36
PRODUCT_KEY6 = 32
PRODUCT_KEY7 = 26
PRODUCT_KEY8 = 22

FUNCTION_KEY1 = 37  # decaff / +
FUNCTION_KEY2 = 35  # mill change / -
FUNCTION_KEY3 = 33  # double cup
FUNCTION_KEY4 = 31  # rinse

INTERRUPT_KEY = 18
SYNC_0_KEY = 12
SYNC_1_KEY = 16
IOT_BOARD_RESET_KEY = 13

# Input key handler macros
PRODUCT_KEYS = [PRODUCT_KEY1, PRODUCT_KEY2, PRODUCT_KEY3, PRODUCT_KEY4,
                PRODUCT_KEY5, PRODUCT_KEY6, PRODUCT_KEY7, PRODUCT_KEY8]

FUNCTION_KEYS = [FUNCTION_KEY1, FUNCTION_KEY2, FUNCTION_KEY3, FUNCTION_KEY4]

FOAMER = 1
COUNT_READING = 2
# CONFIG_BACK and RESET_MODE are used only at the service card inserted state
RESET_OR_CONFIG_BACK_MODE = 3
COFFEE_UNIT_CLEANING_ID = 4
MILK_UNIT_CLEANING_ID = 5
COFFEE_AND_MILK_UNIT_CLEANING_ID = 6
EXCESS_MILK_CLEANING_WATER_REMOVAL = 7
GPIO_RESET = 8

COUNT_READING_KEYS = [FUNCTION_KEY2, FUNCTION_KEY4]

COMBINED_KEY_PRESS_PAUSE_TIME = 0.25  # secs
KEY_PRESS_PAUSE_TIME = 0.1  # secs
MAX_SHORT_KEY_PRESS_SIMULATION_WAIT_TIME = 5  # secs
MAX_LONG_KEY_PRESS_SIMULATION_WAIT_TIME = 10  # secs

SEND_IOT_CMD_MAX_TRY = 3
SEND_IOT_CMD_RETRY_WAIT_TIME = 0.3  # secs

# UART configuration
UART_PORT = '/dev/ttyS0'
UART_BAUD_RATE = 9600
UART_READ_TIME_OUT = 5
WAIT_TIME_BEFORE_READING_REMAINING_UART_DATA = 0.1
INTERRUPT_BOUNCE_TIME = 500  # mill secs

# iot board synchronization commands
ENABLE_KEYPAD_CMD = ">K=1\n"
DISABLE_KEYPAD_CMD = ">K=0\n"
KEYPAD_STATUS_CMD = ">K=?\n"
MB_CONTROL_LCD_DISPLAY_CMD = ">D=1\n"
PI_CONTROL_LCD_DISPLAY_CMD = ">D=0\n"
PI_CONTROL_LCD_STRING_CMD = ">S=String\n"
GET_LCD_STRING_CMD = ">B=?\n"
CLEAR_BUFFER = "\r\n"

PRODUCT_DISPENSING_NAMES = ["Tea", "white C", "Cappuccino", "Espresso", "Milk", "Coffee",
                            "Coffee Sp", "Brewcoffee", "LMacchiato", "Ristretto"]

ERROR_STATES = ["Empty Drawer", "Drain tub", "Drawer missing", "Fill hopper", "Milk low", "Powder error",
                "Change filter", "Service required", "Clean appliance", "Flow error", "Piston error", "Overtime error",
                "NTC coffee def.", "NTC foamer def.", "Tension high/low", "Main switch", "Waterflowerror", "No water"]

USER_KEY_SIMULATION_WORKING_STATES = [DISPENSING_STATE, MILK_NOT_READY_STATE, ENABLE_FOAMER_ON]
USER_KEY_SIMULATION_ALLOWED_STATES = [READY_TO_DISPENSE_STATE, MILK_NOT_READY_STATE,
                                      ENABLE_FOAMER_ON, MACHINE_ERROR_STATE]

LCD_DATA_SIZE = 32
READY = "Ready"
RINSE = "Rinse                           "
PLEASE_WAIT = "Please wait"
FOAMER_OFF = "Foamer Off"
FOAMER_ON = "Foamer On"
SERVICE_CARD = "Service Card"
FOAMER_OFF_ERROR = "Foamer Off      Foamer Off      "
MILK_NOT_READY = "Milk not ready  Foamer On       "
COFFEE_UNIT_CLEANING = "Select          Coffee          "
MILK_UNIT_CLEANING = "Select          Milk            "
COFFEE_AND_MILK_UNIT_CLEANING = "Select          Coffee and Milk "
SAVE_DATA = "Save data"

NO_OF_KEY_SIMULATION_FOR_COFFEE_UNIT_CLEANING = 1
NO_OF_KEY_SIMULATION_FOR_MILK_UNIT_CLEANING = 2
NO_OF_KEY_SIMULATION_FOR_COFFEE_AND_MILK_UNIT_CLEANING = 3
