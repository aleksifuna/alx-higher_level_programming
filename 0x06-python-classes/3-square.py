#!/usr/bin/python3
"""this file contains our square class """


class Square:
    """A class to represent a square."""
    def __init__(self, size=0):
        """ Initializes a square instance.

        Args:
            size: the size of the square.

        Raises:
            TypeError: if size if not an integer.
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area of a square.

        Returns:
            area of the square
        """
        return self.__size * self.__size
