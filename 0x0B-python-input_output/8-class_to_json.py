#!/usr/bin/python3
""" This module supplies one function class_to_json """


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure for
    JSON serialization of an object

    Args:
        obj: any object we are to get the description

    Returns: the dictionary description.
    """
    return obj.__dict__
