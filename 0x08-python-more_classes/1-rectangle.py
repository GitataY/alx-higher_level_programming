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
        """sets the width property"""
        return self._width

    @width.setter
    def width(self, value):
        """sets the width attributes"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        """height property"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height attributes"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >=0')
        self._height = value
