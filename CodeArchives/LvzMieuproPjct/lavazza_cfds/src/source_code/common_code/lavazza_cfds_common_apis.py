"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_common_apis.py
 * Version        : 1.1
 * Date           : JULY 24 2021
 *
 * Copyright (C) mieuPro Systems, 2021-2022
 *
 ******************************************************************************
 """

import logging
from subprocess import Popen, PIPE
import posix_ipc
from SystemEvent import SystemEvent
from filelock import FileLock
import requests
import base64


from lavazza_cfds_common_macros import *


def read_from_file(data, file_to_read):
    """ Reads data from file """
    try:
        with FileLock(file_to_read + ".lock"):
            with open(file_to_read) as file:
                data.update(json.load(file))
        return SUCCESS

    except:
        logging.exception("Read from file to file: {}".format(file_to_read))
        return FAILURE


def write_to_file(data, file_to_write):
    """ Writes data to file """
    try:
        with FileLock(file_to_write + ".lock"):
            file = open(file_to_write, 'w')
            json.dump(data, file)
            file.close()
        return SUCCESS

    except:
        logging.exception("Write to file: {}".format(file_to_write))
        return FAILURE


def update_initialized_services_file(service_name):
    """ Update the initialized_services_file with given service """
    initialized_services = {}

    try:
        # We are using file lock to avoid race condition with the file accessing.
        # It takes the locking key as an argument.
        with FileLock(INITIALIZED_SERVICES_FILE + ".update_lock"):
            if read_from_file(initialized_services, INITIALIZED_SERVICES_FILE) == FAILURE:
                raise Exception("File reading error in ", INITIALIZED_SERVICES_FILE)

            initialized_services["services"].append(service_name)
            initialized_services["no_of_services"] += 1

            if write_to_file(initialized_services, INITIALIZED_SERVICES_FILE) == FAILURE:
                raise Exception("write_to_file error in" + INITIALIZED_SERVICES_FILE)

            return SUCCESS

    except Exception as error:
        logging.exception("{} : update_initialized_services_file : {}".format(service_name, error))
        return FAILURE


def get_system_resources(service_resources, own_service_resources):
    """ Creating the own system resources or opening the dependant system resources """
    system_resources = {}

    # Creating the application_start_event only if it is a own_service_resources.
    # Because, It's common for all the services.
    if own_service_resources:
        system_resources["application_start_event"] = SystemEvent("application_start_event")

    # Creating the own and dependant events.
    for event in service_resources["events"]:
        system_resources[event] = SystemEvent(event)

    for queue in service_resources["queues"]:
        # Creating the own service msg queues.
        if own_service_resources:
            system_resources[queue] = posix_ipc.MessageQueue(name=queue, flags=posix_ipc.O_CREX,
                                                             max_messages=MSG_QUEUE_SIZE)
        # Opening the dependant service msg queues.
        else:
            system_resources[queue] = posix_ipc.MessageQueue(name=queue)

    for lock in service_resources["locks"]:
        # Creating the own service semaphore locks.
        if own_service_resources:
            system_resources[lock] = posix_ipc.Semaphore(name=lock, flags=posix_ipc.O_CREX,
                                                         initial_value=SEMAPHORE_INITIAL_VALUE)
        # Opening the dependant service semaphore locks.
        else:
            system_resources[lock] = posix_ipc.Semaphore(name=lock)

    return system_resources


def initialize_service(service_system_resources, service_name):
    """ Initializing the service and start the service coordination with the other services """
    device_provision_info = {}
    service_details = {}
    dependant_services = None

    try:
        # Get provision status from device config file
        if read_from_file(device_provision_info, DEVICE_PROVISION_INFO_FILE) == FAILURE:
            raise Exception("Error while getting device_provision_info")

        # Get the service details.
        if read_from_file(service_details, SERVICE_DETAILS_FILE) == FAILURE:
            raise Exception("File reading error in ", SERVICE_DETAILS_FILE)

        for service_detail in service_details["service_details"]:
            # Get the specified service detail.
            if service_detail["service_name"] == service_name:
                # Get the specified system resources
                service_system_resources.update(get_system_resources(service_detail["service_resources"], True))
                # Get the dependant services.
                dependant_services = service_detail["dependant_services"]
                break

        # put the entry in the initialized services file
        if update_initialized_services_file(service_name) == FAILURE:
            raise Exception("Error in update_initialized_services_file function")
        logging.info("{} : update_initialized_services_file successfully".format(service_name))

        logging.info("{} : Waiting for the application start event".format(service_name))
        # Waiting for the application start event. It is used to coordinate all the services at the starting.
        service_system_resources["application_start_event"].wait()
        logging.info("{} : Application start event triggered".format(service_name))

        for service_detail in service_details["service_details"]:
            if service_detail["service_name"] in dependant_services:
                # We need to get the dependant service system resources only if that service running.
                # Because, at some conditions some services will not getting started.
                # i.e GUI is not running for the kitchen type and mb io handler will not running at pre provision
                if device_provision_info["provision_status"] is True:
                    # Checking for the device type whether the dependant service running for this device type.
                    if device_provision_info["device_type"] in service_detail["working_device_types"] and device_provision_info["network_mode"] in service_detail["working_wi-fi_modes"]:
                        service_system_resources.update(get_system_resources(service_detail["service_resources"], False))
                    else:
                        logging.info("{} : {} is not running for this device type".format(
                            service_name, service_detail["service_name"]))
                else:
                    # Checking for the pre_provision_init_required whether the dependant service
                    # running at hte pre provision state
                    if service_detail["pre_provision_init_required"] is True and device_provision_info["network_mode"] in service_detail["working_wi-fi_modes"]:
                        service_system_resources.update(get_system_resources(service_detail["service_resources"], False))
                    else:
                        logging.info("{} : {} is not running at pre provision stage".format(
                            service_name, service_detail["service_name"]))

        return SUCCESS

    except Exception as error:
        logging.exception("{} : initialize_thread : {}".format(service_name, error))
        return FAILURE


def clean_msg_queue(queue):
    """ Clears the msg queue when the error occurs """
    try:
        # If the msg queue is non empty, we should clear it.
        if queue.current_messages > 0:
            queue_data = json.loads(queue.receive(timeout=MSG_QUEUE_TIME_OUT)[0].decode())
            logging.warning("Clean_msg_queue : Queue is not cleared properly. Queue_data - {}".format(queue_data))

        logging.info("Clean_msg_queue : Msg queue is perfect Queue size - {}".format(queue.current_messages))

    except Exception as error:
        logging.exception("Clean_msg_queue : {}".format(error))


def trigger_event_handler_framework(input_data):
    # input_data = {"thread_name": thread_name, "event": event, "queue": queue, "event_data": event_data,
    # "finished_event": finished_event, "response_required": True or False}
    try:
        input_data["queue"].send(json.dumps(input_data["event_data"]).encode(), timeout=MSG_QUEUE_TIME_OUT)
        logging.info("{} : event data send successfully".format(input_data["thread_name"]))
        input_data["event"].set()
        logging.info("{} : {} set successfully".format(input_data["thread_name"], input_data["event"]))
        if input_data["finished_event"]:
            logging.info("{} : Waiting for the {}".format(input_data["thread_name"], input_data["finished_event"]))
            input_data["finished_event"].wait(FINISHED_EVENT_TIME_OUT)
            logging.info("{} : {} occurred".format(input_data["thread_name"], input_data["finished_event"]))
            input_data["finished_event"].clear()
            logging.info("{} : {} cleared".format(input_data["thread_name"], input_data["finished_event"]))

        if input_data["response_required"]:
            status = json.loads(input_data["queue"].receive(timeout=MSG_QUEUE_TIME_OUT)[0].decode())
            return status

    except Exception as error:
        logging.exception("{} : trigger_event : {}".format(input_data["thread_name"], error))


def event_handler_framework(input_data):
    # input_data = {"thread_name": thread_name, "event": event, "queue": queue,
    # "queue_handler_function": queue_handler_function, "finished_event": finished_event}
    response = None

    try:
        logging.info("{} : Waiting for the {}".format(input_data["thread_name"], input_data["event"]))
        input_data["event"].wait()
        logging.info("{} : {} occurred".format(input_data["thread_name"], input_data["event"]))
        received_data = json.loads(input_data["queue"].receive(timeout=MSG_QUEUE_TIME_OUT)[0].decode())
        logging.debug("{} : Msg Queue data : {}".format(input_data["thread_name"], received_data))
        response = input_data["queue_handler_function"](received_data)
        logging.info("{} : queue_handler_function finished".format(input_data["thread_name"]))

    except Exception as error:
        logging.exception("{} : event_handler : {}".format(input_data["thread_name"], error))

    finally:
        input_data["event"].clear()
        logging.info("{} : {} cleared".format(input_data["thread_name"], input_data["event"]))

        clean_msg_queue(input_data["queue"])

        if input_data["finished_event"]:
            input_data["finished_event"].set()
            logging.info("{} : {} set successfully".format(input_data["thread_name"], input_data["finished_event"]))

        if response is not None:
            input_data["queue"].send(json.dumps(response).encode(), timeout=MSG_QUEUE_TIME_OUT)
            logging.info("{} : response send successfully".format(input_data["thread_name"]))


def command_executor(output, command):
    """ Executes the command and returns the output """

    try:
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)  # Execute the command
        stdout, stderr = process.communicate()
        if stderr:
            output.update({"stderr": stderr})
        if stdout:
            output.update({"stdout": stdout})
        return process.returncode

    except:
        logging.exception("Command Executor - Execution failed for the command :: {}".format(command))
        return FAILURE


def update_process_id(process_name):
    try:

        process_id = os.getpid()
        process_name_with_pid = {process_name: process_id}
        print(process_name_with_pid)

        if not (os.path.isfile(PROCESS_IDS_FILE)):
            if write_to_file(process_name_with_pid, PROCESS_IDS_FILE) == FAILURE:
                raise Exception("File write error: %s", PROCESS_IDS_FILE)
        else:
            data = {}
            if read_from_file(data, PROCESS_IDS_FILE) == FAILURE:
                raise Exception("File read error: %s", PROCESS_IDS_FILE)
            data.update(process_name_with_pid)
            if write_to_file(data, PROCESS_IDS_FILE) == FAILURE:
                raise Exception("File write error: %s", PROCESS_IDS_FILE)
            return SUCCESS
    except:
        logging.exception("update_process_id")
        return FAILURE


def get_product_details():

    product_names = [None, None, None, None, None, None, None, None]

    try:
        product_details = {}

        # READ DEVICE DETAILS FROM DEVICE PROVISION INFO FILE
        if read_from_file(product_details, DEVICE_PROVISION_INFO_FILE) == FAILURE:
            raise Exception("File reading error in " + DEVICE_PROVISION_INFO_FILE)

        products_details = product_details["provisioned_product_details"]

        for index in range(MAX_PRODUCT_COUNT):
            product_names[index] = products_details[index]

        product_count = len(product_names)

        return product_names, product_count

    except:
        logging.exception("get_product_count:")


def read_from_system_file(data, file_to_read):
    """ Reads data from system file """
    try:
        with open(file_to_read) as file:
            data.append(file.read())
        return SUCCESS

    except Exception as error:
        logging.exception("Read from file - Error {}".format(error))
        return FAILURE


def write_to_system_file(data, file_to_write, mode):
    """ Writes data to file """
    try:
        with open(file_to_write,mode) as file:
            file.write(data)
        return SUCCESS
    except Exception as error:
        logging.exception("Write to file: {}".format(error))
        return FAILURE


class RaceConditionAvoidance:
    def __init__(self, lock, lock_timeout):
        self.lock = lock
        self.lock_timeout = lock_timeout

    def __enter__(self):
        self.lock.acquire(self.lock_timeout)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.lock.release()


def getMAC(interface='eth0'):

    try:
        str = open('/sys/class/net/%s/address' % interface).read()
        return str[0:17]

    except:
        str = None
        return str


def get_wifi_info():

    try:
        wifi_info = {}

        if read_from_file(wifi_info, WIFI_CONF_FILE) == FAILURE:
            raise Exception("WIFI_INFO_FILE read error")

        return wifi_info

    except Exception as error:
        logging.exception("get_wifi_info: {}".format(error))
        return FAILURE


def add_to_url_list(server_type, url_list, url_path_extension):
    """ Forms URL and returns URL list """

    try:

        logging.debug("---------- add_to_url_list -----------")
        with FileLock(FEATURE_CONF_FILE+ ".lock"):
            with open(FEATURE_CONF_FILE) as f:
                feature_configs = json.load(f)

        logging.info("feature_configs -{}".format(feature_configs))
        server_info = feature_configs["server_info"]
        servers = server_info[server_type]
        for server in servers:
            ip = server["ip"]
            port = server["port"]
            url = HTTPS + ip + COLON + port + url_path_extension
            url_list.append(url)
        return SUCCESS

    except Exception as Error:
        logging.exception("Get URL list - Error - {}".format(Error))
        return FAILURE


def add_to_upload_data_list(server_upload_event, data):

    try:
        with FileLock(UPLOAD_DATA_LIST_FILE + ".update.lock"):
            upload_data_list = {}

            if read_from_file(upload_data_list, UPLOAD_DATA_LIST_FILE) == FAILURE:
                raise Exception("Failed to read in the {}".format(UPLOAD_DATA_LIST_FILE))

            items = upload_data_list["items"]
            item_entry = [item_entry for item_entry in items if item_entry["file_path"] == data["file_path"]]

            if item_entry:
                item_entry[0]["url_list"] = list(set(data["url_list"]) | set(item_entry[0]["url_list"]))
            else:
                upload_data_list["items"].append(data)
                upload_data_list["no_of_items"] += 1
                logging.info("Add to upload data list : {} New entry to upload data list".format(data))

            if server_upload_event.isSet():
                upload_data_list["run_time_entries"].append(data["file_type"])
            else:
                server_upload_event.set()

            if write_to_file(upload_data_list, UPLOAD_DATA_LIST_FILE) == FAILURE:
                raise Exception("Failed to write in the {}".format(UPLOAD_DATA_LIST_FILE))

            return SUCCESS

    except Exception as error:
        logging.exception("Add to upload data list - Error : {}".format(error))
        return FAILURE


# TO SEND REST CALL TO SERVER
def api_caller(req_type=None, req_url=None, payload=None, timeout=5, params=None, headers=None):
    if req_type == "GET":
        try:
            res = requests.get(req_url, timeout=timeout, params=params, headers=headers)
            return res.json()
        except requests.exceptions.Timeout as e:
            logging.exception("GET Api caller - Error : {}".format(e))
            return FAILURE

    elif req_type == "POST":
        try:
            res = requests.post(req_url, timeout=timeout, params=params, headers=headers, json=payload)
            return res.json()
        except requests.exceptions.Timeout as e:
            logging.exception("POST Api caller - Error : {}".format(e))
            return FAILURE


# TO CONVERT STRING TO ENCODE FORM
# DEVICE NAME CAN BE ENCODED
def obfuscate(string):
    encoded_str = base64.b64encode(string.encode())
    return encoded_str.decode()
