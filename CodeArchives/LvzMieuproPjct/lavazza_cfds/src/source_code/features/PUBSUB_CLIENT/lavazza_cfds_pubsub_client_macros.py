# common code directory
import os
import sys

BASE_DIRECTORY = os.path.abspath("../../../../") + "/"
COMMON_CODE_FILE_PATH = BASE_DIRECTORY + "src/source_code/common_code/"
MOBILE_APP_FILE_PATH = BASE_DIRECTORY + "src/source_code/features/MOBILE_APP_SERVER/"

sys.path.insert(1, COMMON_CODE_FILE_PATH)
from lavazza_cfds_common_macros import *
from lavazza_cfds_common_apis import *

# Time interval for sync pull of data from pubsub
INTERVAL_FOR_SYNC_PULL = 2

# DB file path
RECENT_MSG_IDS_DB_FILE = BASE_DIRECTORY + 'tmp/recent_msg_ids.db'

# Maximum recent message ids to maintain
MAX_RECENT_MSG_IDS = 10

# Pull type
ASYNC_PULL_TYPE = "async"
SYNC_PULL_TYPE = "sync"

PUBSUB_CLIENT_SERVICE = "lavazza_cfds_pubsub_client.service"
