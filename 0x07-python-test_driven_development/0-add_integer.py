#!/usr/bin/python3
"""This module addds two integers"""


def add_integer(a, b=98):
    """This function implements integer addition"""
    if (type(a) not in [int, float]) or (type(b) not in [int, float]):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
