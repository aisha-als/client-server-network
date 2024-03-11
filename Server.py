import socket

#Define host and port - local host uses local IP of computer
HOST = 'localhost'
PORT = 6666

#Creates a socket object - AF_INET specifies IPv4 - SOCK_STREAM specifies TCP socket type
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    #Binds server_socket to the host and port defined above
    server_socket.bind ((HOST,PORT))

    #Starts listening for incoming connections
    server_socket.listen()

    print(f"Server is listening for connections to {HOST}:{PORT}")


    #Accepts incoming connections
    connection, address = server_socket.accept()

    with connection:
        print(f"Server connected to {address}")

        #Receives data from client side - 1024 represents max number of bytes that can be recieved at once
        while True:
            data = connection.recv(1024)

            #If data recieved is empty, then will break loop
            if not data:
                break

            #Decodes data by converting bytes to string then printing (needs adjusting for other file types e.g. JSON, binary etc)
            print(f"Data recieved: {data.decode()}")
            
            #Sends a copy of the data recieved back to client to confirm its receipt
            connection.sendall(data)