#!/usr/bin/python3
"""create a class student and retrieve the dictionnary"""


class Student:
    """creation of the class"""

    def __init__(self, first_name, last_name, age):
        """instanciation of a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        Args:
            attrs (list): list of strings
        Return: a dictionnary
        """
        if type(attrs) == list:
            check = 0
            for at in attrs:
                if type(at) != str:
                    check = 1
            if check == 0:
                return {att: getattr(self, att)
                        for att in attrs if hasattr(self, att)}
        return self.__dict__
