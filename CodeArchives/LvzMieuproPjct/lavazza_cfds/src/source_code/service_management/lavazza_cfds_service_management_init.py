"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_service_management_init.py
 * Version        : 1.1
 * Date           : APRIL 20 2021
 *
 * Copyright (C) mieuPro Systems, 2021
 *
 ******************************************************************************
 """

import time
from lavazza_cfds_cleanup import *
import sys

# Logging basic configuration
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - Service_Management - %(levelname)s - %(message)s',
                    filename=LAVAZZA_COMMON_LOG_FILE, filemode='a')

service_details = {}
service_manager_system_resources = {}

# Provision status
provision_status = None
device_type = None
network_mode = None
device_mode = None
# Current running services in the machine
running_services = []


def shutdown():
    """ Executes shutdown command """
    ogging.debug("Shutdown - Command initiated")
    output = {}
    if command_executor(output, SHUTDOWN_COMMAND) == SUCCESS:
        logging.debug("Shutdown- Successfully turned off")
        return SUCCESS
    else:
        logging.exception("Shutdown - Error while shutdown : {} ".format(output))
        return FAILURE


def reboot():
    """ Executes reboot command """
    logging.debug("Reboot - Command initiated")
    output = {}
    if command_executor(output, REBOOT_COMMAND) == SUCCESS:
        logging.debug("Reboot - Successfully rebooted")
        return SUCCESS
    else:
        logging.exception("Reboot - Error while rebooting : {} ".format(output))
        return FAILURE


def shutdown_or_reboot_event_queue_handler(msg_type):
    if msg_type == REBOOT:
        cleanup()
        if reboot() == FAILURE:
            logging.exception("Service management - Error while rebooting")

    elif msg_type == SHUTDOWN:
        cleanup()
        if shutdown() == FAILURE:
            logging.exception("Service management - Error while shut down")

def restart_service():
    import subprocess
    cmd = "sudo systemctl restart lavazza_cfds_service_management.service"

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
    (stdout, stderr) = p.communicate()


def trigger_application_start_event(total_service_count):
    """ Triggers application start event based on initialized service details """
    try:
        count = 0
        while True:
            initialized_service_details = {}

            if read_from_file(initialized_service_details, INITIALIZED_SERVICES_FILE) == FAILURE:
                raise Exception("File reading error in ", INITIALIZED_SERVICES_FILE)
            logging.debug("initialized_service_details : {}".format(initialized_service_details))

            initialized_service_count = initialized_service_details["no_of_services"]

            if initialized_service_count == total_service_count:
                break
            else:
                count += 1
                if count != MAX_NO_OF_CHECK:
                    time.sleep(INITIALIZED_SERVICES_CHECK_INTERVAL)
                else:
                    restart_service()
                    raise Exception("Something went wrong while starting the Application")

        service_manager_system_resources["application_start_event"].set()
        logging.info("Trigger application start event - Application start event triggered")
        return SUCCESS

    except Exception as error:
        logging.exception("Trigger application start event - Error : {} ".format(error))
        return FAILURE


def get_total_service_count():
    """ Getting thread counts from file based on provision status """
    global provision_status, network_mode

    total_service_count = 0

    logging.info("get_total_service_count - network_mode : {}".format(network_mode))
    wifi_info = get_wifi_info()
    
    for service_detail in service_details["service_details"]:

        if provision_status is True:
            if (device_type in service_detail["working_device_types"]) and (network_mode in service_detail["working_wi-fi_modes"]):
                total_service_count += 1
        else:
            if service_detail["pre_provision_init_required"] and (network_mode in service_detail["working_wi-fi_modes"]):
                total_service_count += 1
    '''
    if provision_status is True:
        if wifi_info["Previous_ssid"] is not None and total_service_count == 6:
            total_service_count += 1
    '''
    return total_service_count


def init_service_manager_system_resources():
    """ Initializing all system resources to be created by the service_manager """
    global service_manager_system_resources

    for service_detail in service_details["service_details"]:
        if service_detail["service_name"] == SERVICE_MANAGER_SERVICE:
            service_manager_system_resources = get_system_resources(service_detail["service_resources"],
                                                                    own_service_resources=True)
            break

    logging.debug("service_manager_system_resources : {}".format(service_manager_system_resources))


def service_manager_init():
    """ Init service manager """
    try:
        # Init service manager's own system resources(events and queues)
        init_service_manager_system_resources()
        logging.info("service_manager_system_resources created successfully")

        # Update service manager thread to initialized service file
        if update_initialized_services_file(SERVICE_MANAGER_SERVICE) == FAILURE:
            raise Exception("error in update_initialized_services_file function")
        logging.info("update_initialized_services_file completed")

        # Get total service count from service detail file
        total_service_count = get_total_service_count()
        logging.debug("total_service_count : {}".format(total_service_count))

        # Trigger application start event
        if trigger_application_start_event(total_service_count) == FAILURE:
            logging.debug("service_manager_init : Error while starting the application")
            return FAILURE

        return SUCCESS

    except Exception as error:
        logging.exception("service_manager_init - ERROR : {} ".format(error))
        return FAILURE


def start_service(service):
    """ Start services using systemctl service start command """
    command = SYSTEMCTL_SERVICE_START_COMMAND + service
    output = {}
    if command_executor(output, command) == SUCCESS:
        logging.info("Start services - Successfully executed the service : {} ".format(service))
        running_services.append(service)
        return SUCCESS
    else:
        logging.exception("Start services - Error while starting {}  :  {}".format(service, output))
        return FAILURE


def service_startup_init():
    """ Run the services based on provision status """
    logging.info("Services startup init - getting started")
    global provision_status, device_type

    for service_detail in service_details["service_details"]:
        if service_detail["service_name"] == SERVICE_MANAGER_SERVICE:
            continue

        if service_detail["service_name"] == SERVER_COMMUN_SERVICE:
            wifi_info = get_wifi_info()
            if wifi_info["Previous_ssid"] is not None and provision_status is True:
                if start_service(service_detail["service_name"]) == FAILURE:
                    return FAILURE
                
        if provision_status is True:
            if (device_type in service_detail["working_device_types"]) and (network_mode in service_detail["working_wi-fi_modes"]):
                if start_service(service_detail["service_name"]) == FAILURE:
                    return FAILURE
        else:
            if service_detail["pre_provision_init_required"] and (network_mode in service_detail["working_wi-fi_modes"]):
                if start_service(service_detail["service_name"]) == FAILURE:
                    return FAILURE

    logging.debug("Running_services - {}".format(running_services))


def service_manager_start():

    logging.info("")
    logging.info("****************************************************")
    logging.info("* ")
    logging.info("* Version: lavazza_Black_White_OCB_Amazon_V1.2")
    logging.info("* Device: PI-3B+")
    logging.info("* Date: 13-08-2021")
    logging.info("* ")
    logging.info("* Copyright (C) mieuPro Systems, 2021")
    logging.info("* ")
    logging.info("****************************************************")
    logging.info("")

    global service_details, provision_status, device_type, network_mode, device_mode
    # [START OF SERVICE MANAGER]
    logging.info("Service Management - getting started")

    # Get provision status from device config file
    device_provision_info = {}
    if read_from_file(device_provision_info, DEVICE_PROVISION_INFO_FILE) == FAILURE:
        logging.exception("Service Management - Error while getting device_provision_info")
        sys.exit()

    provision_status = device_provision_info["provision_status"]
    device_type = device_provision_info["device_type"]
    network_mode = device_provision_info["network_mode"]
    device_mode = device_provision_info["device_mode"]

    logging.debug("provision_status : {}".format(provision_status))
    logging.debug("device_type : {}".format(device_type))
    logging.debug("network_mode : {}".format(network_mode))
    logging.debug("device_mode : {}".format(device_mode))

    if update_process_id("SERVICE_MANAGER") == FAILURE:
        logging.exception("Error in update_process_id")

    if read_from_file(service_details, SERVICE_DETAILS_FILE) == FAILURE:
        raise Exception("File reading error in ", SERVICE_DETAILS_FILE)

    cleanup()
    logging.info("Initial cleanup completed")

    if write_to_file(INITIALIZED_SERVICES_FILE_INITIAL_DATA, INITIALIZED_SERVICES_FILE) == FAILURE:
        logging.exception("Service Management - Error while initialize initialized services file")
        sys.exit()

    # Start the service init
    if service_startup_init() == FAILURE:
        sys.exit()
    logging.info("Service_startup_init finished successfully")

    # Service manager init
    if service_manager_init() == FAILURE:
        sys.exit()
    logging.info("Service_manager_init finished successfully")

    service_manager_event_handler_data = {"thread_name": "service_manager",
                                          "event": service_manager_system_resources["shutdown_or_reboot_event"],
                                          "queue": service_manager_system_resources["/shutdown_or_reboot_event_queue"],
                                          "queue_handler_function": shutdown_or_reboot_event_queue_handler,
                                          "finished_event": None}

    # wait for shutdown/reboot event
    while True:
        event_handler_framework(service_manager_event_handler_data)


service_manager_start()
