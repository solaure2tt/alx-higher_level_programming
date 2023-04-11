#!/usr/bin/python3
"""Defined a class MyInt"""


class MyInt(int):
    """create a class that inherit from int"""

    def __eq__(self, value):
        """implement the egality for MyInt"""
        return self.real != value

    def __ne__(self, value):
        """implement the difference operator for MyInt"""
        return self.real == value
