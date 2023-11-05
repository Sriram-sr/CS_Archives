
"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_diagnostics_macros.py
 * Version        : 1.0
 * Date           : May 4 2020
 *
 * Copyright (C) mieuPro Systems, 2020
 *
 ******************************************************************************
 """

import sys,os
#BASE_DIRECTORY = "/home/pi/lavazza_cfds/"
BASE_DIRECTORY = os.path.abspath("../../../../") +  "/"

COMMON_CODE_PATH =BASE_DIRECTORY+"src/source_code/common_code/"
sys.path.insert(1, COMMON_CODE_PATH)
from lavazza_cfds_common_apis import *
from lavazza_cfds_common_macros import *

