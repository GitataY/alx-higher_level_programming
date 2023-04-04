#!/usr/bin/python3
"""This module implements string representation"""


class Rectangle:
    """This is a class implementaton of a string representation"""
    def __init__(self, width=0, height=0):
        """function defines self"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """self"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """defines height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """defines self"""
        return self.width * self.height

    def perimeter(self):
        """returns perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """returns __str__"""
        if self.width == 0 or self.height == 0:
            return ""
        return (("#" * self.width) + "\n") * self.height

    def __repr__(self):
        """returns rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)