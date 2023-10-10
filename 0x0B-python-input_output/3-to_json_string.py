#!/usr/bin/python3
import json
""" This module supplies one function ```to_json_string```"""


def to_json_string(my_obj):
    """returns a JSON representation of an object

    Args:
        my_obj: object to return its JSON representation

    Return: JSON  representation of an object
    """
    return (json.dumps(my_obj))
