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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        a = self.id
        b = self.width
        c = self.x
        d = self.y
        return "[Square] ({}) {}/{} - {}".format(a, c, d, b)

    @property
    def size(self):
        """
        Retieves the attribute size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Validated and sets the attribute size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates attributes of class instance
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "size":
                        self.size = value
                    if key == "y":
                        self.y = value
                    if key == "x":
                        self.x = value

    def to_dictionary(self):
        """
        returns dictionary representation of square
        """
        my_dict = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
        return my_dict
