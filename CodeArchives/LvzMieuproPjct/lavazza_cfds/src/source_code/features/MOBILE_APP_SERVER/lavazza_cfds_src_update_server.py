import json
import time
import subprocess
import logging
from threading import Thread
from flask import request, jsonify, render_template, make_response, Blueprint
from lavazza_cfds_mobile_app_server_macros import *

logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - Mobile_App_Backend - %(levelname)s - %(message)s',
                    filename=LAVAZZA_COMMON_LOG_FILE, filemode='a')

src_update = Blueprint('src_update', __name__)

update_config = None
update_status = None
device_provision_info = None


@src_update.route('/fileupload')
def index():
    # Route to serve the upload form
    if device_provision_info["network_mode"] == MACHINE_WIFI:
        return render_template("file_upload.html", ip="192.168.5.1:9876")
    elif device_provision_info["network_mode"] == ORGANIZATION_WIFI:
        wifi_config = {}
        if read_from_file(wifi_config, WIFI_CONF_FILE) == FAILURE:
            logging.exception("WIFI_CONFIG_FILE read error")
            return "<h1>Something went wrong(may be config file read error) !!</h1>"
        return render_template("file_upload.html", ip=wifi_config["ip_address"] + ":9876")
    else:
        return "<h1> invalid wifi mode configured !!</h1>"


@src_update.route('/upload', methods=['POST'])
def upload():
    global update_config

    try:
        file = request.files['file']

        file_name = file.filename
        file_ext = file_name[-3:]
        logging.info("Filename - {}".format(file.filename))

        if file_ext != "zip":
            return make_response(("File not allowed", 400))

        if file_name.split("_")[0] != "src":
            return make_response(("File not allowed", 400))

        save_path = os.path.join(UPDATE_PATH, file.filename)
        current_chunk = int(request.form['dzchunkindex'])

        # If the file already exists it's ok if we are appending to it,
        # but not if it's new file that would overwrite the existing one
        if os.path.exists(save_path) and current_chunk == 0:
            # 400 and 500s will tell dropzone that an error occurred and show an error
            return make_response(("File already exists", 400))

        try:
            with open(save_path, 'ab') as f:
                f.seek(int(request.form['dzchunkbyteoffset']))
                f.write(file.stream.read())
        except OSError:
            # log.exception will include the traceback so we can see what's wrong
            logging.info("Could not write to file")
            return make_response(("Couldn't write the file to disk", 500))

        total_chunks = int(request.form['dztotalchunkcount'])

        if current_chunk + 1 == total_chunks:
            # This was the last chunk, the file should be complete and the size we expect
            if os.path.getsize(save_path) != int(request.form['dztotalfilesize']):
                logging.info("File {} was completed, but has a size mismatch.".format(file.filename))
                logging.info("Actual File Size : {}".format(os.path.getsize(save_path)))
                logging.info("Expected File Size : {}".format(request.form['dztotalfilesize']))

                return make_response(('Size mismatch', 500))
            else:
                update_config["update_files"].append(file_name)
                update_config["new_update"] = True
                logging.info(update_config)
                write_update_config()
                logging.info("File {} has been uploaded successfully".format(file.filename))
        else:
            logging.info("Chunk {} of {} for file {} complete".format(current_chunk + 1, total_chunks, file.filename))

        return make_response(("Chunk upload successful", 200))

    except Exception as error:
        logging.info("File Upload Error : {}".format(error))
        return make_response(("File upload error", 400))


@src_update.route('/update', methods=['GET'])
def update():
    global update_config
    try:
        token_id = request.headers.get("tokenId")
        if token_id == MOBILE_APP_TOKEN:
            if update_config["new_update"] == True:
                src_update_handler_t = Thread(target=src_update_handler, args=())
                src_update_handler_t.start()
                return jsonify(status=SUCCESS), 200
            else:
                return jsonify(status=FAILURE), 200
        else:
            return jsonify(status=FAILURE), 400

    except Exception as error:
        logging.info("Update Error : {}".format(error))
        return jsonify(status=FAILURE), 400


@src_update.route('/revert', methods=['GET'])
def revert_update():
    global update_config
    try:
        token_id = request.headers.get("tokenId")
        if token_id == MOBILE_APP_TOKEN:
            if update_config["revert"] == True:
                revert_update_handler_t = Thread(target=revert_update_handler, args=())
                revert_update_handler_t.start()
                return jsonify(status=SUCCESS), 200
            else:
                return jsonify(status=FAILURE), 200
        else:
            return jsonify(status=FAILURE), 400

    except Exception as error:
        logging.info("Update Revert Error : {}".format(error))
        return jsonify(status=FAILURE), 400


@src_update.route('/deleteZip', methods=['GET'])
def delete_corrupt_zip():
    global update_config
    try:
        token_id = request.headers.get("tokenId")
        if token_id == MOBILE_APP_TOKEN:
            del_corrupt_zip_t = Thread(target=del_corrupt_files, args=())
            del_corrupt_zip_t.start()
            return jsonify(status=SUCCESS), 200
        else:
            return jsonify(status=FAILURE), 400

    except Exception as error:
        print("Deleting corrupt zip file Error : {}".format(error))
        return jsonify(status=FAILURE), 400


@src_update.route('/newUpdate', methods=['GET'])
def check_new_update():
    global update_config
    try:
        token_id = request.headers.get("tokenId")
        if token_id == MOBILE_APP_TOKEN:
            if update_config["new_update"] == True:
                return jsonify(status=SUCCESS), 200
            else:
                return jsonify(status=FAILURE), 200
        else:
            return jsonify(status=FAILURE), 400

    except Exception as error:
        logging.info("Update check Error : {}".format(error))
        return jsonify(status=FAILURE), 400


@src_update.route('/getUpdateConfig', methods=['GET'])
def get_update_config():
    global update_config
    try:
        token_id = request.headers.get("tokenId")
        if token_id == MOBILE_APP_TOKEN:
            return jsonify(status=SUCCESS, data=update_config, tech_id=TECH_ID, tech_pwd=TECH_PASS,
                           device_info=device_provision_info), 200
        else:
            return jsonify(status=FAILURE), 400

    except Exception as error:
        logging.info("Getting Update Config Error : {}".format(error))
        return jsonify(status=FAILURE), 400


@src_update.route('/getUpdateStatus', methods=['GET'])
def get_update_status():
    global update_config
    try:
        token_id = request.headers.get("tokenId")
        if token_id == MOBILE_APP_TOKEN:
            return jsonify(status=SUCCESS, data=update_status), 200
        else:
            return jsonify(status=FAILURE), 400

    except Exception as error:
        logging.info("Getting Update Status Error : {}".format(error))
        return jsonify(status=FAILURE), 400


def del_corrupt_files():
    global update_config, update_status

    try:
        zip_files = [f for f in os.listdir(UPDATE_PATH) if f.endswith('.zip')]
        print(zip_files)

        if len(zip_files) == len(update_config["update_files"]):
            update_status = "No Corrupted zip files to delete"
            print(update_status)
            return

        for file in zip_files:
            if file not in update_config["update_files"]:

                file_del_cmd = "rm -rf " + str(UPDATE_PATH) + "/" + file

                if shell_cmd_executor(file_del_cmd) == "success":
                    print("Corrupted zip {} deleted successfully".format(file))
                else:
                    print("Corrupted zip {} deletion failed".format(file))

        update_status = "Corrupted zip deleted successfully"

    except Exception as error:
        update_status = "Error deleting corrupted zip files"
        print("Corrupted zip deletion Error : {}".format(error))

    print(update_status)
    return


def src_update_handler():
    global update_config, update_status

    src_path = str(UPDATE_PATH) + "/src"
    if os.path.exists(src_path):
        pass
    else:
        update_status = "No source folder to replace"
        print("--------No src folder to replace---------")
        return

    update_config["new_update"] = False
    logging.info(update_config)
    write_update_config()

    update_status = "Update in Progress"

    try:
        file_to_be_updated = update_config["update_files"].pop()
        logging.info("-----------------File to be updated ------------------------")
        logging.info(file_to_be_updated)

        if update_config["revert"] == True:
            update_config["revert"] = False
            write_update_config()
            file_del_cmd = "rm -rf " + str(UPDATE_PATH) + "/" + "prev_src"
            if shell_cmd_executor(file_del_cmd) == "success":
                update_status = "Prev src files deleted"
                logging.info("Prev src deleted successfully")
            else:
                logging.info("Prev src deletion failed")

    except Exception as error:
        logging.info("Deleting previous src folder error : {}".format(error))
        update_status = "Error deleting previous src or accessing update config list"
        return

    def unzip_error_handler():
        global update_status

        try:
            file_del_cmd = "rm -rf " + str(UPDATE_PATH) + "/" + str(filename)
            if shell_cmd_executor(file_del_cmd) == "success":

                update_status = "Error extracting file or file not allowed"
                logging.info("Error extracting file or file not allowed")
                logging.info("Deleting intermediate extracted folders")

                file_del_cmd = "rm -rf " + str(UPDATE_PATH) + "/" + str(file_to_be_updated)
                if shell_cmd_executor(file_del_cmd) == "success":
                    update_status = "Error extracting file or file not allowed"
                    logging.info("Deleting source zip")
                else:
                    update_status = "Something went wrong"
            else:
                update_status = "Something went wrong"

            update_config["update_files"] = []
            write_update_config()

        except Exception as error:
            logging.info("Error extracting file or file not allowed error : {}".format(error))
            update_status = "Error extracting file or file not allowed"

        return

    # Delete previous version files
    try:
        if len(update_config["update_files"]) > 0:
            for file in update_config["update_files"]:
                logging.info("=======File to be deleted======")
                logging.info(file)
                file_del_cmd = "rm -rf " + str(UPDATE_PATH) + "/" + str(file)
                if shell_cmd_executor(file_del_cmd) == "success":
                    time.sleep(0.2)
                else:
                    update_status = "Error deleting previous files"
                    return

            update_config["update_files"] = []
            logging.info("----------Previous versions deleted successfully----------------")

    except Exception as error:
        logging.info("Deleting previous update files error : {}".format(error))
        update_status = "Error deleting previous files"
        return

    # Get extraction password
    try:
        filename = file_to_be_updated[0:-4]
        file_info = filename.split("_")

        zip_pwd = ""
        for i in file_info[2]:
            pwd_char = PASS_STR.find(i)
            if pwd_char != -1:
                zip_pwd = zip_pwd + str(pwd_char)
            else:
                logging.info("Password mismatch")
                update_status = "File not allowed"
                return

        logging.info("-----------Zip password acquired successfully------------")

    except Exception as error:
        logging.info("Password extraction error : {}".format(error))
        update_status = "Error in extracting file"
        return

    # Unzip the update file
    try:
        file_to_unzip = str(UPDATE_PATH) + "/" + str(file_to_be_updated)
        unzip_cmd = "unzip -P " + str(zip_pwd) + " " + file_to_unzip + " " + "-d " + str(UPDATE_PATH)
        if shell_cmd_executor(unzip_cmd) == "success":
            time.sleep(0.3)
            logging.info("-----------Files has been unzipped successfully-------------")
        else:
            unzip_error_handler()
            return

    except Exception as error:
        logging.info("Password extraction error : {}".format(error))
        unzip_error_handler()
        return

    # Move src to prev_src
    try:
        # moving current src to prev_src folder
        source = str(UPDATE_PATH) + "/" + "src"
        dest = str(UPDATE_PATH) + "/" + "prev_src"
        mv_cmd = "mv " + source + " " + dest
        if shell_cmd_executor(mv_cmd) == "success":
            time.sleep(0.3)
        else:
            update_status = "Something went wrong"
            return

        # moving src_ver_pass to src folder
        source = str(UPDATE_PATH) + "/" + str(filename)
        dest = str(UPDATE_PATH) + "/" + "src"
        mv_cmd = "mv " + source + " " + dest
        if shell_cmd_executor(mv_cmd) == "success":
            time.sleep(0.3)
        else:
            update_status = "Something went wrong"
            return

        # deleting src_ver_pass.zip
        file_del_cmd = "rm -rf " + str(UPDATE_PATH) + "/" + str(file_to_be_updated)
        if shell_cmd_executor(file_del_cmd) == "success":
            time.sleep(0.3)
        else:
            update_status = "Something went wrong"
            return

        logging.info("-----------Files operation has been done successfully-------------")

    except Exception as error:
        logging.info("File Update error : {}".format(error))
        update_status = "Something went wrong"
        return

    update_config["previous_version"] = str(update_config["current_version"])
    update_config["current_version"] = str(file_info[1])
    update_config["revert"] = True
    update_config["update_files"] = []
    write_update_config()

    update_status = "Updated successfully"

    logging.info("Version Update")
    logging.info(update_config)

    return


def revert_update_handler():
    global update_config, update_status

    update_status = "Reverting update in Progress"

    # Move src to prev_src
    try:
        # moving current src to rm_src folder
        source = str(UPDATE_PATH) + "/" + "src"
        dest = str(UPDATE_PATH) + "/" + "rm_src"
        mv_cmd = "mv " + source + " " + dest
        if shell_cmd_executor(mv_cmd) == "success":
            time.sleep(0.3)
        else:
            update_status = "Something went wrong"
            return

        # moving prev_src to src folder
        source = str(UPDATE_PATH) + "/" + "prev_src"
        dest = str(UPDATE_PATH) + "/" + "src"
        mv_cmd = "mv " + source + " " + dest
        if shell_cmd_executor(mv_cmd) == "success":
            time.sleep(0.3)
        else:
            update_status = "Something went wrong"
            return

        # deleting rm_src folder
        file_del_cmd = "rm -rf " + str(UPDATE_PATH) + "/" + "rm_src"
        if shell_cmd_executor(file_del_cmd) == "success":
            time.sleep(0.3)
        else:
            update_status = "Something went wrong"
            return

        logging.info("-----------Revert Files operation has been done successfully-------------")

    except Exception as error:
        logging.info("Revert Update error : {}".format(error))
        update_status = "Something went wrong"
        return

    current_ver = str(update_config["current_version"])
    update_config["current_version"] = str(update_config["previous_version"])
    update_config["previous_version"] = current_ver
    update_config["revert"] = False
    write_update_config()

    update_status = "Update has been reverted successfully"
    logging.info("Revert Update")
    logging.info(update_config)

    return


def shell_cmd_executor(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()
    if process.returncode == 0:
        return "success"
    else:
        return "failure"


def read_update_config(device_provision_info_param):
    global update_config, device_provision_info

    device_provision_info = device_provision_info_param

    logging.info("Reading from update config file")
    with open(UPDATE_CONFIG_FILE) as file:
        update_config = json.load(file)


def write_update_config():
    global update_config

    logging.info("Writing to update config file")
    with open(UPDATE_CONFIG_FILE, 'w') as outfile:
        json.dump(update_config, outfile)
