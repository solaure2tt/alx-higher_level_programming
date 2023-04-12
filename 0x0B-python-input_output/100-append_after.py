#!/usr/bin/python3
"""Module that insert a text in a file"""


def append_after(filename="", search_string="", new_string=""):
    """function that will insert new_string in filename after
    every search_string
    Args:
        filename (str): name of the file
        search_string (str): string to search
        new_string (str): string to insert
    """
    with open(filename, encoding="utf-8") as myFile:
        i = 0
        text = ""
        for line in myFile:
            text += line
            if search_string in line:
                i = 1
                text += new_string
    if i == 1:
        with open(filename, mode="w", encoding="utf-8") as myFile:
            myFile.write(text)
