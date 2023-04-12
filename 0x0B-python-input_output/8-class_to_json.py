#!/usr/bin/python3
"""
    the dictionary description with simple data structure
    for JSON serialization of an object
"""


def class_to_json(obj):
    """ returns the dictionary description
        with simple data structure (list, dictionary, string,
        integer and boolean) for JSON serialization of an object
        Args:
            obj (json): object
        Return: a dictionnary
    """
    return obj.__dict__
