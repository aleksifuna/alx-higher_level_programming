#!/usr/bin/python3
""" This module supplies one class, base """
import json


class Base:
    """
    this class will be the base of all other classes in the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
