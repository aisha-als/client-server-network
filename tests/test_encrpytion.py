import pytest
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad  

# --- Encryption/Decryption Functions ---
def encrypt_file(file_name, key):
    with open(file_name, 'rb') as f:
        data = f.read()

    iv = get_random_bytes(16)  # Generate a random initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = iv + cipher.encrypt(pad(data, AES.block_size))

    with open(file_name + ".enc", 'wb') as f:  # Store encrypted data
        f.write(ciphertext)

def decrypt_file(encrypted_file_name, key):
    with open(encrypted_file_name, 'rb') as f:
        data = f.read()

    iv = data[:16]  # Extract IV from the beginning 
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(data[16:]), AES.block_size)

    with open(encrypted_file_name[:-4], 'wb') as f:  # Decrypted output
        f.write(plaintext)

# --- Encryption Tests ---
def test_encrypt_decrypt_text_file():
    file_name = "test_file.txt"
    key = get_random_bytes(16)  

    encrypt_file(file_name, key)
    decrypt_file(file_name + ".enc", key)  

    with open(file_name, "r") as f:
        original_content = f.read()

    with open("decrypted_file.txt", "r") as f:
        decrypted_content = f.read()

    assert original_content == decrypted_content  

def test_decrypt_invalid_key():
    file_name = "test_file.txt"
    original_key = get_random_bytes(16)
    wrong_key = get_random_bytes(16)

    encrypt_file(file_name, original_key) 

    with pytest.raises(ValueError):  # Or the specific error the code raises
        decrypt_file(file_name + ".enc", wrong_key) 
