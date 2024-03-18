import pytest
from clientserver.encryption import open_file, symmetric_encryption  

# Fixtures 
@pytest.fixture
def sample_file_content():
    return "This is a sample file to be sent from the client to the server."

@pytest.fixture
def text_file_path():
    return "text_data.txt" 

# Tests
def test_open_file(text_file_path, sample_file_content):
    # 1. Creates the "text_data.txt" file with the sample content
    with open(text_file_path, "w") as f:  
        f.write(sample_file_content)

    # 2. Read the file content 
    file_content = open_file()  
    assert file_content == sample_file_content

def test_encryption(sample_file_content):
    encrypted_content = symmetric_encryption(sample_file_content)

    # Assert that the content is encrypted 
    assert encrypted_content != sample_file_content  
