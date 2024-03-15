import pytest
import os 

# --- File Creation Tests --- 
def test_create_small_text_file():
    file_name = "test_file.txt"
    content = "This is a small text file."
    with open(file_name, "w") as f:
        f.write(content)

    assert os.path.exists(file_name) 
    os.remove(file_name)  

def test_create_large_text_file():
    file_name = "large_test_file.txt"
    with open(file_name, 'w') as f:
        for i in range(10000):  
            f.write("This is a line in a large file\n")

    assert os.path.exists(file_name) 
    os.remove(file_name) 

def test_create_file_invalid_filename():
    file_name = "test@#$%^&*.txt" 
    with pytest.raises(OSError): 
        with open(file_name, "w") as f:
            pass   

# --- File Sending Tests ---
def test_send_text_file():
    file_name = 'test_file.txt'
    # ... Create the file if it doesn't exist 

    def send_file(file_name):  # Placeholder for your actual sending logic
        print(f"Sending file: {file_name}")  

    send_file(file_name) 
    # ... Add assertions to verify success if 'send_file' function gives feedback

# ... Tests for size limits, unsupported types

# --- Encryption Tests (PyCryptodome) ---
from Cryptodome.Cipher import AES 

def test_encrypt_and_send():
    file_name = 'test_file.txt'

    # ... (Encryption using PyCryptodome)
