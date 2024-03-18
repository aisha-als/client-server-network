import pytest
from cryptography.fernet import InvalidToken
from clientserver.encryption import symmetric_encryption, symmetric_decryption

# Test Data
original_message = "This is a secret message."

def test_encrypt_decrypt():
    """Tests the core encryption and decryption functionality."""
    key = Fernet.generate_key()
    encrypted_message = symmetric_encryption(original_message, key)
    decrypted_message = symmetric_decryption(encrypted_message, key)

    assert original_message == decrypted_message 

def test_encryption_changes_data():
    """Tests that encryption produces a different output."""
    key = Fernet.generate_key()
    encrypted_message = symmetric_encryption(original_message, key)

    assert encrypted_message != original_message

def test_decrypt_invalid_key():
    """Tests that using an incorrect key raises an error."""
    key = Fernet.generate_key()
    encrypted_message = symmetric_encryption(original_message, key)
    wrong_key = Fernet.generate_key()

    with pytest.raises(InvalidToken):
        symmetric_decryption(encrypted_message, wrong_key)
