#!/usr/bin/python3
""" This module supplies one function ```from_json_string```"""


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string

    Args:
        my_str: the JSON string

    Returns: a python object represented by JSON string
    """
    import json
    return json.loads(my_str)
