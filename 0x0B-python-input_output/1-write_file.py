#!/usr/bin/python3
""" This module supplies one function ```write_file``` """


def write_file(filename="", text=""):
    """writes text into filename
    Args:
        filename: path and filename to file we want to write to.
        text: content to write in filename

    Return: number of characters writen.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
