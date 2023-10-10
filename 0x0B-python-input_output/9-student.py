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

    def to_json(self):
        """
        Retrieves and returns a dictionary representation of a student
        """
        return self.__dict__
