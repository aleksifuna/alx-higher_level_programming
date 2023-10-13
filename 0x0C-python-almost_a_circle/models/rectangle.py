#!/usr/bin/python3
""" This module supplies a class Rectangle"""
from .base import Base


class Rectangle(Base):
    """ Inherits from Base with some private instance """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes an instance of class Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """
        retrieves the private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Validates and sets the attribute height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        retrieves the private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        validates and sets the attribute height
        """
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def x(self):
        """
        retrieves the private instance attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        validates and sets the attribute height
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
         retrieves the private instance attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        validates and sets the attribute height
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
