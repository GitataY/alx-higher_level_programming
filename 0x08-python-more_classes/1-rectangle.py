#!/usr/bin/python3
"""This class module defines a rectangle"""


class Rectangle:
    """This module defines a rectangle"""
    def __init__(self, width=0, height=0):
        """This is the main method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value > 0:
            raise ValueError('height must be >=0')
