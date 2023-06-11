import json
import pathlib
import os
import logging

json_file_path = pathlib.Path(__file__).parent.resolve()/'db.json'
log_file_path = pathlib.Path(__file__).parent.resolve()/'app.log'

logging.basicConfig(filename= log_file_path, level=logging.INFO,
                    format='%(asctime)s- %(levelname)s - %(message)s') 

def send_text(client, content):
    client.send(content.encode())

def send_object(client, content):
    serialized_content = json.dumps(content)
    client.send(serialized_content.encode())

def receive_text(client):
    content = client.recv(1024).decode()
    return content

def receive_object(client):
    plain_content = client.recv(1024).decode()
    json_content = json.loads(plain_content)
    return json_content

def read_json():
    content = {}
    try:
        if os.path.isfile(json_file_path):
            with open(json_file_path, 'r') as json_file:
                file_text = json_file.read()
                content = json.loads(file_text)
                logging.info('Read file Success')
        else:
            pass
            logging.error('Read file path does not exist')
    except Exception as error:
        print(error)
        return error

    return content

def write_json(content):
    try:
        if os.path.isfile(json_file_path):
            with open(json_file_path, 'w+') as json_file:
                json_file.write(json.dumps(content))
                logging.info('Write file Success')
        else:
            pass
            logging.error('Read file path does not exist')

    except Exception as error:
        print(error)
        return error

