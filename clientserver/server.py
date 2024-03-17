import socket
import encryption
import save_to_file
import os

# Define host and port - local host uses local IP of computer
HOST = 'localhost'
PORT = 6666

def is_encrypted(data):
    return data.startswith(b'gAAAAAB')

def get_user_decision(prompt, valid_responses):
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if user_input in valid_responses:
                return user_input
            else:
                print(f"Invalid input. Please enter {' or '.join(valid_responses)}.")
        except Exception as e:
            print(f"An error occurred while getting user decision: {e}")

def handle_encryption(data):
    decrypt_choice = get_user_decision("Do you want to decrypt the data? (Y/N): ", ['y', 'n'])
    if decrypt_choice == 'y':
        return encryption.symmetric_decryption(data), True
    return data, False

def handle_data_output(data):
    output_choice = get_user_decision("Do you want to print the received data on screen or save it to a file? (Print/Save): ", ['print', 'save'])
    if output_choice == 'print':
        print(f"\nData received: {data}")
    elif output_choice == 'save':
        filename = save_to_file.writ(data)
        print(f"Data has been saved to {filename}. Please check the file.")

def receive_data():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            print("\n*** Initiating Server ***")
            print(f"\nServer is listening for connections to {HOST}:{PORT}\n")
        except socket.error as e:
            print(f"Failed to bind or listen on {HOST}:{PORT}: {e}")
            return

        while True:
            try:
                connection, address = server_socket.accept()
                print(f"\nServer connected to {address}")
            except socket.error as e:
                print(f"A socket error occurred during connection acceptance: {e}")
                continue

            try:
                data = connection.recv(1024)
                if not data:
                    print("No data received. Closing connection.")
                    connection.close()
                    continue
            except socket.error as e:
                print(f"Error receiving data: {e}")
                connection.close()
                continue

            process_connection(data, connection, address)

def process_connection(data, connection, address):
    encrypted = is_encrypted(data)
    print(f"\n*** Data received. {'Data appears to be encrypted.' if encrypted else 'Data does not appear to be encrypted.'} ***")

    if encrypted:
        data, decrypted = handle_encryption(data)
        if decrypted:
            print("\n*** Data has been decrypted. ***\n")
        else:
            print("\n*** Data will remain encrypted. ***\n")

    handle_data_output(data)

    if isinstance(data, str):
        data = data.encode('utf-8')
    connection.sendall(data)

    if get_user_decision("\nDo you want to keep the server running? (Y/N): ", ['y', 'n']) == 'n':
        print("\n*** Server stopped ***\n")
        connection.close()
        exit()
    else:
        print(f"\nServer is listening for connections to {HOST}:{PORT}\n")

if __name__ == '__main__':
    receive_data()
