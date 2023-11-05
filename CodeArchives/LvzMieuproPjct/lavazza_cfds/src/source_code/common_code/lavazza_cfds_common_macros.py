"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_common_macros.py
 * Version        : 1.1
 * Date           : JULY 24 2021
 *
 * Copyright (C) mieuPro Systems, 2021
 *
 ******************************************************************************
 """

import os
import json
from filelock import FileLock

# Configuration file path
current_file_path = os.path.abspath(__file__)
current_file_path_as_list = current_file_path.split('/')
del current_file_path_as_list[-4:]
BASE_DIR = "/".join(current_file_path_as_list) + "/"


FEATURE_CONF_FILE = BASE_DIR + "src/configs/feature_configs/feature_configs.json"

# File contains details about all the service of the application
SERVICE_DETAILS_FILE = BASE_DIR + "src/configs/feature_configs/service_details.json"

DEVICE_CONF_DIR = BASE_DIR + "src/configs/device_configs/"
DEVICE_PROVISION_INFO_FILE = DEVICE_CONF_DIR + "device_provision_info.json"
PRODUCT_NAME_CONFIG_FILE = DEVICE_CONF_DIR + "product_details.json"
DEV_TYPE_CONFIG_FILE = DEVICE_CONF_DIR + "dev_type.json"
WIFI_CONF_FILE = DEVICE_CONF_DIR + "wifi_config.json"
GSM_CONF_FILE = DEVICE_CONF_DIR + "gsm_config.json"

TMP_DIRECTORY_PATH = BASE_DIR + "tmp/"
UPLOAD_DATA_LIST_FILE = TMP_DIRECTORY_PATH + "upload_data_list.json"
COUNTER_DATA_FILE = TMP_DIRECTORY_PATH + "counter_data.json"
KEEP_ALIVE_FILE = TMP_DIRECTORY_PATH + "keep_alive.json"
VERSION_SYNC_DATA_FILE = TMP_DIRECTORY_PATH + "version_sync.json"
INITIALIZED_SERVICES_FILE = TMP_DIRECTORY_PATH + "initialized_services.json"
QR_CODE_IMAGE = TMP_DIRECTORY_PATH + "qr_code.png"

MB_IO_HANDLER_FILE_PATH = BASE_DIR + "src/source_code/features/MOTHERBOARD_IO_HANDLER"
RESOURCES_FILE_PATH = BASE_DIR + "src/resources"

WPA_CONFIG_FILE = "/etc/wpa_supplicant/wpa_supplicant.conf"
HOTSPOT_CONF_FILE = "/etc/hostapd/hostapd.conf"
DHCPCD_CONF_FILE = "/etc/dhcpcd.conf"
INTERFACE_CONF_FILE = "/etc/network/interfaces"
HOSTAPD_CONF_FILE = "/etc/default/hostapd"

# LOG FILES
LAVAZZA_COMMON_LOG_FILE = BASE_DIR + "logs/lavazza.log"
DETAILED_LOG = BASE_DIR + "/logs/detailed_diagnostics_log.json"
DETAILED_LOG_BACKUP = BASE_DIR + "/logs/detailed_diagnostics_log_backup.json"
SUMMARY_LOG = BASE_DIR + "/logs/summary_diagnostics_log.json"
SUMMARY_LOG_BACKUP = BASE_DIR + "/logs/summary_diagnostics_log_backup.json"

PROCESS_IDS_FILE = TMP_DIRECTORY_PATH + "process_ids.json"

# URL strings
HTTPS = "http://"
COLON = ":"

# response codes of rest call
HTTP_SUCCESS_STATUS_CODE = 200

# rest call token
TOKEN = "l@v@zz@_m!3upr0"

# Server
CONFIGURATION_SERVER = "configuration_server"
KEEP_ALIVE_SERVER = "keep_alive_server"
COUNTER_DATA_SERVER = "counter_data_server"

MAX_MACHINE_READY_EVENT_WAIT_TIME = 45  # secs
MAX_ORDER_DISPENSE_WAIT_TIME = 45  # seconds

SEMAPHORE_INITIAL_VALUE = MSG_QUEUE_SIZE = 1
MSG_QUEUE_TIME_OUT = 20 # 20 secs
FINISHED_EVENT_TIME_OUT = 30  # secs
LOCK_ACQUIRE_TIME_OUT = 30  # secs

ENABLE = True
DISABLE = False

# Function return values
SUCCESS = 0
FAILURE = -1

# Machine types
PANTRY_TYPE = "Pantry-Type"
RETRO_FIT_TYPE = "Retrofit-Type"
PRONTO_BAR_TYPE = "Pronto_bar_Type"

# MESSAGE TYPES
TC_TEXT_MESSAGE_TYPE_ID = 1  # tech console display
ENABLE_POP_UP_MESSAGE_TYPE_ID = 2  # popup_msg_enable
DISABLE_POP_UP_MESSAGE_TYPE_ID = 3  # popup_msg_enable
SHUTDOWN_MESSAGE_TYPE_ID = 4  # device_shutdown
APPLICATION_RESET_MESSAGE_TYPE_ID = 5  # device_reboot
INIT_PROVISION_MESSAGE_TYPE_ID = 6  # initiate_provision
PRODUCT_NAME_MESSAGE_TYPE_ID = 7  # save the product names
DEVICE_INFO_MESSAGE_TYPE_ID = 8  # save ssid and password
REBOOT_MESSAGE_TYPE_ID = 9  # reboot the the machine
UPDATE_NUMBER_OF_STATION_MESSAGE_TYPE_ID = 1010

WIFI_INFO_MESSAGE_TYPE_ID = 11
WIFI_STATUS_MESSAGE_TYPE_ID = 12  # "wifi_status"
UPDATE_WIFI_MESSAGE_TYPE_ID = 13
WIFI_AVAILABILITY_MESSAGE_TYPE_ID = 14  # "wifi_availability"
CONNECT_WIFI_MESSAGE_TYPE_ID = 15  # "test_wifi"
WIFI_CONFIG_MESSAGE_TYPE_ID = 16  # "wifi_config"
RESET_WIFI_CONFIG_FILE_MSG_TYPE_ID = 30
GET_DEVICE_ID_MESSAGE_TYPE = 17  # "get_device_id"
SITE_SPECIFIC_MESSAGE_TYPE_ID = 18  # "site_specific_device_info"

GSM_INFO_MESSAGE_TYPE_ID = 19
GSM_AVAILABILITY_MESSAGE_TYPE_ID = 20  # "gsm_availability"
GSM_STATUS_MESSAGE_TYPE_ID = 21  # "test_gsm"
GSM_CONFIG_MESSAGE_TYPE_ID = 22  # "gsm_config"

DEVICE_MODE_UPDATE_MESSAGE_TYPE_ID = 23
QR_CODE_UPDATE_STATUS_MESSAGE_TYPE_ID = 24  # "QR code update"

# CALLER_ID
USER_CALLER_ID = 1
ADMIN_CALLER_ID = 2
TECHNICIAN_CALLER_ID = 3
MOBILE_APP_ID = 4
INPUT_KEY_HANDLER_ID = 5
GUI_CONTROLLER_ID = 6
COUNT_READER_ID = 7
IOT_COUNT_READER = 8

# Machine states ID
READY_TO_DISPENSE_STATE = 1
DISPENSING_STATE = 2
RINSE_STATE = 3
ENABLE_FOAMER_ON = 4
MILK_NOT_READY_STATE = 5
MACHINE_NOT_READY_STATE = 6
DISABLE_SERVICE_CARD = 7
MACHINE_ERROR_STATE = 8
UNKNOWN_STATE = 9

MAX_PRODUCT_COUNT = 8

# DEVICE MODES
INTERNET_MODE = "Inter_Mode"
INTRANET_MODE = "Intra_Mode"

# NETWORK MODES
ORGANIZATION_WIFI = "Corp_Wi-Fi"
MACHINE_WIFI = "Device_Wi-Fi"
GSM = "Gsm"

with FileLock(FEATURE_CONF_FILE + ".lock"):
    with open(FEATURE_CONF_FILE) as f:
        feature_configs = json.load(f)
        LOG_LEVEL = feature_configs['other_parameters']['log_level']
        
print("LOG_LEVEL =", LOG_LEVEL)


