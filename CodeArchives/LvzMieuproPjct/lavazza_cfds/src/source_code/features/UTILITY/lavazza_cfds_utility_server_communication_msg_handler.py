import lavazza_cfds_utility_macros
import logging
import pyqrcode


def generate_qr_code():

    try:

        logging.debug("--- generate_qr_codefunction started ------")

        if lavazza_cfds_utility_macros.read_from_file(
                lavazza_cfds_utility_macros.feature_configs, lavazza_cfds_utility_macros.FEATURE_CONF_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("File reading error in " + lavazza_cfds_utility_macros.FEATURE_CONF_FILE)

        qr_code_url = lavazza_cfds_utility_macros.feature_configs["server_info"]["qr_code"]
        logging.debug("qr_code_url - {}".format(qr_code_url))

        device_info = {}
        # read the DEVICE_PROVISION_INFO_FILE to get the device type info
        if lavazza_cfds_utility_macros.read_from_file(device_info,
                                                 lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE) == lavazza_cfds_utility_macros.FAILURE:
            raise Exception("File reading error in ", lavazza_cfds_utility_macros.DEVICE_PROVISION_INFO_FILE)

        device_id = device_info["device_id"]
        logging.debug("device_id - {}".format(device_id))

        # String which represents the QR code

        if device_info["device_mode"] == lavazza_cfds_utility_macros.INTERNET_MODE:
            qr_string = qr_code_url+"?deviceId=" + lavazza_cfds_utility_macros.obfuscate(device_id)
            scale = 4

        else:
            qr_string = "http://192.168.5.1:9876/"
            scale = 6
            
        logging.info("qr_string - {}".format(qr_string))

        # Generate QR code
        url = pyqrcode.create(qr_string)

        # Create and save the png file naming "web_app_qr_code.png"
        qr_file_name = lavazza_cfds_utility_macros.QR_CODE_IMAGE
        url.png(qr_file_name, scale=scale)
        logging.debug("QR code generated Successfully")

        logging.debug("--- generate_qr_code function finished ------")
        return lavazza_cfds_utility_macros.SUCCESS

    except Exception as error:
        logging.exception("Error occurred while creating qr code")
        return lavazza_cfds_utility_macros.FAILURE
