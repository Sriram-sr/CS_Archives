import logging
import threading
import time

from lavazza_cfds_pubsub_client_macros import *

sys.path.insert(1, COMMON_CODE_FILE_PATH)
from lavazza_cfds_common_apis import read_from_file, initialize_service, update_process_id

import lavazza_cfds_pubsub_client_google_apis as google_apis

# Logging basic configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - Pubsub_Client - %(levelname)s - %(message)s',
                    filename=LAVAZZA_COMMON_LOG_FILE, filemode='a')

pubsub_client_system_resources = {}

# if __name__ == "__main__":
def main():

    try:
        if update_process_id("PUBSUB_CLIENT") == FAILURE:
            print("ERROR in updating process id ")

        # Initialize pubsub client
        if initialize_service(pubsub_client_system_resources, PUBSUB_CLIENT_SERVICE) == FAILURE:
            raise Exception("Pubsub Client initialization failed")
        logging.info("Pubsub Client service system_resources initialized successfully")

        device_provision_info = {}
        if read_from_file(device_provision_info, \
                          DEVICE_PROVISION_INFO_FILE) == FAILURE:
            logging.debug("DEVICE_PROVISION_INFO_FILE read error")
            return

        if device_provision_info["provision_status"]:
            utility_event_trigger_data = {"thread_name": "pubusub_client",
                                          "event": pubsub_client_system_resources["utility_event"],
                                          "queue": pubsub_client_system_resources["/utility_queue"],
                                          "event_data": None,
                                          "finished_event": None,
                                          "response_required": False}

            # Fetch subscription List from device provisipn json file
            device_provision_info = {}
            if read_from_file(device_provision_info, DEVICE_PROVISION_INFO_FILE) == FAILURE:
                logging.exception("Pubsub client init - Error in fetching subscription list")
                exit()

            pubsub_subscriptions = device_provision_info["pubsub_subscriptions"]
            logging.debug("Pubsub client init -  PUBSUB SUBSCRIPTIONS :: {} ".format(pubsub_subscriptions))

            # Split up the subscription list based on the types(sync and async)
            async_pull_subscriptions = []
            sync_pull_subscriptions = []

            for subscription in pubsub_subscriptions:
                if subscription["subscriptionType"] == ASYNC_PULL_TYPE:
                    async_pull_subscriptions.append(subscription)

                elif subscription["subscriptionType"] == SYNC_PULL_TYPE:
                    sync_pull_subscriptions.append(subscription)

            logging.info("Pubsub client init - async_pull_subscriptions :: {} ".format(async_pull_subscriptions))
            logging.info("Pubsub client init - sync_pull_subscriptions :: {} ".format(sync_pull_subscriptions))

            for subscription in sync_pull_subscriptions:

                try:
                    google_apis.pull_message_synchronously(subscription["topicName"], subscription["subscriptionName"],
                                                  subscription["projectId"], subscription["credentials"],
                                                  pubsub_client_system_resources,utility_event_trigger_data)

                except Exception as error:
                    logging.exception("Pubsub client init - sync message pull Error :: {} ".format(error))

            # Synchronous message pull from Google Cloud
            while True:

                if device_provision_info["network_mode"] == ORGANIZATION_WIFI:
                    network_config_file = WIFI_CONF_FILE
                    network_ket_status = "wifi_status"

                elif device_provision_info["network_mode"] == GSM:
                    network_config_file = GSM_CONF_FILE
                    network_ket_status = "gsm_status"

                network_info = {}

                if read_from_file(network_info, network_config_file) == FAILURE:
                    raise Exception("File reading error in " + network_config_file)

                network_status = network_info[network_ket_status]
                logging.debug("network_status {} - {}".format(network_ket_status, network_status))

                if network_status:

                    for async_subscription in async_pull_subscriptions:
                        try:
                            google_apis.pull_message_synchronously(async_subscription["topicName"], async_subscription["subscriptionName"],
                                                          async_subscription["projectId"], async_subscription["credentials"],
                                                          pubsub_client_system_resources,utility_event_trigger_data)

                        except Exception as error:
                            logging.exception("Pubsub client init - sync message pull Error :: {} ".format(error))
    
                time.sleep(INTERVAL_FOR_SYNC_PULL)

    except Exception as error:
        logging.exception("Pubsub client init - : {} ".format(error))

main()
