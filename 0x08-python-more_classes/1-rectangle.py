#!/usr/bin/python3
"""
This module supplies a class Rectangle
"""


class Rectangle:
    """a class rectangle that with private instance attribute
    with and height
    """
    def __init__(self, width=0, height=0):
        """initializes he class"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """retrieves the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates and sets the field height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """retrieves the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """validates and sets the field width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
