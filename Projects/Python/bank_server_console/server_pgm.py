import socket
#import Json_handler
from _thread import *
import os 
import json
import multiprocessing

server = socket.socket()
host = socket.gethostname()
port = 5005
server.bind((host,port))
server.listen(2)

Lock = multiprocessing.Lock()

def Read_File(filepath):
    try : 
        if os.path.isfile(filepath):
            with open(filepath,'r') as json_file :
                Lock.acquire()
                file_txt = json_file.read()
                read_content = json.loads(file_txt)
                Lock.release()
    except Exception as error :
        print(error)
    return read_content

def Write_File(filepath,content):
    try :
        if os.path.isfile(filepath):
            Lock.acquire()
            with open(filepath,'w') as json_file :
                json_file.write(json.dumps(content,indent = 4,separators = ',:'))
                Lock.release()
    except Exception as error:
        print(error)

    return 'success'    

def Withdrawal_Module(client):
    Main_Database = Read_File("Server_Entries.json")
    Ac_No = client.recv(1024).decode()
    Amount = client.recv(1024).decode()
    for users in Main_Database :
        user = Main_Database[users]
        for details in user.values() :
            if details == Ac_No :
                User_Name = users
    Balance_Amount = Main_Database[User_Name]["Bank_Balance"]
    Remaining_Balance = Main_Database[User_Name]["Bank_Balance"] - int(Amount)
    if int(Amount) < Balance_Amount :
        Main_Database[User_Name]["Bank_Balance"] -= int(Amount)
        client.send("\nSuccessfully Debited".encode())
    else :
        client.send("\nInsufficient_Balance".encode())
    if client.recv(1024).decode() == "Show_Balance" :
        client.send(f"\nRemaining_Balance : {Remaining_Balance}".encode())
    else :
        pass
    Write_File("Server_Entries.json",Main_Database)
    #Json_handler.Basic_Functions.Write_File("Server_Entries.json",Main_Database)

def Deposit_Module(client):
    Main_Database = Read_File("Server_Entries.json")
    Ac_No = client.recv(1024).decode()
    Amount = client.recv(1024).decode()
    for users in Main_Database :
        user = Main_Database[users]
        for details in user.values():
            if Ac_No == details :
                User_Name = users
    Main_Database[User_Name]["Bank_Balance"] += int(Amount)
    client.send("\nSuccessfully Credited".encode())
    Write_File("Server_Entries.json",Main_Database)

def Init_Function(client):
    User_Option = client.recv(1024).decode()
    if User_Option == '1':
        Withdrawal_Module(client)
    if User_Option == '2':
        Deposit_Module(client)

while True :
    client,address = server.accept()
    print(f"Connected with client {address}")
    start_new_thread(Init_Function,(client,))



