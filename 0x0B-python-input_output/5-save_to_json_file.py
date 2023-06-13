#!/usr/bin/python3
"""This module saves object to file"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
