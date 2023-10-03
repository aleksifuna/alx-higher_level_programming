#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unitest class for max_integer function"""
    def test_max_integer(self):
        """test edge cases for the function max_integer"""
        self.assertEqual(max_integer([5, -1, 3, 4]), 5)
        self.assertEqual(max_integer([-6, -1, -3, -7]), -1)
        self.assertEqual(max_integer([5, 7, 7, 4]), 7)
        self.assertEqual(max_integer([-5, -1, -2, 9]), 9)
