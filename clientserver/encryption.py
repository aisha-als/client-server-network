""" Encryption

This script uses the Fernet module from the cryptography Python package.
It is used to generate a symmetric encryption key that can be used to encrypt and decrypt data.
"""

from cryptography.fernet import Fernet

# Use Fernet to generate an encryption key
key = Fernet.generate_key()
# Write the key to a local key.key file
with open("key.key", "wb") as fernet:
    fernet.write(key)


def open_file():
    # Open the .txt file
    with open("text_data.txt", "r") as f:
        txt = f.read()
        return txt


def symmetric_encryption(file):
    """Returns encrypted data after generating a symmetric encryption key using the Fernet module.

    Argument:
    file - file / data to be encrypted.
    """
    # Load the generated key
    key = open("key.key", "rb").read()
    fernet = Fernet(key)
    # Encrypt the .txt file using the generated key
    encrypted_txt = fernet.encrypt(file.encode())

    # Print statements to view the unencrypted and encrypted versions
    print("Unencrypted file: ", file)
    print("Encrypted file: ", encrypted_txt)

    # Return the encrypted text
    return encrypted_txt


def symmetric_decryption(file):
    """Returns the decrypted data after decrypting it using the symmetric key generated in def symmetric_encryption.

    Argument:
    file - file / data to be decrypted.
    """
    # Load the generated key
    key = open("key.key", "rb").read()
    fernet = Fernet(key)

    # try statement to check if the text is encrypted
    try:
        # Decrypt the file using the same key used in encryption
        txt = fernet.decrypt(file).decode()
        # print("Decrypted file: ", txt)
    except:
        # If there are errors decrypting then it means the text in not encrypted. Return the text.
        txt = file
    # Return the txt whether it was decrypted or not encrypted
    return txt


if __name__ == '__main__':
    txt_file = open_file()
    encrypted_txt = symmetric_encryption(txt_file)
    symmetric_decryption(encrypted_txt)
