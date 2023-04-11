#!/usr/bin/python3
"""In this module we will create an
class BaseGeometry"""


class BaseGeometry:
    """create a class with an public method"""

    def area(self):
        """ method that return the area of
        an instance of a baseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that that validates value
        Args: name - a string
            value - value to test
        """
        if name is not None:
            if type(value) is not int:
                msg = name + " must be an integer"
                raise TypeError(msg)
            if value <= 0:
                msg = name + " must be greater than 0"
                raise ValueError(msg)
