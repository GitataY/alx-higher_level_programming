#!/usr/bin/python3
"""This module writes a string to a text file """


def write_file(filename="", text=""):
    """This function writes file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        num_characters = file.write(text)
    return num_characters
