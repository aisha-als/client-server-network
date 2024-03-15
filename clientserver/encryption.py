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


def symmetric_decryption(file):
    # Use the same key as the encryption
    key = Fernet.generate_key()
    fernet = Fernet(key)
    # Instance the Fernet class with the key
    fernet = Fernet(key)

    # decrypt the encrypted string with the
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methods
    decrypted_txt = fernet.decrypt(file).decode()

    print("decrypted string: ", decrypted_txt)
    return decrypted_txt


if __name__ == '__main__':
    txt_file = open_file()
    symmetric_encryption(txt_file)
