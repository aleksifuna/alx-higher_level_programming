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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_obj to a file

        Args:
            list_objs: List of instances that inherit from base
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = "{}.json".format(class_name)
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)
        with open(filename, 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        """
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates and return an instance of base class with all attribute
        already set
        """
        if cls.__name__ == "Rectangle":
            my_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            my_obj = cls(1)
        else:
            return None
        my_obj.update(**dictionary)
        return my_obj
