#!/usr/bin/python3
""" This module supplies one function ``` inherits_from``` """


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class that inherited
    from specified class

    Args:
        obj: represents the child class object
        a_class: represents the parent class object

    Return: True if so else False
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    return False
