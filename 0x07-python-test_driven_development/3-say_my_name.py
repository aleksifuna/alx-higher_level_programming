#!/usr/bin/python3
"""
This module supplies a function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """ concatinates two strings representing first name and second name
    then prints My name is <first name> <last name>

    Args:
        first_name: string representing first name
        last_name: string representing last name

    Raise:
        TypeError: if firstname or lastname is not a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
