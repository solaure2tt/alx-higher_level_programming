#!/usr/bin/python3
"""This module is to verify if an object is
an instance of a class"""


def is_same_class(obj, a_class):
    """verify if a object is an instance of a class
    Args: obj - objet
        a_class - class
    """
    return (type(obj) == a_class)
