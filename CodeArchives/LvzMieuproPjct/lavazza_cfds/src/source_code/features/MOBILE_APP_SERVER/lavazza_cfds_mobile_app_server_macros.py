"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_mobile_app_server_macros.py
 * Version        : 1.1
 * Date           : APRIL 20 2021
 *
 * Copyright (C) mieuPro Systems, 2021
 *
 ******************************************************************************
 """

import os
import sys

cwd = os.getcwd()

#SRC_BASE_DIR = "/home/pi/lavazza_cfds/src/"
BASE_DIR = os.path.abspath("../../../../") + "/"

COMMON_CODE_FILE_PATH = BASE_DIR + "src/source_code/common_code"
AVAILABLE_WIFI=BASE_DIR+"tmp/available_wifi.json"

sys.path.append(COMMON_CODE_FILE_PATH)
from lavazza_cfds_common_apis import *

APP_SERVER = cwd + '/'

STATIC = APP_SERVER + "static/"
PWA_CONFIG_FILE = STATIC + "pwa_config.json"

TOKEN_HANDLER = APP_SERVER + "token_handler/"
PUBLIC_KEY = TOKEN_HANDLER + "jwt_key.pub"
PRIVATE_KEY = TOKEN_HANDLER + "jwt_key"

#ISSUER = "LaV@ZzA"
#TOKEN = "secret"

MOBILE_APP_TOKEN = "l@vA@zzacfd$"
PWA_TOKEN = "LaVaZzApWa"
MAX_REQ_PARAMS = 3 #seconds
MIN_QUEUE_LENTH = 1 #seconds
MIN_PER_USER_WAIT_TIME = 1
MIN_ORDER_NUM = 0
MAX_ORDER_NUM = 100
MAX_DISP_AND_CANC_ORDERS_CLEAN_WAIT_TIME = 90 #seconds
MIN_GUI_MESSAGE_CLEAN_TIME = 0.5 #seconds
MIN_NEXT_ORDER_DISP_TIME = 2 #seconds
ERROR_GUI_POP_UP_WAIT_TIME = 2.5 #seconds

HOST = '0.0.0.0'
PORT = 9876

# ORDER POSITIVE STATUS CODE
BEFORE_PLACING_ORDER = 0
PLEASE_WAIT = 1
ORDER_RECEIVED_OR_INQUEUE = 2
WAITING_TO_DISPENSE = 3
DISPENSING = 4
DISPENSED = 5

# ORDER ERROR STATUS CODE
SOMETHING_WENT_WRONG = 6
TIMEOUT_EXPIRED = 7
MACHINE_NOT_READY = 8
FOAMER_OFF = 9
RINSING = 10
MILK_NOT_READY = 11
MACHINE_DETAIL_MISMATCH = 12

# COMMON ERROR STATUS CODE
INVALID_TOKEN = 13
EXCEPTION_OCCURRED = 14
MACHINE_ERROR = 15

feature_configs = {}
if read_from_file(feature_configs,FEATURE_CONF_FILE) == FAILURE:
    raise Exception("Mobile App Server : Feature config File reading error")

SERVER_URL = feature_configs["server_info"]["server_url"]

# Product Dispense Error States
DISPENSE_ERROR_STATE = {ENABLE_FOAMER_ON: {"status": FOAMER_OFF,
                                            "display_msg":"Foamer is off \nPlease turn on the Foamer",
                                            "debug_msg":"foamer is disabled",
                                            "empty_dispense_queue_flag":False},

                        RINSE_STATE: {"status": RINSING,
                                       "display_msg":"Rinsing \nPlease try again shortly",
                                       "debug_msg":"machine is rinsing",
                                       "empty_dispense_queue_flag":False},

                        MILK_NOT_READY_STATE: {"status": MILK_NOT_READY,
                                               "display_msg": "Milk is not Ready \nPlease try after sometime",
                                               "debug_msg": "milk is not ready",
                                               "empty_dispense_queue_flag": False},

                        MACHINE_NOT_READY_STATE: {"status": MACHINE_NOT_READY,
                                                  "display_msg": "Machine is not Ready \nPlease try after sometime",
                                                  "debug_msg": "machine is not ready",
                                                  "empty_dispense_queue_flag": True},

                        FAILURE : {"status": MACHINE_NOT_READY,
                                    "display_msg": "Something went wrong \nPlease try after sometime",
                                    "debug_msg": "something went wrong",
                                    "empty_dispense_queue_flag": True},

                        MACHINE_ERROR_STATE : {"status": MACHINE_ERROR,
                                                "display_msg": "Machine Error Occured \nPlease try after sometime",
                                                "debug_msg": "machine error occured",
                                                "empty_dispense_queue_flag": True}
                        }


#Src Update Macros

UPDATE_CONFIG_FILE = APP_SERVER + "static/update_config.json"

PASS_STR = "qazwsxedcrfvtgb/yhnujmikolp/POLIKUJMYHN/TGBRFVEDCWSXQAZ/0123456789"

UPDATE_PATH = "/usr/lib/.lavazza_cfds"
TECH_ID = "!@V@ZZ@TECH"
TECH_PASS = "TECH456"
