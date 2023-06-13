#!/usr/bin/python3
"""This module returns an object represented by a JSON strng"""


import json


def from_json_string(my_str):
    """returns an object from json"""
    return json.loads(my_str)
