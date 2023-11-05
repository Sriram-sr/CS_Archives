import requests
from filelock import FileLock

from lavazza_cfds_server_communication_macros import *

server_communication_system_resources = {}


def send_server_ack_to_utility_thread():
    utility_event_lock_status = False
    try:
        upload_data_list_data = {}
        utility_event_data = {"thread_name": "Server_Upload_Handler",
                              "event": server_communication_system_resources["utility_event"],
                              "queue": server_communication_system_resources["/utility_queue"],
                              "event_data": None,
                              "finished_event": server_communication_system_resources["utility_finished_event"],
                              "response_required": False}

        if read_from_file(upload_data_list_data, UPLOAD_DATA_LIST_FILE) == FAILURE:
            raise Exception("File reading error in " + UPLOAD_DATA_LIST_FILE)

        if not upload_data_list_data["items"]:
            files_sent_status = True
        else:
            files_sent_status = False

        data = {"msg_type": "server_ack", "msg": files_sent_status}
        utility_event_data["event_data"] = data

        # Acquiring lock to avoid race condition at the GUI backend event access.
        server_communication_system_resources["/utility_event_lock"].acquire(timeout=LOCK_ACQUIRE_TIME_OUT)
        logging.info("Server_Communication : utility_event_lock acquired")
        utility_event_lock_status = True
        trigger_event_handler_framework(utility_event_data)

    except Exception as error:
        logging.exception("Server_Upload_Handler : send_server_ack_to_utility_thread : {}".format(error))

    finally:
        # We are using the counting semaphore for the lock. So, we need to maintain it's lock count as 1.
        # Every release call increases it's lock count by 1.
        # So, we need to release the lock only if we were acquired it.
        if utility_event_lock_status:
            server_communication_system_resources["/utility_event_lock"].release()
            logging.info("Server_Communication : utility_event_lock released")


def send_data_to_server(url, header, payload):
    try:
        logging.info("Server_Upload_Handler : inside send_data_to_server function")
        resp = requests.post(url=url, json=payload, headers=header)
        logging.info("Server_Upload_Handler : Server_response {}".format(resp))
        if resp.status_code == HTTP_SUCCESS_STATUS_CODE:
            return True
        else:
            return False
    except Exception as error:
        logging.exception("Server_Upload_Handler : send_data_to_server : %s", error)
        return False


def remove_from_upload_data_list(file_path, url_list):
    logging.info("Server_Upload_Handler : remove_from_upload_data_list function started")
    upload_data_list_data = {}

    try:
        with FileLock(UPLOAD_DATA_LIST_FILE + ".update.lock"):
            if read_from_file(upload_data_list_data, UPLOAD_DATA_LIST_FILE) < 0:
                raise Exception("File reading error in " + UPLOAD_DATA_LIST_FILE)

            item_entry = [item for item in upload_data_list_data["items"] if item["file_path"] == file_path]

            if item_entry:
                item_entry[0]["url_list"] = [url for url in item_entry[0]["url_list"] if url not in url_list]
                if not item_entry[0]["url_list"]:
                    upload_data_list_data["items"].remove(item_entry[0])
                    upload_data_list_data["no_of_items"] -= 1
                    logging.debug("Server_Upload_Handler : %s is remove_from_upload_data_list", file_path)
            else:
                logging.warning("Server_Upload_Handler : %s is not found", file_path)

            if write_to_file(upload_data_list_data, UPLOAD_DATA_LIST_FILE) == FAILURE:
                raise Exception("write_to_file error in " + UPLOAD_DATA_LIST_FILE)

    except Exception as error:
        logging.exception("Server_Upload_Handler : remove_from_upload_data_list : %s", error)


def upload_to_server_service(input_data):
    file_data = {}

    try:
        '''entry = {"file_type": "file_type", "file_path": "file_path", "url_list": ["url"], 
                    "retry_on_error": retry_on_error, "delete_on_success": "delete_on_success_flag"}
        '''

        device_provision_info = {}
        if read_from_file(device_provision_info, \
                          DEVICE_PROVISION_INFO_FILE) == FAILURE:
            logging.debug("DEVICE_PROVISION_INFO_FILE read error")
            raise Exception("read DEVICE_PROVISION_INFO_FILE error in " + DEVICE_PROVISION_INFO_FILE)

        header = {"Authorization": TOKEN, 'content-type': 'application/json', "device_id": device_provision_info["device_id"]}

        if read_from_file(file_data, input_data['file_path']) == FAILURE:
            raise Exception("File reading error in " + input_data['file_path'])

        payload = {'file_type': input_data['file_type'], 'data': file_data}

        successful_url_list = [url for url in input_data['url_list'] if send_data_to_server(url, header, payload)]

        if set(successful_url_list) == set(input_data['url_list']) or not input_data['retry_on_error']:
            remove_from_upload_data_list(input_data['file_path'], input_data['url_list'])
            if input_data['delete_on_success']:
                os.remove(input_data['file_path'])
        else:
            remove_from_upload_data_list(input_data['file_path'], successful_url_list)

    except Exception as error:
        logging.exception("Server_Upload_Handler : upload_to_server_service : %s", error)


def upload_to_server_event_handler(system_resources):
    logging.info("Server_Upload_Handler : upload_to_server_handler getting started")
    global server_communication_system_resources
    upload_data_list_data = {}

    server_communication_system_resources = system_resources
    logging.debug("Server_Upload_Handler : server_communication_system_resources : {}".format(
        server_communication_system_resources))

    if not os.path.isfile(UPLOAD_DATA_LIST_FILE):
        if write_to_file(UPLOAD_DATA_LIST_FILE_INITIAL_DATA, UPLOAD_DATA_LIST_FILE) == FAILURE:
            raise Exception("write_to_file error in " + UPLOAD_DATA_LIST_FILE)

    device_provision_info = {}
    if read_from_file(device_provision_info, \
                          DEVICE_PROVISION_INFO_FILE) == FAILURE:
        logging.debug("DEVICE_PROVISION_INFO_FILE read error")
        raise Exception("read DEVICE_PROVISION_INFO_FILE error in " + DEVICE_PROVISION_INFO_FILE)

    if device_provision_info["provision_status"]:
        send_current_firmware_version_to_server()

    while True:
        try:
            with FileLock(UPLOAD_DATA_LIST_FILE + ".update.lock"):

                if read_from_file(upload_data_list_data, UPLOAD_DATA_LIST_FILE) == FAILURE:
                    raise Exception("File reading error in " + UPLOAD_DATA_LIST_FILE)

                if not upload_data_list_data["run_time_entries"]:
                    server_communication_system_resources["server_upload_event"].clear()
                else:
                    server_communication_system_resources["server_upload_event"].set()

                    upload_data_list_data["run_time_entries"].clear()

                    if write_to_file(upload_data_list_data, UPLOAD_DATA_LIST_FILE) == FAILURE:
                        raise Exception("File writing error in " + UPLOAD_DATA_LIST_FILE)

            server_upload_event_time_out = RETRY_INTERVAL if upload_data_list_data["items"] else RETRY_POLL_INTERVAL

            if not server_communication_system_resources["server_upload_event"].isSet():
                logging.info("Server_Upload_Handler : waiting for the server_upload_event")
                server_communication_system_resources["server_upload_event"].wait(server_upload_event_time_out)

                if read_from_file(upload_data_list_data, UPLOAD_DATA_LIST_FILE) == FAILURE:
                    raise Exception("File reading error in " + UPLOAD_DATA_LIST_FILE)

            logging.info("Server_Upload_Handler : Server_Upload_Event status : {}".format(
                server_communication_system_resources["server_upload_event"].isSet()))

            if server_communication_system_resources["wifi_connection_status_event"]:

                for item in upload_data_list_data["items"]:
                    upload_to_server_service(item)

                if not device_provision_info["provision_status"]:
                    logging.info("Server_Upload_Handler : notify the utility event")
                    send_server_ack_to_utility_thread()

            else:
                logging.warning("Server_Upload_Handler : Network Down")

            if not device_provision_info["provision_status"]:
                send_server_ack_to_utility_thread()

            logging.info("Server_Upload_Handler : upload_to_server_event_handler function finished")

        except Exception as error:
            logging.exception("Server_Upload_Handler : %s", error)


def send_current_firmware_version_to_server():

    try:

        device_monitor_info = {}
        version_sync_url_list = []
        
        if read_from_file(device_monitor_info, DEVICE_MONITOR_FILE) == FAILURE:
            raise Exception("File reading error in " + DEVICE_MONITOR_FILE)

        if add_to_url_list(CONFIGURATION_SERVER, version_sync_url_list, VERSION_SYNC_SERVER_PATH) == FAILURE:
            raise Exception("add_to_url_list error" + UPLOAD_DATA_LIST_FILE)

        firmware_version = device_monitor_info['firmware_version']
        feature_configs_version = device_monitor_info["feature_configs_version"]
        logging.info("sending firmware_version_to_server")
        firmware_details = {"firmware_version": firmware_version, "feature_configs_version":feature_configs_version, "iot_enabled":device_monitor_info["iot_enabled"]}

        if write_to_file(firmware_details, VERSION_SYNC_DATA_FILE) == FAILURE:
            raise Exception("write_to_file error in " + VERSION_SYNC_DATA_FILE)

        server_upload_data = {"file_type": "version_sync", "file_path": VERSION_SYNC_DATA_FILE,
                                          "url_list": version_sync_url_list, "retry_on_error": ENABLE,
                                          "delete_on_success": ENABLE}
        add_to_upload_data_list(server_communication_system_resources["server_upload_event"], server_upload_data)

    except Exception as Error:
        logging.error("server_upload_handler: send_current_firmware_version_to_server - %s",Error)
