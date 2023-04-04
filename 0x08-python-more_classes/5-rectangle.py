#!/usr/bin/python3


"""This module detects instance deletion"""
class Rectangle:
    """class implementation"""
    def __init__(self, width=0, height=0):
        """initialize"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """defines width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns self"""
        return self.__height

    @height.setter
    def height(self, value):
        """defines height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """join"""
        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """returns rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """print"""
        print("Bye rectangle...")
