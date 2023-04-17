#!/usr/bin/python3
"""This module implements Base class"""


class Base:
    """class implementation"""
    __nb_objects = 0


def __init__(self, id=None):
    """self initialization"""
    if id is not None:
        self.id = id
    else:
        base.__nb_objects += 1
        self.id = base.__nb_objects
