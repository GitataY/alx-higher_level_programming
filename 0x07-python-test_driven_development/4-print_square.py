#!/usr/bin/python3
"""This module prints a square"""


def print_square(size):
    """This function prints a square size"""

    if not isinstance(size, int):
        if isinstance(size, float) and size.is_integer() and size >= 0:
            size = int(size)
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
