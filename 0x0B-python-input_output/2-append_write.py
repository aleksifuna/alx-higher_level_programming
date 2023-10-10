#!/usr/bin/python3
""" This module supplies one function ```append_write``` """


def append_write(filename="", text=""):
    """appends a sting at the end of a txt file
    Args:
        filename: path and filename to file we want to write to.
        text: content to write in filename

    Return: number of characters writen.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
