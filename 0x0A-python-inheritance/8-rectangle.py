#!/usr/bin/python3
""" This module supplies one class BaseGeometry"""


class BaseGeometry:
    """Class with 2 public instance method """
    def area(self):
        """Raises an Exeption with custom message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name: a string label
            value: represents value to be validated

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ Initializes the class
        Args:
            width: represents the width of rectangle
            height: represents the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
