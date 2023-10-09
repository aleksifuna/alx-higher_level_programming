#!/usr/bin/python3
""" This module supplies one class MyInt"""


class MyInt(int):
    """ It inherits from class int though has == and != operators inverted """

    def __eq__(self, other):
        """defines the behaviour of equality operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """defines the behaviour of inequality operator"""
        return super().__eq__(other)
