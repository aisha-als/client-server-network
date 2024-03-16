import socket
import sys
import encryption
import file_printer

# Define host and port - local host uses local IP of computer
HOST = 'localhost'
PORT = 6666


def receive_data(print_to_file=False, decryption=False):
    # Creates a socket object - AF_INET specifies IPv4 - SOCK_STREAM specifies TCP socket type
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        # Binds server_socket to the host and port defined above
        server_socket.bind((HOST, PORT))

        # Starts listening for incoming connections
        server_socket.listen()

        print(f"Server is listening for connections to {HOST}:{PORT}")

        # Accepts incoming connections
        connection, address = server_socket.accept()

        with connection:
            print(f"Server connected to {address}")

            # Receives data from client side - 1024 represents max number of bytes that can be recieved at once
            while True:
                data = connection.recv(1024)
                
                # If data recieved is empty, then will break loop
                if not data:
                    break

                # Decrypt if decryption is required
                if decryption:
                    data = encryption.symmetric_decryption(data)
                # Decodes data by converting bytes to string then printing
                # (needs adjusting for other file types e.g. JSON, binary etc)
                print(f"Data recieved: {data}")

                # Print to file if required
                if print_to_file:
                    file_printer.writ(data)

                # Sends a copy of the data recieved back to client to confirm its receipt
                if type(data) is str:
                    connection.sendall(data.encode())
                else:
                    connection.sendall(data)


if __name__ == '__main__':
    # Select if the data is to be print to file
    # Options: True, False
    print_to_file = True

    # Select if the data is to be decrypted
    # Options: True, False
    decryption = False

    # Call the main script
    receive_data(print_to_file, decryption)
