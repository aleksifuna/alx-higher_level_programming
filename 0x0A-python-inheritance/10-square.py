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
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """calculates and return the area of a rectangle

        Returns: the area of a rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """ returns a formated representation of an object

        Returns: string representation of the object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Inherites from Rectangle and defines a square geometry"""
    def __init__(self, size):
        """ Initializes the class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ calculates and returns the area of a square
        Returns: area of the square
        """
        return self.__size ** 2
