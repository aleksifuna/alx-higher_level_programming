#!/usr/bin/python3
"""This module supplies one function is_same_class"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class.

    Args:
        obj: represents the child class object
    a_class: represents the parent (super class)

    Return: True if so else False
    """
    if type(obj) is a_class:
        return True
    return False
