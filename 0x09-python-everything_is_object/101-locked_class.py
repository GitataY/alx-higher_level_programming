#!/usr/bin/python3
"""This class module is a locked class"""


class LockedClass:
    """This class is a locked class"""

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        """function documentation"""
        self.first_name = first_name
