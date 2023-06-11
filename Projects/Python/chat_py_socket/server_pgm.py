import socket

host = socket.gethostname()
port = 45680

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((host,port))
    server.listen()
    client, address = server.accept()
    print('Connected with ', address[0])
    with client:
        while True:
            server_input = input("Server: ")
            client.send(server_input.encode())
            if server_input == '' or server_input == 'bye' or server_input == 'Bye':
                break
            client_message = client.recv(1024).decode()
            if client_message or client_message=='':
                if client_message=='bye' or client_message=='' or client_message=='Bye':
                    print('\n Client Quitted')
                    break
            print('Client: ', client_message)



