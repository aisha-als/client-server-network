import socket
import data_formats
from data_formats import student_names
import encryption

# Define host and port - local host uses local IP of computer
HOST = 'localhost'
PORT = 6666

def get_data_type_selection():
    """
    Prompts the user to select a data type to send.
    Returns:
        format (str): The selected data format.
    """
    data_type_selection = {
        '1': 'json',
        '2': 'xml',
        '3': 'binary',
        '4': 'txt',
    }
    prompt = "\n".join([
        "What data type do you want to send?",
        "Enter 1 for JSON",
        "Enter 2 for XML",
        "Enter 3 for Binary",
        "Enter 4 for TXT",
        "Your choice: "
    ])

    while True:
        data_type_input = input(prompt)
        if data_type_input in data_type_selection:
            return data_type_selection[data_type_input]
        else:
            print("ERROR: Wrong option selected")

def get_encryption_preference():
    """
    Prompts the user to select whether to encrypt the data.
    Returns:
        encrypt (bool): True if the user wants to encrypt the data, False otherwise.
    """
    while True:
        encrypt_input = input("Do you want to encrypt the data? (Enter Y/N): ")
        if encrypt_input.strip().lower() in ('y', 'n'):
            return encrypt_input.strip().lower() == 'y'
        else:
            print("ERROR: Wrong option selected")

def data_types(dictionary, format):
    """
    Takes a dictionary and converts it to chosen format.
    Arguments:
    dictionary - The raw data in a dictionary to format
    format - The chosen format to convert the dictionary to
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
        print(f"An error in data_types function has occurred: {e}")
        return None

def send_data(format, encrypt=False):
    """
    Connects to server and sends data.
    Arguments:
    format - The chosen format the dictionary was converted to.
    encrypt - Whether or not to encrypt the file, default = false.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            data_sent = data_types(student_names, format)
            if data_sent is None:
                return 1

            if encrypt:
                data_sent = data_sent.decode()
                data_sent = encryption.symmetric_encryption(data_sent)

            client_socket.sendall(data_sent)
            print("\nFollowing data has been sent to the server.\n")
            print(data_sent)
            print("\nStatus: Waiting for server response...")

            data = client_socket.recv(1024)
            print(f"\nServer has received data.\nCopy of data received: {data}")

            return 0
    except ConnectionRefusedError as cre:
        print(f"A connection error has occurred: {cre}. Please check that the server is running.")
        return 1
    except socket.error as se:
        print(f"A socket error has occurred: {se}")
        return 1
    except Exception as e:
        print(f"An error in send_data function has occurred: {e}")
        return 1

if __name__ == '__main__':
    format = get_data_type_selection()
    encrypt = False
    if format == 'txt':
        encrypt = get_encryption_preference()

    err = send_data(format, encrypt)
    if err != 0:
        print('Program halted because of an error')
    else:
        print('Program ran successfully')
