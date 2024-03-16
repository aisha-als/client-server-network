from Crypto.Cipher import AES

def open_file():
    # Open the .txt file
    with open("text_data.txt", "r") as f:
        txt = f.read()
        return txt

def symmetric_encryption(file):
    # Use AES to generate a symmetric key (same key used to encrypt and decrypt)
    obj1 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    # use the to encrypt the message in client side
    encrypted_text = obj1.encrypt(file.encode())

    # Print statements to view the unencrypted and encrypted versions
    print("Unencrypted file: ", file)
    print("Encrypted file: ", encrypted_txt)

    # Return the encrypted text
    return encrypted_txt

def symmetric_decryption(file):
    # Generate the same key as the encryption key 
    # if the same passphrase and the initialization vector(IV) are used
    # this decryption key can used in server side
    obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    # decryption in sever side
    decrypted_text = obj2.decrypt(file).decode()

    print("decrypted string: ", decrypted_txt)
    return decrypted_txt

if __name__ == '__main__':
    txt_file = open_file()
    symmetric_encryption(txt_file)
