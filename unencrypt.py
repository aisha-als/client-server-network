from cryptography.fernet import Fernet


def find_key():
    return open('encryption_key', 'r')


def open_file():
    # Open the .txt file
    with open("text_data.txt", "r") as f:
        txt = f.read()
        return txt


def symmetric_decryption(file, encryption_key):
    # Use the same key as the encryption
    decryption_key = encryption_key
    # Instance the Fernet class with the key
    fernet = Fernet(decryption_key)

    # decrypt the encrypted string with the
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methods
    decrypted_txt = fernet.decrypt(file).decode()

    print("decrypted string: ", decrypted_txt)


if __name__ == '__main__':
    txt_file = open_file()
    txt_key = find_key()
    symmetric_decryption(txt_file, txt_key)
