"""
 ******************************************************************************
 *
 * File Name      : lavazza_utility_keep_alive_handler_macros.py
 * Version        : 1.1
 * Date           : MAY 04 2021
 *
 * Copyright (C) mieuPro Systems, 2021
 *
 ******************************************************************************
 """

GET_NTP_MESSAGE_CMD = "timedatectl show-timesync | grep NTPMessage"
CPU_IDLE_TIME_CMD = "iostat | awk 'NR==4{print $6 }'"
AVAILABLE_MEMORY_CMD = "free -m | awk 'NR==2{print $7}'"
TOTAL_MEMORY_CMD = "free -m | awk 'NR==2{print $2}'"

NTP_MESSAGE_DATETIME_STRING_STARTING_INDEX = 25
NTP_MESSAGE_DATETIME_STRING_ENDING_INDEX = 44

KEEP_ALIVE_SERVER_PATH = "/keepAlive"
PROVISION_UPDATE_SERVER_PATH = "/updateDeviceModes"