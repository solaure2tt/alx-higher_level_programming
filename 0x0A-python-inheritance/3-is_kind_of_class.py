#!/usr/bin/python3
"""This module verify if an object is an
instance of a class or the class that inherited"""


def is_kind_of_class(obj, a_class):
    """function that verify if an object is an
    instance of a class or the class that inherited
    Args: obj - object
        a_class - class
    Return: True or false"""
    return (isinstance(obj, a_class))
