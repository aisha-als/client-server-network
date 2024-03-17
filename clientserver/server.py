import socket
import encryption
import save_to_file
import os

# Define host and port - local host uses local IP of computer
HOST = 'localhost'
PORT = 6666

def is_encrypted(data):
    # Simple heuristic to check if data might be encrypted
    # This should be replaced with a more robust method depending on the encryption detection logic
    return data.startswith(b'gAAAAAB')

def receive_data():
    # Creates a socket object - AF_INET specifies IPv4 - SOCK_STREAM specifies TCP socket type
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        # Binds server_socket to the host and port defined above
        server_socket.bind((HOST, PORT))

        # Starts listening for incoming connections
        server_socket.listen()
        print("\n*** Initiating Server ***")

        while True:
            print(f"\nServer is listening for connections to {HOST}:{PORT}\n")

        
            # Accepts incoming connections
            connection, address = server_socket.accept()

            with connection:
                print(f"Server connected to {address}")

                # Receives data from client side - 1024 represents max number of bytes that can be recieved at once
                data = connection.recv(1024)
            
                # Notify user of received data and check if it's encrypted
                encrypted = is_encrypted(data)
                print(f"\n*** Data received. {'Data appears to be encrypted.' if encrypted else 'Data does not appear to be encrypted.'} ***\n")

                # If data received is encrypted, ask the user if they want to decrypt it
                if encrypted:
                    while True:
                        decrypt_choice = input("Do you want to decrypt the data? (Y/N): ")
                        if decrypt_choice.strip().lower() == 'y':
                            data = encryption.symmetric_decryption(data)
                            print("\n*** Data has been decrypted. ***\n")
                            break
                        elif decrypt_choice.strip().lower() == 'n':
                            print("\n*** Data will remain encrypted. ***\n")
                            break
                        else:
                            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")

                # Ask the user whether they want to print the received data on screen or save to file
                while True:
                    output_choice = input("Do you want to print the received data on screen or save it to a file? (Print/Save): ")
                    if output_choice.strip().lower() == 'print':
                        print(f"\nData received: {data}")
                        # Delete output.txt if exists
                        if os.path.exists("output.txt"):
                            os.remove("output.txt")
                            break
                        else: break
                    elif output_choice.strip().lower() == 'save':
                        save_to_file.writ(data)
                        print("Data has been saved to output.txt. Please check the file.")
                        break
                    else:
                        print("Invalid input. Please enter 'Print' or 'Save'.")

                # Sends a copy of the data received back to the client to confirm its receipt
                # connection.sendall(b"Data received successfully.")
                connection.sendall(data)

            # After processing a connection, ask if the server should continue running
            while True:
                user_input = input("\n Do you want to keep the server running? (Y/N): ")
                if user_input.strip().lower() == 'y':
                    break  # Continue the outer while loop
                elif user_input.strip().lower() == 'n':
                    print("\n*** Server stopped ***\n")
                    return  # Exit the function, effectively stopping the server
                else:
                    print("Invalid input. Please enter 'Y' for yes or 'N' for no.")

if __name__ == '__main__':
    receive_data()
