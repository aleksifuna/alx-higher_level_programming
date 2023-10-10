#!/usr/bin/python3
""" This module supplies one function ```read_file``` """


def read_file(filename=""):
    """ Reads a text file and prints to stdout
    Args:
        filename: the name and path of file to open
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
