#!/usr/bin/python3
"""Module to write in a text file"""


def write_file(filename="", text=""):
    """write in a file in python and
    prints the number of character written
    Args:
        filename (str): name of the file
        text (str): text to write
    Return: number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return (myFile.write(text))
