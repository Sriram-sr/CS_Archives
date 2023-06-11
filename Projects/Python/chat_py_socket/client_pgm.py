import socket 

host = socket.gethostname()
port = 45680

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host,port))
    while True:
        server_message = client.recv(1024).decode()
        if server_message or server_message=='':
            if server_message == 'bye' or server_message == '' or server_message == 'Bye':
                print('\n Server Quitted')
                break
        print('Server: ', server_message)
        client_input = input("Client: ")
        client.send(client_input.encode())
        if client_input=='' or client_input=='Bye' or client_input=='bye':
            break



