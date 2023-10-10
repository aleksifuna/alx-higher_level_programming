#!/usr/bin/python3
""" This module supplies one function load_from_json_file """


def load_from_json_file(filename):
    """
    creates an object from a JSON file

    Args:
        filename: the path and name to the JSON file

    Returns: the created object
    """
    import json

    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data
