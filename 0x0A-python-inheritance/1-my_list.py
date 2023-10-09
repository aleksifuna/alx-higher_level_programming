#!/usr/bin/python3
""" This module supplies a class MyList, its attributes and methods"""


class MyList(list):
    """ Inherits from list class. had a custom method"""
    def print_sorted(self):
        """ Prints a list in sorted order"""
        newlist = sorted(self)
        print(newlist)
