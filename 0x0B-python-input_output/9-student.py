#!/usr/bin/python3
"""create a class student and retrieve the dictionnary"""


class Student:
    """creation of the class"""

    def __init__(self, first_name, last_name, age):
        """instanciation of a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
