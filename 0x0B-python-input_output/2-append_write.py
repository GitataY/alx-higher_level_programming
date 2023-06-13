#!/usr/bin/python3
"""This module appends a file"""


def append_write(filename="", text=""):
    """This function appends a file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        num_characters_added = file.write(text)
    return num_characters_added
