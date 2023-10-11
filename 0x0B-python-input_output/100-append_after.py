#!/usr/bin/python3
""" This module supplies a function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing\
            search string.
    Args:
        filname: path and name to the file
        search_string: to append after this string
        new_string: what to append
    """
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, 'w', encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
