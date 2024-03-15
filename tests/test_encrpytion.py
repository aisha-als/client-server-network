import pytest
from cryptography.fernet import Fernet
from encryption import symmetric_encryption

# Test Data
original_message = "This is a secret message."

# Test: Encryption and Decryption
def test_encrypt_decrypt():
    key = Fernet.generate_key()  
    fernet = Fernet(key)

    encrypted_message = symmetric_encryption(original_message, key)
    assert encrypted_message != original_message  # Basic check that it's changed

    decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
    assert original_message == decrypted_message

# Test: Invalid Key for Decryption (If applicable)  
def test_decrypt_invalid_key():
    # ... Generate encryption using a valid key

    wrong_key = Fernet.generate_key()

    with pytest.raises(cryptography.fernet.InvalidToken):
        # ... Attempt to decrypt the message with the wrong key

    with pytest.raises(ValueError):  # Or the specific error the code raises
        decrypt_file(file_name + ".enc", wrong_key) 
