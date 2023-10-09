#!/usr/bin/python3
""" This module supplies one function ``` is_kind_of_class``` """


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of or if the object is an instance
    of a class that inherited from the specified class.

    Args:
        obj: represents the child class object
        a_class: represents the parent class object

    Return: True if so else False
    """
    if isinstance(obj, a_class):
        return True
    return False
