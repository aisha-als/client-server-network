from cryptography.fernet import Fernet


def open_file():
    # Open the .txt file
    with open("text_data.txt", "r") as f:
        txt = f.read()
        return txt


def symmetric_encryption(file):
    # Use Fernet to generate an encryption key
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # Encrypt the .txt file using the generated key
    encrypted_txt = fernet.encrypt(file.encode())

    # Print statements to view the unencrypted and encrypted versions
    print("Unencrypted file: ", file)
    print("Encrypted file: ", encrypted_txt)

    # Return the encrypted text
    return encrypted_txt


if __name__ == '__main__':
    txt_file = open_file()
    symmetric_encryption(txt_file)
