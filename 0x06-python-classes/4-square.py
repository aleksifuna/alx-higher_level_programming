#!/usr/bin/python3
"""this file contains our square class """


class Square:
    """A class to represent a square."""
    def __init__(self, size=0):
        """ Initializes a square instance.

        Args:
            size: the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """ Retrieves attribute size.
        Returns:
            size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """validates the value of size
        Args:
            value: the size of the square.

        Raises:
            TypeError: if size if not an integer.
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates the area of a square.

        Returns:
            area of the square
        """
        return self.__size * self.__size
