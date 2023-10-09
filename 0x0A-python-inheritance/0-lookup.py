#!/usr/bin/python3
""" This module supplies one function ```lookup```"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: represents the object

    Return:
        a list of available attributes and methods of the object

    """
    return (dir(obj))
