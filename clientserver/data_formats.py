import json
import pickle
from dicttoxml import dicttoxml

student_names = {
    "Name1": "Aisha",
    "Name2": "Alou",
    "Name3": "Emilia",
    "Name4": "Edward",
    "Name5": "Devam",
}


def dict_to_json(dictionary):
    names_json = json.dumps(dictionary)
    print(names_json)
    return names_json


def dict_to_xml(dictionary):
    names_xml = dicttoxml(dictionary)
    print(names_xml)
    return names_xml


def dict_to_binary(dictionary):
    names_binary = pickle.dumps(dictionary)
    print(names_binary)
    return names_binary


if __name__ == '__main__':
    dict_to_json(student_names)
    dict_to_xml(student_names)
    dict_to_binary(student_names)
