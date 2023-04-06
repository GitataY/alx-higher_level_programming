#!/usr/bin/python3
"""This module prints a name"""

    
def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): First name string.
        last_name (str): Last name string (optional). Defaults to an empty string.

    Returns:
        None
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
