#!/usr/bin/python3
"""This module prints a square with the character #
"""


def print_square(size):
    """ function that def print_square(size):
        Args: size - size of the square"""
    if type(size) is not int:
        msg = "size must be an integer"
        raise TypeError(msg)
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
