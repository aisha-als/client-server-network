import pytest
import pickle
import json
import xmltodict  # If we're testing XML serialisation

# --- Dictionary Creation Tests ---

def test_basic_dictionary_creation():
    my_dict = {"name": "Alice", "age": 30}
    assert isinstance(my_dict, dict) 
    assert my_dict["name"] == "Alice"
    assert my_dict["age"] == 30

def test_nested_dictionary_creation():
    my_dict = {"outer": {"inner_key": "value"}}
    assert isinstance(my_dict['outer'], dict)
    assert my_dict['outer']['inner_key'] == "value"

def test_mixed_types_dictionary_creation():
    my_dict = {"str": "hello", "int": 10, "list": [1, 2, 3], "float": 3.14}
    # ... keep assertions to check if each element is of the expected type ?
    assert isinstance(my_dict["str"], str)   # Check for string
    assert isinstance(my_dict["int"], int)   # Check for integer 
    assert isinstance(my_dict["list"], list)  # Check for list
    assert isinstance(my_dict["float"], float)  # Check for float 

def test_empty_dictionary_creation():
    my_dict = {}
    assert len(my_dict) == 0  

def test_serialization_unsupported_type():
    class CustomObject: pass
    my_dict = {"custom": CustomObject()}

    with pytest.raises(TypeError):  # Expect a TypeError for pickling
        pickle.dumps(my_dict)

# --- Serialization Tests ---

def test_binary_serialization():
    my_dict =  {"key1": "value1", "key2": 2}
    data = pickle.dumps(my_dict) 
    assert isinstance(data, bytes)  

    # Add a test step for deserialisation on the server-side:
    # ... (Need the server-side code for this)

def test_json_serialization():
    # ... Similar structure to binary serialization test

def test_xml_serialization():
    # ... Similar structure, using xmltodict
