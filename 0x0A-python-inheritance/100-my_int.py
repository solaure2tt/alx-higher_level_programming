#!/usr/bin/python3
"""This module is to class MyInt that inherits
from int
"""


class MyInt(int):
    """create a class tha inherit from int"""

    def __eq__(self, value):
        """implement the egality for MyInt
        Args: value - first int
        """
        return self.real != value

    def __ne__(self, value):
        """implement the difference operator for MyInt
        Args: value - first int
        """
        return self.real == value
