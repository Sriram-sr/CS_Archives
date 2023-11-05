import posix_ipc
import sys

BASE_DIR = ""
COMMON_CODE_FILE_PATH = BASE_DIR + "src/source_code/common_code/"
SYSTEMCTL_SERVICE_STOP_COMMAND = "systemctl stop "

sys.path.append(COMMON_CODE_FILE_PATH)
from lavazza_cfds_common_apis import *


def unlink_message_queue(mq_name):
    try:
        posix_ipc.unlink_message_queue(mq_name)
        print("Cleanup_Module : {} is unlinked successfully".format(mq_name))

    except Exception as error:
        print("Cleanup_Module : unlink_message_queue : {} : {}".format(mq_name, error))


def unlink_semaphore_lock(sem_lock_name):
    try:
        posix_ipc.unlink_semaphore(sem_lock_name)
        print("Cleanup_Module : {} is unlinked successfully".format(sem_lock_name))

    except Exception as error:
        print("Cleanup_Module : unlink_semaphore_lock : {} : {} ".format(sem_lock_name, error))


def stop_services():
    """ Stop services using systemctl service stop command """
    service_details = {}

    if read_from_file(service_details, SERVICE_DETAILS_FILE) == FAILURE:
        raise Exception("File reading error in ", SERVICE_DETAILS_FILE)

    for service_detail in service_details["service_details"]:
        command = SYSTEMCTL_SERVICE_STOP_COMMAND + service_detail["service_name"]
        output = {}
        if command_executor(output, command) == SUCCESS:
            print("Stop service - Successfully stopped the service : {} ".format(
                service_detail["service_name"]))
        else:
            print("Stop service - Error while stopping {}  :  {}".format(
                service_detail["service_name"], output))


def cleanup():
    try:
        service_details = {}

        if read_from_file(service_details, SERVICE_DETAILS_FILE) == FAILURE:
            raise Exception("File reading error in ", SERVICE_DETAILS_FILE)

        stop_services()

        unlink_semaphore_lock("SystemEvent." + "application_start_event")

        for service_detail in service_details["service_details"]:
            for event_name in service_detail["service_resources"]["events"]:
                unlink_semaphore_lock("SystemEvent." + event_name)

            for queue_name in service_detail["service_resources"]["queues"]:
                unlink_message_queue(queue_name)

            for lock in service_detail["service_resources"]["locks"]:
                unlink_semaphore_lock(lock)

    except Exception as error:
        print("Cleanup_Module : {} ".format(error))


cleanup()
