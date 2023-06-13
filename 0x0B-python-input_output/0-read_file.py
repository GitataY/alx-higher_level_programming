#!/usr/bin/python3
"""This module reads a text file and prints it out"""


def read_file(filename=""):
    """Function reads a text file and prints it"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
