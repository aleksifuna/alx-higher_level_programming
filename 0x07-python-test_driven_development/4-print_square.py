#!/usr/bin/python3
"""
This module has one function print_square
"""


def print_square(size):
    """prints a square of size size with character #

    args:
        size: an integer representing the size of the square

    Raise:
        TypeError: if size is not an integer
        ValueError: if size if < 0
        TypeError: if size is a float and < 0
    """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
            if j == (size - 1):
                print()
