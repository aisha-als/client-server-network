import socket

# Define host and port - local host uses local IP of computer
HOST = 'localhost'
PORT = 6666

# Creates a socket object - AF_INET specifies IPv4 - SOCK_STREAM specifies TCP socket type
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

    # Connects client to server
    client_socket.connect((HOST, PORT))

    # Sends data to server
    client_socket.sendall()

    # Copy of data that server recieved
    data = client_socket.recv(1024)

# Decodes data by converting bytes to string then printing (needs adjusting for other file types e.g. JSON, binary etc)
print(f"Server has recieved data. Copy of data recieved: {data.decode()}")
