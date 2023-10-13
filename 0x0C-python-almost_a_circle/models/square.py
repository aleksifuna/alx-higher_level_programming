#!/usr/bin/python3
"""This module supplies one class Square """

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a class square that inherits from class Rectangle with additional
    methods and attributes
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes an instance of class Square
        """
        width = size
        height = size
        super().__init__(width, height, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        a = self.id
        b = self.width
        c = self.x
        d = self.y
        return "[Square] ({}) {}/{} - {}".format(a, c, d, b)
