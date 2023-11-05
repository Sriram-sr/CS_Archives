"""
 ******************************************************************************
 *
 * File Name      : lavazza_cfds_diagnostics_init.py
 * Version        : 1.0
 * Date           : June 12 2020
 *
 * Copyright (C) mieuPro Systems, 2020
 *
 ******************************************************************************
 """

# def remove_excess_readings(max_no_of_readings, file):
# def is_empty_line_present(file): - checks empty line present in a file
# def update_process_mem_info(dict_cmds): - find each module memory info and update
# def find_critical_info_and_update(dict_cmds): - find some important diagnostic info
# def fing_logs_and_update(commands, file, current_count, max_no_of_readings,critical_parameters_limit): - execute diagnostics commands and store it in the log files
# def is_json_file_present(file): - checks if json_log_file present and create new if not exists
# def backup_file(file,backup_file): - backup the current logs to backup logfile on every restart or after a cycle
# def main(): - read the DIAGNOSTICS CONFIG and run the while loop to call update reading function


import subprocess
import pprint
import psutil

from datetime import datetime
import time
import os
import shutil
from lavazza_cfds_diagnostics_macros import *

import logging

logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - DIAGNSOTICS - %(levelname)s - %(message)s',
                    filename=LAVAZZA_COMMON_LOG_FILE ,filemode='a')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - DIAGNSOTICS - %(levelname)s - %(message)s',
#                     filename='/home/pi/lavazza/logs/diag.log', filemode='a')
#

def remove_excess_readings(max_no_of_readings, file):
    """if no_of_readings present in log file are more than max_no_of_readings configured,
     remove the excess no_of_readings readings,
     it occurs when a max_no_of_readings is changed from a higher value to a lower value"""

    logging.info("started remove_excess_readings")
    readings = {}
    if read_from_file(readings, file) == FAILURE:
        raise Exception("remove_excess_readings - Readings file error :", file)

    no_of_readings_present_in_file = len(readings) - 1

    #logging.debug("no_of_readings_present_in_file = %s", no_of_readings_present_in_file)

    #logging.debug("max_no_of_readings = %s", max_no_of_readings)

    if no_of_readings_present_in_file > max_no_of_readings:

        logging.debug("Key length greater than max_no_of_readings")

        for reading_no in range(max_no_of_readings + 1, no_of_readings_present_in_file + 1):
            key = "reading_" + str(reading_no)
            logging.debug("DELETING key = %s",key)
            try:
                del readings[key]
            except:
                logging.exception("remove_excess_readings")
                logging.critical("DELETING key = %s", key)


        if write_to_file(readings, file) == FAILURE:
            raise Exception("Write to file error :",file)


def is_empty_line_present(file):
    """checks if file is empty or contains only empty line"""

    f = open(file)
    line = f.readline()
    if not line.strip():
        return 1
    else:
        return 0




def update_process_mem_info(dict_cmds):

    data = {}
    if read_from_file(data, PROCESS_IDS_FILE) == FAILURE:
        raise Exception("File read error: %s", PROCESS_IDS_FILE)
    process_dict = {}
    for process_name, process_id in data.items():
        #logging.debug("%s : %s",process_name, process_id)
        if psutil.pid_exists(process_id):
            #logging.debug("%s : PID exists",process_name)
            process = psutil.Process(process_id)
              
            process_info={
                         "ram": process.memory_full_info().rss >> 20,
                         "swap": process.memory_full_info().swap >> 20 }
            """
                process_info={"memory_full_info": process.memory_full_info(),
                         "ram": process.memory_full_info().rss >> 20,
                         "swap": process.memory_full_info().swap >> 20 }
            """

            process_dict.update({process_name: process_info})
        else:
             logging.warning("%s : PID not exists",process_name)

    dict_cmds.update({"process_mem_info":{"stdout":process_dict}})



def find_critical_info_and_update(dict_cmds,critical_parameters_limit):
    """memory, cpu, disk size """

    #get iostat_cpu_avg_usage_percent
    output = {}
    command = "iostat | awk 'NR==4{print $6 }'"
    command_executor(output, command)
    if 'stderr' in output.keys():
        iostat_cpu_avg_usage_percent = output['stderr'].decode('utf-8')
    elif output:
        iostat_cpu_avg_usage_percent = 100 - float(output['stdout'].decode('utf-8'))

    critical_parameters = {"mem_usage_percent":{"stdout":psutil.virtual_memory().percent},
            "swap_usage_percent":{"stdout":psutil.swap_memory().percent},
            "disk_usage_percent":{"stdout":psutil.disk_usage('/').percent},
            "cpu_avg_usage_time_percent_since_last_call":{"stdout":100 - psutil.cpu_times_percent().idle},
            "iostat_cpu_avg_usage_percent_since_boot":{"stdout":iostat_cpu_avg_usage_percent}}

    dict_cmds.update(critical_parameters)
    
    for key in critical_parameters.keys():
        try:
            if key in critical_parameters_limit.keys():
                if critical_parameters[key]['stdout'] > critical_parameters_limit[key]:
                    logging.critical("diagnostic parameters reached critical limits '%s' %s",key,critical_parameters[key] )
            else:
                logging.warning("key not present in critical_parameters_limit:%s",key)
        except:
            logging.exception("Critical parameters compared with specified level - %s",key)

    



def fing_logs_and_update(commands, file, current_count, max_no_of_readings,critical_parameters_limit):
    """finds the log output for log commands and updates the log file
       log files are rotated if it reaches max_no_of_readings"""
    file_updated_in_current_iteration = 0

    # create dictionary for storing command and command outputs
    dict_cmds = {}

    # current_count indicates current reading_value to be updated
    #logging.debug("current_count = %s", current_count)

    reading_value = "reading_" + str(current_count)
    #logging.debug("reading_value = %s", reading_value)

    # storing cmd_name and cmd_op in dict
    for cmd in commands:
        try:
            p = subprocess.Popen(cmd[1], stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
            (stdout, stderr) = p.communicate()
            output={}
            if stdout:
                output.update({"stdout": stdout.decode("ASCII")})
            if stderr:
                output.update({"stderr": stderr.decode("ASCII")})

            dict_cmds.update({cmd[0]: output})



        except:
            logging.exception("fing_logs_and_update - Executing log commands")
    dict_cmds.update({"date_time":{"stdout":str(datetime.now())}})

    try:
        if file == DETAILED_LOG:
            update_process_mem_info(dict_cmds)
    except:
         logging.exception( "fing_logs_and_update - update proc_mem_info ")
      
    try:
        if file == SUMMARY_LOG:
            if critical_parameters_limit:
                find_critical_info_and_update(dict_cmds,critical_parameters_limit)
            else:
                logging.warning("fing_logs_and_update - critical_parameters_limit is None")
    except:
         logging.exception( "fing_logs_and_update - find_critical_info_and_update ")
      

    # when file is updated for the first time or when it is empty
    if os.stat(file).st_size == 0 or (os.stat(file).st_size != 0 and is_empty_line_present(file)):
        readings = {}
        readings.update({reading_value: dict_cmds})

        if write_to_file(readings, file) == FAILURE:
            raise Exception("File write error: %s",file)
        file_updated_in_current_iteration = 1


    # when file is updated for the consequent readings except the very first time
    else:
        readings = {}
        if read_from_file(readings, file) == FAILURE:
            raise Exception("File read error: %s",file)

        readings.update({reading_value: dict_cmds})

        if write_to_file(readings, file) == FAILURE:
            raise Exception("File write error: %s",file)
        file_updated_in_current_iteration = 1
        #logging.debug("File_updated_in_current_iteration")


    # check if file is updated with new readings and increase the current_count
    if file_updated_in_current_iteration == 1:
        if current_count < max_no_of_readings:
            current_count += 1
        else:
            logging.info("Current count equals to max_no_of_readings ")
            current_count = 1
            # if readings in log file are more than max_no_of_readings, remove the excess readings
            remove_excess_readings(max_no_of_readings, file)


        file_updated_in_current_iteration = 0
    else:
        logging.error("Diagnostics - Reading not updated due to some error")

    return current_count


def is_json_file_present(file):
    """creates the json file if not present"""
    try:
        if not (os.path.isfile(file)):
            open(file, 'a').close()
    except:
        logging.exception(" is_json_file_present")


def backup_file(file, backup_file):
    """copy 'file' to 'backup_file' path"""

    try:
        if os.path.isfile(file):
            shutil.copyfile(file, backup_file)
            readings = {}
            if os.stat(file).st_size != 0:
                if read_from_file(readings, file) == FAILURE:
                    raise Exception("File read error: %s",file)

                current_date_time = str(datetime.now())
                today_date = current_date_time.split(' ')[0]
                logging.debug("today_date : %s", today_date)

                if 'CURRENT_DATE' in readings.keys():
                    current_log_date = str(readings['CURRENT_DATE']['CURRENT_DATE'])
                    logging.debug("current_log_date : %s", current_log_date)
                    if current_log_date != today_date:
                        logging.debug("Date changed from current_log_date")
                        shutil.copyfile(file, backup_file)
                        readings.update({"CURRENT_DATE": {"CURRENT_DATE": today_date}})
                        write_to_file(readings, file)

                else:

                    readings.update({"CURRENT_DATE": {"CURRENT_DATE": today_date}})
                    write_to_file(readings, file)

    except:
        logging.exception("backup_file()")



def main():

    diagnostics_system_events_queues = {}
    logging.info("DIAGNOSTICS - Started")

    if initialize_service(diagnostics_system_events_queues, "lavazza_cfds_diagnostics.service") == FAILURE:
        logging.error("Diagnostics initialization failed")

    logging.info("Diagnostics main - Diagnostics initialized successfully")

    if update_process_id("DIAGNOSTICS") == FAILURE:
        logging.error("DIAGNOSTICS : updating process id")

    current_count_1 = current_count_2 = 1

    #To initiate cpu usage readings from this point of time, this call is required for later measurement of cpu
    psutil.cpu_times_percent()

    feature_configs = {}
    try:
        if read_from_file(feature_configs, FEATURE_CONF_FILE) == SUCCESS:

           
            #logging.debug(feature_configs)

            diagnostics_configs = feature_configs['diagnostics']
            
            #logging.debug(diagnostics_configs)

            detailed_log_commands = diagnostics_configs['detailed_log_commands']
            summary_log_commands = diagnostics_configs['summary_log_commands']
            max_no_of_readings = diagnostics_configs['max_no_of_readings']
            duration_bw_2cycles = diagnostics_configs['duration_bw_2cycles']
            critical_parameters_limit = diagnostics_configs['critical_parameters_limit']

            while 1:
                is_json_file_present(DETAILED_LOG)
                is_json_file_present(SUMMARY_LOG)

                # backup everyday based on date if date is changed
                # need to backup in 24*7 machine based on the below condition
                # if the machine has completed max_no_of_readings from boot and also date has changed
                if current_count_1 == 1:
                    backup_file(DETAILED_LOG, DETAILED_LOG_BACKUP)
                    backup_file(SUMMARY_LOG, SUMMARY_LOG_BACKUP)
                #logging.debug("Updating detailed log")
                current_count_1 = fing_logs_and_update(detailed_log_commands, DETAILED_LOG, current_count_1,
                                                       max_no_of_readings, None)
                #logging.debug("Updating summarylog")
                current_count_2 = fing_logs_and_update(summary_log_commands, SUMMARY_LOG, current_count_2,
                                                       max_no_of_readings,critical_parameters_limit)

                logging.debug("WAIT FOR DURATION")
                #logging.debug("Wait:current_count_1 = %s", current_count_1)
                #logging.debug("Wait:current_count_2 = %s", current_count_2)
                time.sleep(duration_bw_2cycles)



    except:
        logging.exception("Diagnostics - main()")
        if os.path.exists(DETAILED_LOG):
            os.remove(DETAILED_LOG)
        if os.path.exists(SUMMARY_LOG):
            os.remove(SUMMARY_LOG)
        logging.info("After the above exception, deleted DETAILED_LOG & SUMMARY_LOG")
        
        
main()

 
