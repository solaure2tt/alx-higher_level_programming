#!/usr/bin/python3
"""This module is to verify if an instance
of a class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """return True if obj directly or indirectly
    inherited from a_class
    Args: obj - object
        a_class - class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
