#!/usr/bin/python3

import json
""" This module supplies one function ```to_json_string```"""


def to_json_string(my_obj):
    """
    Returns a JSON representation of an object

    Args:
        my_obj: object to return its JSON representation

    Returns: JSON  representation of an object
    """
    return (json.dumps(my_obj))
