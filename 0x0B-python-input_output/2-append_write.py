#!/usr/bin/python3
"""Module to append in a text file"""


def append_write(filename="", text=""):
    """append in a file in python and
    prints the number of character written
    Args:
        filename (str): name of the file
        text (str): text to write
    Return: number of characters appended
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return (myFile.write(text))
