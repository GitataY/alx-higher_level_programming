#!/usr/bin/python3
"""This module  returns the JSON representation of an object"""


import json

def to_json_string(my_obj):
    """ function returns json representation"""
    return json.dumps(my_obj)
