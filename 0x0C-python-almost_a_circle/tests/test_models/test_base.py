#!/usr/bin/python3
""" This module supplies a unittest for base class attributes and method
"""
import unittest
from models.base import Base


class Testbase(unittest.TestCase):
    """
    Test class for base that inherits from unitest TestCase
    """
    def test_base_id(self):
        """
        Tests assignment of id attribute to class instance
        """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 4)
