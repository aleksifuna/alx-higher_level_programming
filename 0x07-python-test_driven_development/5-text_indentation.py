#!/usr/bin/python3
"""
This module has one function text_indentation
"""


def text_indentation(text):
    """prints a text with 2 new lines after . ? and :

    Args:
        text: a string representing the test to be printed

    Raises:
        TypeError: if text is not a string
        """
    sep = ".?:"
    flag = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        if c == ' ' and flag == 1:
            flag = 0
        else:
            print(c, end="")
            flag = 0
        if c in sep:
            print("\n")
            flag = 1
