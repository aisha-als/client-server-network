""" Data Formats

This script is used to have a sample dictionary object and convert it into different data types.
It provides these data types as output: JSON, XML and binary.
"""

import json
import pickle
from dicttoxml import dicttoxml

# Sample dictionary object.
student_names = {
    "Name1": "Aisha",
    "Name2": "Alou",
    "Name3": "Emilia",
    "Name4": "Edward",
    "Name5": "Devam",
}


def dict_to_json(dictionary):
    """Returns JSON object from a dictionary object."""
    names_json = json.dumps(dictionary)
    print(names_json)
    return names_json


def dict_to_xml(dictionary):
    """Returns XML object from a dictionary object."""
    names_xml = dicttoxml(dictionary)
    print(names_xml)
    return names_xml


def dict_to_binary(dictionary):
    """Returns binary object from a dictionary object."""
    names_binary = pickle.dumps(dictionary)
    print(names_binary)
    return names_binary


if __name__ == '__main__':
    dict_to_json(student_names)
    dict_to_xml(student_names)
    dict_to_binary(student_names)
