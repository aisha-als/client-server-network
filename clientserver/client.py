import socket
import data_formats
from data_formats import student_names
import encryption

# Define host and port - local host uses local IP of computer
HOST = 'localhost'
PORT = 6666


def data_types(dictionary, format):
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

            # Inform the user that the data has been sent and waiting for server response
            print("\nFollowing data has been sent to the server.\n")
            print(data_sent)
            print("\nStatus: Waiting for server response...")

            # Copy of data that server recieved
            data = client_socket.recv(1024)

        # Decodes data by converting bytes to string then printing
        if format == 'binary':
            print(f"\nServer has recieved data.\nCopy of data recieved: {data}")
        else:
            print(f"\nServer has recieved data.\nCopy of data recieved: {data.decode()}")
        
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
    # Data type selection
    data_type_selection = {
        '1': 'json',
        '2': 'xml',
        '3': 'binary',
        '4': 'txt',
    }

    while True:
        data_type_input = input("What data type do you want to send?\n"
                                "Enter 1 for JSON\n"
                                "Enter 2 for XML\n"
                                "Enter 3 for Binary\n"
                                "Enter 4 for TXT\n"
                                "Your choice: ")
        if data_type_input in data_type_selection:
            format = data_type_selection[data_type_input]
            break
        else:
            print("ERROR: Wrong option selected")

    # Initialize encryption preference to False
    encrypt = False

    # Encryption preference - only if TXT is selected
    if format == 'txt':
        while True:
            encrypt_input = input("Do you want to encrypt the data? (Enter Y/N): ")
            if encrypt_input.strip().lower() in ('y', 'n'):
                encrypt = True if encrypt_input.strip().lower() == 'y' else False
                break
            else:
                print("ERROR: Wrong option selected")

    # Call the main function with the user inputs
    err = send_data(format, encrypt)
    if err != 0:
        print('Program halted because of an error')
    else:
        print('Program ran successfully')
