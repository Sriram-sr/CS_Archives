import os
from sys import path

BASE_DIRECTORY = os.path.abspath("../../../../") + "/"
COMMON_CODE_FILE_PATH = BASE_DIRECTORY + "src/source_code/common_code/"

DEVICE_MONITOR_FILE = BASE_DIRECTORY + "src/configs/device_configs/device_monitor.json"
path.append(COMMON_CODE_FILE_PATH)
from lavazza_cfds_common_apis import *

device_info = {}

DEVICE_TYPE = None
SERVER_COMMUNICATION_SERVICE = "lavazza_cfds_server_communication.service"
WIFI_STATUS_CHECK_INTERVAL = 60  # Secs
MAX_WIFI_WAIT_TIME = 5  # minutes
UPLOAD_DATA_LIST_FILE_INITIAL_DATA = {"no_of_items": 0, "items": [], "run_time_entries": []}

RETRY_INTERVAL = 60
RETRY_POLL_INTERVAL = 86400

VERSION_SYNC_SERVER_PATH = "/versionSync"

HOSTS = ["www.google.com", "www.apple.com", "www.microsoft.com"]
ROUTE_FILE = "/proc/net/route"

PORT = 80

MIN_TIME_TO_IFACE_ON = 5
MIN_TIME_TO_IFACE_OFF = 2

AVAILABLE_WIFI_LIST_CMD = ' sudo iwlist wlan0 scanning | grep ESSID '
AVAILABLE_WIFI_FILE = BASE_DIRECTORY + "tmp/available_wifi.json"
WIFI_INTERFACE_NAME = "wlan0"
GSM_INTERFACE_NAME = "usb0"
GET_WIFI_ENABLE_STATUS_CMD = " ifconfig | grep 'wlan0' "
WIFI_ON_CMD = "rfkill unblock wifi"
WIFI_OFF_CMD = "rfkill block wifi"
WIFI_RECONNECT_CMD = 'sudo wpa_cli -i wlan0 reconfigure'
GET_IPADDRESS_CMD = "ifconfig wlan0 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'"
WPA_CONFIG_DATA = "ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\ncountry=GB\n"

MIN_TIME_TO_WIFI_CONNECT = 1
MIN_TIME_TO_WIFI_RECONNECT = 35

GSM_CONNECTION_FILE = '/etc/ppp/peers/gsm_connection'
GSM_ON_CMD = "sudo pon gsm_connection"
GSM_OFF_CMD = "sudo poff gsm_connection"
