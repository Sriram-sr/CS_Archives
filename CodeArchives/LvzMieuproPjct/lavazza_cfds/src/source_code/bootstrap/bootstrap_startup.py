# def read_json_file(file): - reads json data from given file
# def update_json_file(data,file): - updates json data in the given file
# def copy_file_from_a_folder_to_another(source_file, destination_filepath): - used for copying files from updates dir to src dir
# def remove_files_recursively_from_dir(source_dir): -  after firmware_upgrade, remove files recursively from all sub_dirs of updates/source_code dir
# def check_for_incremental_updates(): -  # handles the incremental_updates, resource_updates, feature_config updates
# def check_for_complete_upgrade(): - handles the firmware_upgrade, replace the source_code dir with source_code_update dir contents
# def on_restart_check_for_updates(): - on_restart, checking for any updates present and call the upgrade  modules


import shutil
import json
import time
import os
import subprocess
from datetime import datetime

LAVAZZA_BASE_DIR = "/home/pi/lavazza"


SOURCE_CODE_PATH = LAVAZZA_BASE_DIR  + "/src/source_code/"
SOURCE_CODE_UPDATE_PATH = LAVAZZA_BASE_DIR  + "/updates/source_code"

RESOURCES_PATH = LAVAZZA_BASE_DIR  + "/src/resources/"
RESOURCES_UPDATE_PATH = LAVAZZA_BASE_DIR +  "/updates/resources/"

FEATURE_CONFIGS_PATH = LAVAZZA_BASE_DIR + "/src/configs/feature_configs/"
FEATURE_CONFIGS_UPDATE_PATH = LAVAZZA_BASE_DIR + "/updates/configs/feature_configs/"

DEVICE_PROVISION_INFO = LAVAZZA_BASE_DIR  + "/src/configs/device_configs/device_provision_info.json"
DEVICE_MONITOR = LAVAZZA_BASE_DIR  + "/src/configs/device_configs/device_monitor.json"


def read_json_file(file):
    try:
        with open(file) as f:
            data = json.load(f)
            return data
    except Exception as Error:
        print(Error)

def update_json_file(data,file):
    try:
        with open(file,'w') as f:
            json.dump(data,f)
    except Exception as Error:
        print(Error)

def copy_file_from_a_folder_to_another(source_file, destination_filepath):
    """copies the source_file to destination directory"""

    # delete dest. file if the destination already contains the same file
    dir, file_name = os.path.split(source_file)
    destination_file = destination_filepath + file_name
    if os.path.isfile(destination_file):
        print("File exist", file_name)
        os.remove(destination_file)
        print("File deleted", file_name)

    #copy file to dest. dir
    try:
        print("copying process started")
        shutil.copy(source_file, destination_filepath)
        print("copying process completed")
        return 1
    except Exception as Error:
        print("Exception occured in copy_file_from_a_folder_to_another: \n", Error)
        return 0


def check_for_incremental_updates(update):
    """handles the incremental_updates, resource_updates, feature_config updates,
       move the files present in specified updates dir to  specified src dir"""

    if update == 'incremental':
        source_dir = SOURCE_CODE_UPDATE_PATH

    elif update == 'resources':
        source_dir = RESOURCES_UPDATE_PATH

    elif update == 'feature_configs':
        source_dir = FEATURE_CONFIGS_UPDATE_PATH

    for dirpath, dirnames, files in os.walk(source_dir):
        curr_dir = dirpath
        print("Files")
        for file in files:
            print("********************************************")
            print(file)
            src = curr_dir + '/'+ file
            dest = curr_dir.replace('updates', 'src') +'/'
            print("src:", src)
            print("dest:", dest)
            copy_file_from_a_folder_to_another(src, dest)
            os.remove(src)
            print("********************************************")


def remove_files_recursively_from_dir(source_dir):
    """after firmware_upgrde, delete all the files recursively from all sub_dirs of source_dir"""

    for dirpath, dirnames, files in os.walk(source_dir):
        curr_dir = dirpath
        for file in files:
            filepath = curr_dir + "/" + file
            os.remove(filepath)



def check_for_complete_upgrade():
    """handles the firmware_upgrade,
       replace the /src/source dir with /updates/source_code dir contents"""

    print("Deleting working source_code folder")
    #Deleting working source_code folder
    if os.path.isdir(SOURCE_CODE_PATH):
        shutil.rmtree(SOURCE_CODE_PATH)
    print("Deleted working source_code folder")
    time.sleep(10)

    print("Copying source_code_update folder to source_code")
    #Copying updates/source_code  to src/source_code
    shutil.copytree(SOURCE_CODE_UPDATE_PATH, SOURCE_CODE_PATH)
    print("Copied source_code_update folder to source_code")

    print("cleaning the source_code_update sub_dirs")
    #cleaning the updates/source_code sub_dirs
    remove_files_recursively_from_dir(SOURCE_CODE_UPDATE_PATH)


def on_restart_check_for_updates():
    """on_restart, checking for any updates present and call the upgrade  modules"""
  
    #update related code will be added later, now not handling any updates

 
    last_boot_time = subprocess.check_output(['date']).decode("utf8")
    device_monitor = read_json_file(DEVICE_MONITOR)

    device_monitor['last_boot_time']= last_boot_time
    update_json_file(device_monitor, DEVICE_MONITOR)
    
    print(device_monitor)
   



if __name__ == "__main__":
    try:
        on_restart_check_for_updates()
    except Exception as Error:
        print(Error)

    subprocess.Popen(["sudo", "systemctl", "start", "lavazza_service_management.service"])

    exit()

