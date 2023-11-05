import re, codecs, logging, json
import pathlib, datetime, time
from subprocess import Popen, PIPE
from lavazza_cfds_server_communication_macros import BASE_DIRECTORY,LAVAZZA_COMMON_LOG_FILE
'''
logging.basicConfig(level=10,
                    format='%(asctime)s - SIGNAL_STRENGTH - signal strength - %(levelname)s - %(message)s',
                    filename=LAVAZZA_COMMON_LOG_FILE,filemode='a')'''
SUCCESS = 0
FAILURE = -1
essid = "MIEUPRO"
file_to_write=BASE_DIRECTORY+"tmp/strength.json"
file_to_read=BASE_DIRECTORY+"src/configs/device_configs/wifi_config.json"
# data1={}
# read_from_file(data1,"/usr/lib/.lvz_ocb/src/configs/device_configs/wifi_config.json")

def command_execute_function(cmd):
    try:
        process = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        global stdout, stderr
        stdout, stderr = process.communicate()
        if stderr:
            return stderr
        elif stdout:
            return stdout
    except Exception as error:
        logging.exception("error occured while executing cmd ==> {}".format(error))
        return FAILURE


def read_from_file(data,file_to_read):
    """ Reads data from file """
    with open(file_to_read) as file:
        data.update(json.load(file))

def write_to_file(data,file_to_write):
    with open(file_to_write,"w") as file:
        file.write(json.dumps(data))

def signal_strength():
    try:
        data = command_execute_function("iwlist {} scan".format("wlan0"))
        if data != FAILURE:
            data = (codecs.decode(data, 'unicode_escape'))
            essid_found_list = re.findall("ESSID.*", data)
            frequency_found_list = re.findall("Frequency.*GHz", data)
            quality_found_list = re.findall("Quality.*[\d]/[\d]{1,2}", data)
            signal_found_list = re.findall("Signal.*dBm", data)

            wifi_data={}
            read_from_file(wifi_data,file_to_read)
            essid=wifi_data["SSID"]
            match_index=essid_found_list.index("ESSID:\""+essid+"\"")

            signal_strength = {}
            signal_strength["time calculated: "]=str(datetime.datetime.now())
            signal_strength[essid_found_list[match_index].split(":")[0]] = \
            essid_found_list[match_index].split(":")[1]
            signal_strength[frequency_found_list[match_index].split(":")[0]] = \
                frequency_found_list[match_index].split(":")[1]
            signal_strength[quality_found_list[match_index].split("=")[0]] = str(
                round((int((quality_found_list[match_index].split("=")[1]) \
                           .split("/")[0]) / int((quality_found_list[match_index].split("=")[1]) \
                                                 .split("/")[1]) * 100), 2)) + " %"
            signal_strength[signal_found_list[match_index].split("=")[0]] = \
            signal_found_list[match_index].split("=")[1]

            signal_strength_int = int((re.findall('[\d]+', signal_found_list[match_index].split("=")[1]))[0])
            if(signal_strength_int in range(0,35)):
                strength_point=4
            elif(signal_strength_int in range(35,45)):
                strength_point=3
            elif(signal_strength_int in range(45,55)):
                strength_point=2
            elif(signal_strength_int in range(55,75)):
                strength_point=1
            else:
                strength_point=0
            signal_strength["signal_point"]=int(strength_point)
            write_to_file(signal_strength,file_to_write)
            logging.info("signal details {}".format(signal_strength))
        else:
            logging.error("error occured while scanning the interface")


    except Exception as error:
        signal_strength={}
        signal_strength["time calculated: "]=str(datetime.datetime.now())
        signal_strength['Signal level']="- dBm"
        signal_strength["signal_point"]="-"
        write_to_file(signal_strength,file_to_write)
        logging.exception("error occured ==> {}".format(error))

def start_signal_strength():
    logging.info("signal strength thread started")
    while True:
        signal_strength()
        time.sleep(300)
#start_signal_strength()
