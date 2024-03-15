import pytest
import json 
import xmltodict  # pip install xmltodict - need for test
import pickle

from data_formats import dict_to_json, dict_to_xml, dict_to_binary


# --- Sample Test Data ---
simple_dict = {"name": "Edward", "city": "Liverpool"}


# --- JSON Tests ---
def test_dict_to_json_valid():
    json_data = dict_to_json(simple_dict) 
    
    # Check if valid JSON
    try:
        json_object = json.loads(json_data)  # Attempt to parse JSON
        assert isinstance(json_object, dict)  # Should be a dictionary
    except json.JSONDecodeError:
        pytest.fail("Generated output is not valid JSON") 


def test_dict_to_json_content():
    json_data = dict_to_json(simple_dict)

     # Check if expected keys and values exist
    json_object = json.loads(json_data)
    assert json_object['name'] == "Edward"
    assert json_object['city'] == "Liverpool"

# --- XML Tests --- (Similar structure to JSON tests)
def test_dict_to_xml_valid():
    xml_data = dict_to_xml(simple_dict)

    try:
        xmltodict.parse(xml_data)  # Attempt to parse as XML
    except xmltodict.expat.ExpatError:
        pytest.fail("Generated output is not valid XML")

def test_dict_to_xml_content():
    xml_data = dict_to_xml(simple_dict)
    xml_dict = xmltodict.parse(xml_data)

    # Assumming typical XML structure 
    assert xml_dict['root']['name'] == "Edward"
    assert xml_dict['root']['city'] == "Liverpool"

# --- Binary Tests ---
def test_dict_to_binary():
    binary_data = dict_to_binary(simple_dict)

     # Assert that it's a byte string
    assert isinstance(binary_data, bytes)

    # Deserialization Test (this is one way to check if 'correct')
    try:
        recovered_dict = pickle.loads(binary_data)
        assert recovered_dict == simple_dict 
    except pickle.UnpicklingError:
        pytest.fail("Unable to deserialise binary data back to a dictionary")
