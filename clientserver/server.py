import socket
import encryption
import save_to_file

# Define host and port - local host uses local IP of computer
HOST = 'localhost'
PORT = 6666


def receive_data(print_to_file=False):
    """
    Receives data sent from the client.

    Arguments:
    print_to_file - Whether to output data to a file or not. Default = false.
    """
    # Creates a socket object - AF_INET specifies IPv4 - SOCK_STREAM specifies TCP socket type
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            # Binds server_socket to the host and port defined above
            server_socket.bind((HOST, PORT))

            # Starts listening for incoming connections
            server_socket.listen()

            print(f"Server is listening for connections to {HOST}:{PORT}")

            # Accepts incoming connections
            connection, address = server_socket.accept()
        except socket.error as se:
            print(f"A socket error has occured: {se}")
            return 1
        except Exception as e:
            print(f"An error has occured in the receive_data function: {e}")
            return 1

        with connection:
            print(f"Server connected to {address}")

            # Receives data from client side - 1024 represents max number of bytes that can be recieved at once
            while True:
                data = connection.recv(1024)
                
                # If data recieved is empty, then will break loop
                if not data:
                    break

                # Run decryption which will check if the text is encrypted or not and if so, decrypt it
                data = encryption.symmetric_decryption(data)

                #Checks to see if data is an interger (If it is an interger then it means symmetric_decryption function has failed)
                if type(data) is int and data == 1:
                    return data

                # Decodes data by converting bytes to string then printing
                # (needs adjusting for other file types e.g. JSON, binary etc.)
                print(f"Data recieved: {data}")

                # Print to file if required
                if print_to_file:
                    save_to_file.writ(data)

                # Sends a copy of the data recieved back to client to confirm its receipt
                if type(data) is str:
                    connection.sendall(data.encode())
                else:
                    connection.sendall(data)
    return 0

if __name__ == '__main__':
    # Select if the data is to be print to file
    # Options: True, False
    print_to_file = True

    # Call the main script
    err = receive_data(print_to_file)
    if err != 0:
        print('Program halted because of an error')
    else:
        print('Program ran successfully')
