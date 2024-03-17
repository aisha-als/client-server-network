import socket
import data_formats
from data_formats import student_names
import encryption

# Define host and port - local host uses local IP of computer
HOST = 'localhost'
PORT = 6666


def data_types(dictionary, format):
    """
    Takes a dictonary and converts to chosen format.

    Arguments:
    dictionary - The raw data in a dictionary format
    format - The chosen format to convert the dictonary to
    """
    try:
        if format == 'json':
            data = data_formats.dict_to_json(dictionary).encode()
        elif format == 'xml':
            data = data_formats.dict_to_xml(dictionary)
        elif format == 'binary':
            data = data_formats.dict_to_binary(dictionary)
        elif format == 'txt':
            data = encryption.open_file().encode()
        else:
            raise ValueError("Invalid format specified")
        return data
    except Exception as e:
        print(f"An error in data_types function has occured: {e}")
        return None


def send_data(format, encrypt=False):
    """
    Connects to server and sends data.

    Arguments:
    format - The chosen format the dictionary was converted to.
    encrypt - Whether or not to encrypt the file, default = false.
    """
    try:
        # Creates a socket object - AF_INET specifies IPv4 - SOCK_STREAM specifies TCP socket type
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

            # Connects client to server
            client_socket.connect((HOST, PORT))

            # Calling the data_types function in this script to choose the data type
            data_sent = data_types(student_names, format)
            if data_sent is None:
                return 1

            # If encryption is required
            if encrypt:
                data_sent = data_sent.decode()
                data_sent = encryption.symmetric_encryption(data_sent)

            # Sends data to server
            client_socket.sendall(data_sent)

            # Copy of data that server recieved
            data = client_socket.recv(1024)

        # Decodes data by converting bytes to string then printing
        if format == 'binary':
            print(f"Server has recieved data. Copy of data recieved: {data}")
        else:
            print(f"Server has recieved data. Copy of data recieved: {data.decode()}")
        
        # Program successful, return 0
        return 0
        
    except ConnectionRefusedError as cre:
        print(f"A connection error has occured: {cre}. Please check that the server is running.")
        return 1
    except socket.error as se:
        print(f"A socket error has occured: {se}")
        return 1
    except Exception as e:
        print(f"An error in send_data function has occured: {e}")
        return 1


if __name__ == '__main__':
    # Select which data type to be sent to the server
    # Options: json, xml, binary, txt
    format = 'txt'

    # Select if the data is to be encrypted
    # Options: True, False
    encrypt = True

    # Call the main script
    err = send_data(format, encrypt)
    if err != 0:
        print('Program halted because of an error')
    else:
        print('Program ran successfully')
