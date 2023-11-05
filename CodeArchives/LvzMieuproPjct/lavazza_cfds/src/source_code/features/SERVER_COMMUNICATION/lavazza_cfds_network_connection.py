import logging
import socket
from lavazza_cfds_server_communication_macros import *


def check_internet_connection(iface):
    for test_number in range(3):
        try:
            with socket.socket() as s:
                # Forcing the socket to use Wi-Fi interface
                s.setsockopt(socket.SOL_SOCKET, 25, str(iface).encode('utf-8'))
                # Getting DNS Address
                host_ip = socket.gethostbyname(HOSTS[test_number])
                # Creating a dummy connection with host
                connection = socket.create_connection((host_ip, PORT), 2)
                connection.close()
                # If there was no error
                return True
        except Exception as error:
            logging.error(HOSTS[test_number])
            logging.error(error)
            # If it is the last host
            if test_number == 2:
                return False
            continue


def check_connectivity(interface):
    try:
        logging.debug("check connectivity : {} connectivity check".format(interface))
        route_file_data = []
        if read_from_system_file(route_file_data, ROUTE_FILE) == FAILURE:
            logging.exception("Error occurred while reading route conf file")
            return False
        iface_connect_status = route_file_data[0].find(interface)
        logging.debug("check connectivity: connection status code - {}".format(iface_connect_status))
        if iface_connect_status > -1:
            logging.debug("check connectivity: connection status - True")
            return check_internet_connection(interface)

        else:
            logging.debug("check connectivity: connection status - False")
            return False
    except Exception as error:
        logging.exception("Wifi_Connection : {}".format(error))
        return False


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
