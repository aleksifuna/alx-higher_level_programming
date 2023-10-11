#!/usr/bin/python3
""" This module supplies one class Student """


class Student:
    """ Define a student class togethor with the attributes and methods """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the class students
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves and returns a dictionary representation of a student
        """
        dic_rep = self.__dict__
        if type(attrs) is list:
            return {key: dic_rep[key] for key in attrs if key in dic_rep}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all the attributes of of the student instance
        """
        if json:
            self.first_name = json['first_name']
            self.last_name = json['last_name']
            self.age = json['age']
