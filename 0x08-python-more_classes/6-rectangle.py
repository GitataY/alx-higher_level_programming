#!/usr/bin/python3
"""This module defines how many instances"""


class Rectangle:
    """class implementation"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializing"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """print"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """returns self"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns area"""
        return self.width * self.height

    def perimeter(self):
        """defines perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """string implementation"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (("#" * self.width + "\n") * self.height).strip()

    def __repr__(self):
        """return rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)
