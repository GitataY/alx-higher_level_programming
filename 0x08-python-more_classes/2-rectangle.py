#!/usr/bin/python3
"""This module includes area and perimeter"""


class Rectangle:
    """class implentation of area and perimeter"""
    def __init__(self, width=0, height=0):
        """Defines __init__"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defines the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property"""
        return self.__height

    @height.setter
    def height(self, value):
        """defines height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """self"""
        return self.__width * self.__height

    def perimeter(self):
        """defines the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
