#!/usr/bin/python3
"""this file contains our square class """


class Square:
    """A class to represent a square."""
    def __init__(self, size):
        """ Initializes a square instance.

        Args:
            size: the size of the square.

        Returns:
            None.
        """
        self.__size = size
