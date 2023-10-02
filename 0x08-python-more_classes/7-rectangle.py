#!/usr/bin/python3
"""
This module supplies a class Rectangle
"""


class Rectangle:
    """a class rectangle that with private instance attribute
    with and height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes he class"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """object method that computes and returns the area of a
        rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """object method that computes and returns the are of a rectangle
        if either width or height is 0 it returns 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of class instance"""
        return_str = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                return_str += str(self.print_symbol)
                if j == self.__width - 1 and i < self.__height - 1:
                    return_str += '\n'
        return return_str

    def __repr__(self):
        """Return the canonical string representation of class instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when on object is about to be deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
