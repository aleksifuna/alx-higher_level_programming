#!/usr/bin/python3
"""
supplies one function find_peak
"""


def find_peak(list_of_integers):
    """
    finds the peak integer in a list
    """
    if len(list_of_integers) == 0:
        return None
    current = list_of_integers[0]
    for num in list_of_integers:
        if num > current:
            current = num
    return current
