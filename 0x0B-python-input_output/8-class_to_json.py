#!/usr/bin/python3
"""This module converts an object to a dictionary"""


def class_to_json(obj):
    """Converts an object to a dictionary"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    else:
        return obj
