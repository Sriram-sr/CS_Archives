"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_service_management_macros.py
 * Version        : 1.1
 * Date           : APRIL 20 2021
 *
 * Copyright (C) mieuPro Systems, 2021
 *
 ******************************************************************************
 """

import os

BASE_DIR = os.path.abspath("../../../") + "/"
COMMON_CODE_FILE_PATH = BASE_DIR + "src/source_code/common_code/"

SERVICE_MANAGER_SERVICE = "lavazza_cfds_service_management.service"
SERVER_COMMUN_SERVICE = "lavazza_cfds_server_communication.service"
SERVER_COMMUN_FILE_PATH = BASE_DIR + "src/source_code/features/SERVER_COMMUNICATION/"

# System commands
SYSTEMCTL_SERVICE_START_COMMAND = "systemctl start "
SYSTEMCTL_SERVICE_STOP_COMMAND = "systemctl stop "
REBOOT_COMMAND = "reboot"
SHUTDOWN_COMMAND = "poweroff"

# msg_type
REBOOT = "reboot"
SHUTDOWN = "shutdown"

# Initialized threads file macros
INITIALIZED_SERVICES_FILE_INITIAL_DATA = {"services": [], "no_of_services": 0}
INITIALIZED_SERVICES_CHECK_INTERVAL = 3
MAX_NO_OF_CHECK = 10
