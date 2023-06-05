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

    def area(self):
        """returns the area of rect"""
        return self._width * self._height

    def perimeter(self):
        """returns the perimeter of the rect"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self._height):
            rectangle_str += "#" * self._width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        print("Bye rectangle...")
