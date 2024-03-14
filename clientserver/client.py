import socket
import data_formats
from data_formats import student_names
import encryption

# Define host and port - local host uses local IP of computer
HOST = 'localhost'
PORT = 6666


def data_types(dictionary, format):
    if format == 'json':
        data = data_formats.dict_to_json(student_names).encode()
    elif format == 'xml':
        data = data_formats.dict_to_xml(dictionary)
    elif format == 'binary':
        data = data_formats.dict_to_binary(dictionary)
    elif format == 'txt':
        data = encryption.open_file().encode()
    return data


def send_data(format, encrypt=False):
    # Creates a socket object - AF_INET specifies IPv4 - SOCK_STREAM specifies TCP socket type
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

        # Connects client to server
        client_socket.connect((HOST, PORT))

        # Calling the data_types function in this script to choose the data type
        data_sent = data_types(student_names, format)

        # If encryption is required
        if encrypt:
            data_sent = data_sent.decode()
            data_sent = encryption.symmetric_encryption(data_sent)

        # Sends data to server
        client_socket.sendall(data_sent)

        # Copy of data that server recieved
        data = client_socket.recv(1024)

    # Decodes data by converting bytes to string then printing
    # (needs adjusting for other file types e.g. JSON, binary etc)
    if format == 'binary':
        print(f"Server has recieved data. Copy of data recieved: {data}")
    else:
        print(f"Server has recieved data. Copy of data recieved: {data.decode()}")


if __name__ == '__main__':
    # Select which data type to be sent to the server
    # Options: json, xml, binary, txt
    format = 'binary'

    # Select if the data is to be encrypted
    # Options: True, False
    encrypt = False

    # Call the main script
    send_data(format, encrypt)
