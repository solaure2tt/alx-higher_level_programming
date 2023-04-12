#!/usr/bin/python3
"""Module to read a text file"""


def read_file(filename=""):
    """read a file in python
    Args:
        filename (str); file to read
    """
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            print(line, end="")
