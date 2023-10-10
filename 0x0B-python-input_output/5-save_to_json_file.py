#!/usr/bin/python3
""" This module supplies one function save_to_json_file """


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using a JSON representation

    Args:
        my_obj: object to write
        filename: path and filename to write.
    """
    import json

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
