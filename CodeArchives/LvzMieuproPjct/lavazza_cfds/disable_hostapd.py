from subprocess import Popen, PIPE

SUCCESS = 0
FAILURE = -1
DENY_INTERFACES = 'denyinterfaces wlan0'
ALLOW_INTERFACE = 'auto lo\niface lo inet loopback\n\nauto eth0\niface eth0 inet dhcp\n\nallow-hotplug wlan0\niface wlan0 inet static\n    address 192.168.5.1\n    netmask 255.255.255.0\n    network 192.168.5.0\n    broadcast 192.168.5.255'
HOSTAPD_ENABLE = 'DAEMON_CONF="/etc/hostapd/hostapd.conf"'
ENABLE_CMD = 'systemctl enable hostapd.service'
DISABLE_CMD = 'systemctl disable hostapd.service'

def read_from_system_file(data, file_to_read):
    """ Reads data from system file """
    try:
        with open(file_to_read) as file:
            data.append(file.read())
        return SUCCESS
    except Exception as error:
        #logging.exception("Read from file - Error %s : ", error)
        print("Read from file - Error : ", error)
        return FAILURE


def write_to_system_file(data, file_to_write, mode):
    """ Writes data to file """
    try:
        #print(data)
        with open(file_to_write,mode) as file:
            #file = open(file_to_write, mode)
            file.write(data)
        return SUCCESS
    except Exception as error:
        #logging.exception("Write to file: %s", file_to_write)
        print("Write to file - Error : ", error)
        return FAILURE

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

    except Exception as Error:
        print("Command Executor - Execution failed for the command :: ", command)
        print("Command Executor - Error : ", Error)
        #logging.exception("Command Executor - Execution failed for the command :: %s",command)
        return FAILURE
		
		
def disable_hotspot():
    try:
        dhcpcd_conf_file_data = []
        if read_from_system_file(dhcpcd_conf_file_data,
                                                             "/etc/dhcpcd.conf") == FAILURE:
            print("Error occured while reading dhcpcd conf file")
            return FAILURE
        #print(dhcpcd_conf_file_data)
        splitted_dhcpcd_data = dhcpcd_conf_file_data[0].split("\n")
        while("" in splitted_dhcpcd_data) : 
            splitted_dhcpcd_data.remove("") 
        if(splitted_dhcpcd_data[-1] == DENY_INTERFACES):
            #print(new_dhcpcd_data)
            new_dhcpcd_data = "\n".join(splitted_dhcpcd_data[:-1])
        else:
            new_dhcpcd_data = "\n".join(splitted_dhcpcd_data[:])
        print("new_dhcpcd_data",new_dhcpcd_data)
        if write_to_system_file(new_dhcpcd_data, "/etc/dhcpcd.conf",
                                                            'w+') == FAILURE:
            print("Error occured while writing to dhcpcd conf file")
            return FAILURE
        if write_to_system_file('', "/etc/network/interfaces",
                                                            'w') == FAILURE:
            print("Error occured while writing to interface conf file")
            return FAILURE
        if write_to_system_file('', "/etc/default/hostapd",
                                                            'w') == FAILURE:
            print("Error occured while writing to hostapd conf file")
            return FAILURE
        cmd_output = {}
        if command_executor(cmd_output, DISABLE_CMD) != SUCCESS:
            return FAILURE
        print("Successfuy disabled")
        return SUCCESS
    except Exception as error:
        print("error in disable hotspot : {} ".format(error))
        return FAILURE
disable_hotspot()
