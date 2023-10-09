#!/usr/bin/python3
""" This module supplies one function add_attribute
"""


def add_attribute(obj, key, value):
    """ Adds an attribute key with value value to obj

    Args:
        obj: the object to add the attribute to
        key: the name of the attribute
        value: The value of the attribute

    Raises:
        TypeError: if the attribute cannot be set"""
    if hasattr(obj, "__dict__"):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
