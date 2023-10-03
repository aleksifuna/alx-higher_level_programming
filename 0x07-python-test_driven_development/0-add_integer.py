#!/usr/bin/python3
"""
This module supplies one function, add_integer
"""


def add_integer(a, b=98):
    """Computes and returns the sum of two integers.


    Args:
        a: A numbers representing the first integer
        b: A number representing the second integer

    Returns:
        integer: A number representing the sum of 'a' and 'b'.

    Raises:
        TypeError: An error occurs when either 'a' or 'b' is not int or float

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
