"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_utility_macros.py
 * Version        : 1.1
 * Date           : APRIL 20 2021
 *
 * Copyright (C) mieuPro Systems, 2021
 *
 ******************************************************************************
 """

import sys
import os

BASE_DIRECTORY = os.path.abspath("../../../../") +  "/"
COMMON_CODE_PATH = BASE_DIRECTORY+"src/source_code/common_code/"
sys.path.insert(1, COMMON_CODE_PATH)
from lavazza_cfds_common_apis import *
from lavazza_cfds_common_macros import *

DENY_INTERFACES = 'denyinterfaces wlan0'
ALLOW_INTERFACE = 'auto lo\niface lo inet loopback\n\nauto eth0\niface eth0 inet dhcp\n\nallow-hotplug wlan0\niface wlan0 inet static\n    address 192.168.5.1\n    netmask 255.255.255.0\n    network 192.168.5.0\n    broadcast 192.168.5.255'
HOSTAPD_ENABLE = 'DAEMON_CONF="/etc/hostapd/hostapd.conf"'
ENABLE_CMD = 'systemctl enable hostapd.service'
DISABLE_CMD = 'systemctl disable hostapd.service'
utility_system_events_queues = {}
feature_configs = {}
