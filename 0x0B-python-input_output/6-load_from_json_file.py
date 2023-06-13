#!/usr/bin/python3
"""This module creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """function that creates an object from a json file"""
    with open(filename, mode="r") as file:
        obj = json.load(file)
    return obj
