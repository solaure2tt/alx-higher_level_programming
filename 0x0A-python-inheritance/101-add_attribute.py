#!/usr/bin/python3
"""In this module we adds attributes to objects"""


def add_attribute(obj, att, value):
    """an attribute wiil be add if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
