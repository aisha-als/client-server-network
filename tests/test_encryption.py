import pytest
from clientserver.encryption import symmetric_encryption, symmetric_decryption

def test_simple_encryption_decryption():
    #Test data
    original_data = "This is a test message."

    encrypted_data = symmetric_encryption(original_data)
    decrypted_data = symmetric_decryption(encrypted_data)

    assert decrypted_data == original_data
