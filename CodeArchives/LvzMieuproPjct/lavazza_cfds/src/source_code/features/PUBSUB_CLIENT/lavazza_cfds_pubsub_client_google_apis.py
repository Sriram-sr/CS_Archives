import datetime
import json
import sqlite3
import logging
from google.cloud import pubsub_v1
from google.oauth2 import service_account
from google.auth import jwt
from google.api_core import retry
import time
from lavazza_cfds_pubsub_client_macros import *
from lavazza_cfds_common_apis import trigger_event_handler_framework


##sys.path.insert(1, MOBILE_APP_FILE_PATH)
##import lavazza_cfds_pubsub_dispense_queue_handler
#import append_dispense_queue, dispense_permission_event_handler

def check_msg_duplication(current_msg_id, subscription):
    """Check for duplication of received messages"""
    # Establishing db connection
    sqlite_connection = sqlite3.connect(RECENT_MSG_IDS_DB_FILE)
    cursor = sqlite_connection.cursor()

    # Maintain most recent received msg ids(say last 10 ids) to avoid duplication of  message delivery
    # create table if not exist
    cursor.execute("create table IF NOT EXISTS " + subscription + "  ( recent_msg_ids TEXT PRIMARY KEY,time TEXT )")
    sqlite_connection.commit()

    # fetch most recent msg ids from db
    recent_msg_ids = cursor.execute(
        " select recent_msg_ids from " + subscription).fetchall()

    # convert the recent_msg ids to list
    recent_msg_id_list = []
    if recent_msg_ids:
        for message_id in recent_msg_ids:
            recent_msg_id_list.append(message_id[0])

    # check for duplication
    if current_msg_id in recent_msg_id_list:
        logging.debug("Dup msg check - Already Received message...Ignoring Duplicate msg")
        cursor.close()
        sqlite_connection.close()
        return True

    else:
        logging.debug("Dup msg check - New Message Arrived")
        if len(recent_msg_id_list) >= MAX_RECENT_MSG_IDS:
            cursor.execute("delete from " + subscription + " order by time ASC LIMIT 1 ")
            sqlite_connection.commit()

        cursor.execute(
            "insert into " + subscription + "  (recent_msg_ids,time) values(?,?) ",
            (current_msg_id, datetime.datetime.now(),))
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return False


def form_message_metadata_and_data_from_message(msg_data, msg_metadata, msg, topic_name, subscription_name):
    """get  msg data and msg metadata from the message received"""
    try:
        # convert bytes string msg data to dict
        data = msg.data.decode()
        logging.info("data - {}".format(data))
        data = json.loads(data)
        msg_data.update(data)
        metadata = {"topic_name": topic_name, "subscription_name": subscription_name,
                    "msg_id": msg.message_id,
                    "msg_type": msg.attributes["type"]}
        msg_metadata.update(metadata)
        return SUCCESS

    except Exception as error:
        logging.exception("Form message metadata and data from message - Error :: {} ".format(error))
        return FAILURE


def create_utility_event_data(msg_data,msg_metadata):
    msg = {"msg_data": msg_data, "msg_metadata": msg_metadata}
    msg_type = msg_metadata["msg_type"]
    event_data = {"msg": msg, "msg_type": msg_type}
    return event_data


def async_message_pull(topic_name, subscription_name, project_id, credentials,
                       pubsub_client_system_resources, utility_event_trigger_data):
    
    try:
        
        """Receives messages from a pull subscription."""
        # create subscriber client
        credentials = service_account.Credentials.from_service_account_info(credentials)
        subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

        # The `subscription_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/subscriptions/{subscription_name}`
        subscription_path = subscriber.subscription_path(
            project_id, subscription_name
        )

        def callback(message):
            """Callback execute when new message received in the async pull subscription"""

            logging.debug("Async message pull callback - message received from {} ".format(subscription_name))
            logging.debug("Async message pull callback - {} ".format(message))

            msg_data = message.data.decode()
            logging.info("data - {}".format(msg_data))

            if message.attributes:
                value = message.attributes.get("type")
                logging.info("value - {}".format(value))
                
                try:
                    logging.info("Pubsub Client : utility_event triggered")

                    utility_event_trigger_data["event_data"] = {"msg": msg_data, "msg_type": value}
                    # Acquiring lock to avoid race condition at the GUI backend event access.
                    pubsub_client_system_resources["/utility_event_lock"].acquire(timeout=LOCK_ACQUIRE_TIME_OUT)
                    logging.info("Pubsub Client : utility_event_lock acquired")
                    utility_event_lock_status = True
                    # Send the msg to the GUI.
                    trigger_event_handler_framework(utility_event_trigger_data)
                    message.ack()

                except Exception as error:
                    logging.exception("Pubsub Client : Error in triggering event - {}".format(error))

                finally:
                    # We are using the counting semaphore for the lock. So, we need to maintain it's lock count as 1.
                    # Every release call increases it's lock count by 1.
                    # So, we need to release the lock only if we were acquired it.
                    if utility_event_lock_status:
                        pubsub_client_system_resources["/utility_event_lock"].release()
                        logging.info("Pubsub Client : utility_event_lock released")
##                        time.sleep(1)

        # Limit the subscriber to only have ten outstanding messages at a time.
        flow_control = pubsub_v1.types.FlowControl(max_messages=10)

        # Register the callback which will get invoked after receiving message from GCP
        streaming_pull_future = subscriber.subscribe(
            subscription_path, callback=callback
        )
        logging.debug("Async message pull - Listening for messages on {}..".format(subscription_path))


        # Wrap subscriber in a 'with' block to automatically call close() when done.
        with subscriber:
            try:
                # When `timeout` is not set, result() will block indefinitely,
                # unless an exception is encountered first.
                streaming_pull_future.result(timeout=None)
            except TimeoutError:
                logging.exception("Async message pull - Error :: ")
                streaming_pull_future.cancel()  # Trigger the shutdown.
                streaming_pull_future.result()  # Block until the shutdown is complete.

##        try:
##            # result() in a future will listen for messages and block indefinitely if `timeout` is not set,
##            # unless an exception is encountered first.
##            streaming_pull_future.result(timeout=None)
##
##        except Exception as error:  # noqa
##            logging.exception("Async message pull - Error ::  {} ".format(error))
##            streaming_pull_future.cancel()
            
    except Exception as error:
        logging.exception("pubsub_client_google_apis : async_message_pull - {}".format(error))


def sync_message_pull(topic_name, subscription_name, project_id, credentials,
                      pubsub_client_system_resources, utility_event_trigger_data):

    try:
        
        logging.info("------------------------sync_message_pull----------------------")
        """Pulling messages synchronously."""
        # create subscriber client
        credentials = service_account.Credentials.from_service_account_info(
            credentials)
        subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

        logging.info("subscriber :{}".format(subscriber))

        # The `subscription_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/subscriptions/{subscription_name}`
        subscription_path = subscriber.subscription_path(
            project_id, subscription_name
        )

        logging.info("subscription_path :{}".format(subscription_path))
        # Maximum number of messages per pull
        NUM_MESSAGES = 1

        # Pull messages from subscription
        response = subscriber.pull(subscription_path, max_messages=NUM_MESSAGES)

##        logging.info("response :{}".format(response))

        ack_ids = []
        for received_message in response.received_messages:
            logging.debug("Sync message pull - message received from {} ".format(subscription_name))
            logging.debug("Sync message pull - {} ".format(received_message))

            msg_data = received_message.message.data.decode()
            logging.info("data - {}".format(msg_data))

            value1 = received_message.message.attributes
            logging.info("value1 - {}".format(value1))

            value = value1['type']
            logging.info("value :{}".format(value))


            if value == 'order' or value == 'dispense':

                try:
                    logging.info("Pubsub Client : utility_event triggered")

                    utility_event_trigger_data["event_data"] = {"msg": msg_data, "msg_type": value}
                    # Acquiring lock to avoid race condition at the GUI backend event access.
                    pubsub_client_system_resources["/utility_event_lock"].acquire(timeout=LOCK_ACQUIRE_TIME_OUT)
                    logging.info("Pubsub Client : utility_event_lock acquired")
                    utility_event_lock_status = True
                    # Send the msg to the GUI.
                    trigger_event_handler_framework(utility_event_trigger_data)
                    ack_ids.append(received_message.ack_id)

                except Exception as error:
                    logging.exception("Pubsub Client : Error in triggering event - {}".format(error))

                finally:
                    # We are using the counting semaphore for the lock. So, we need to maintain it's lock count as 1.
                    # Every release call increases it's lock count by 1.
                    # So, we need to release the lock only if we were acquired it.
                    if utility_event_lock_status:
                        pubsub_client_system_resources["/utility_event_lock"].release()
                        logging.info("Pubsub Client : utility_event_lock released")
            
##            msg_metadata = {}
##            msg_data = {}
##            if form_message_metadata_and_data_from_message(msg_data, msg_metadata, received_message.message, topic_name,
##                                                           subscription_name) == FAILURE:
##                logging.exception("Async message pull callback - Error in msg format")
##                continue
##
##            logging.info("Sync message pull - message_metadata = {}".format(msg_metadata))
##            logging.info("Sync message pull - message_data = {}".format(msg_data))
##            try:
##                duplication_status = check_msg_duplication(msg_metadata["msg_id"], subscription_name)
##
##            except Exception as error:
##                logging.exception("Sync message pull - Error in dup msg check function : {} ".format(error))
##                continue
##
##            if duplication_status is False:
##                try:
##                    utility_event_trigger_data.event_data = create_utility_event_data(msg_data, msg_metadata)
##                    logging.info("Pubsub Client : utility_event triggered")
##
##                    # Acquiring lock to avoid race condition at the GUI backend event access.
##                    pubsub_client_system_resources["/utility_event_lock"].acquire(timeout=LOCK_ACQUIRE_TIME_OUT)
##                    logging.info("Pubsub Client : utility_event_lock acquired")
##                    utility_event_lock_status = True
##                    # Send the msg to the GUI.
##                    trigger_event_handler_framework(utility_event_trigger_data)
##                    ack_ids.append(received_message.ack_id)
##
##                except Exception as error:
##                    logging.exception("Pubsub Client : Error in triggering event - {}".format(error))
##
##                finally:
##                    # We are using the counting semaphore for the lock. So, we need to maintain it's lock count as 1.
##                    # Every release call increases it's lock count by 1.
##                    # So, we need to release the lock only if we were acquired it.
##                    if utility_event_lock_status:
##                        pubsub_client_system_resources["/utility_event_lock"].release()
##                        logging.info("Pubsub Client : utility_event_lock released")

        # Acknowledges the received messages so they will not be sent again.
        if ack_ids:
            subscriber.acknowledge(subscription_path, ack_ids)


    except Exception as error:
        logging.exception("pubsub_client_google_apis : sync_message_pull - {}".format(error))


def pull_message_synchronously(topic_name, subscription_name, project_id, service_act_credentials,
                      pubsub_client_system_resources, utility_event_trigger_data):

    try:
        logging.info("------------------------sync_message_pull----------------------")
        # create subscriber client

        audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

        credentials = jwt.Credentials.from_service_account_info(service_act_credentials, audience=audience)
        subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

        logging.info("subscriber :{}".format(subscriber))

        subscription_path = subscriber.subscription_path(
            project_id, subscription_name
        )

        logging.info("subscription_path :{}".format(subscription_path))
        # Maximum number of messages per pull
        NUM_MESSAGES = 1

        #with subscriber:
        response = subscriber.pull(
            request={"subscription": subscription_path, "max_messages": NUM_MESSAGES},
            retry=retry.Retry(deadline=60),
        )

        logging.debug(f"Response length: {len(response.received_messages)}")
        if len(response.received_messages) != 0:
            ack_ids = []
            for received_message in response.received_messages:
                ack_ids.append(received_message.ack_id)

                msg_data = received_message.message.data.decode()
                logging.info("Message data - {}".format(msg_data))

                value1 = received_message.message.attributes
                logging.info("Message Attribute - {}".format(value1))

                value = value1['type']
                logging.info("Message type :{}".format(value))

                if value == 'order' or value == 'dispense':

                    try:
                        logging.info("Pubsub Client : utility_event triggered")

                        utility_event_trigger_data["event_data"] = {"msg": msg_data, "msg_type": value}
                        # Acquiring lock to avoid race condition at the GUI backend event access.
                        pubsub_client_system_resources["/utility_event_lock"].acquire(timeout=LOCK_ACQUIRE_TIME_OUT)
                        logging.info("Pubsub Client : utility_event_lock acquired")
                        utility_event_lock_status = True
                        # Send the msg to the GUI.
                        trigger_event_handler_framework(utility_event_trigger_data)

                    except Exception as error:
                        logging.exception("Pubsub Client : Error in triggering event - {}".format(error))

                    finally:
                        if utility_event_lock_status:
                            pubsub_client_system_resources["/utility_event_lock"].release()
                            logging.info("Pubsub Client : utility_event_lock released")

            # Acknowledges the received messages so they will not be sent again.
            subscriber.acknowledge(request={"subscription": subscription_path, "ack_ids": ack_ids})
        
        subscriber.close()
        logging.debug(f"Received and acknowledged {len(response.received_messages)} messages from {subscription_path}.")

    except Exception as error:
        logging.exception("pubsub_client_google_apis : sync_message_pull - {}".format(error))
