#!/usr/bin/python3
""" This module is to  prints a text with 2 new lines after
   those caharacters: ., ?, :
   """


def text_indentation(text):
    """ prints text with two new line
    after some characters(., ?, :)
    Args: text -  atext to print
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    lin = ""
    for letter in range(len(text)):
        lin = lin + text[letter]
        if text[letter] in ".?:":
            print((lin + '\n').lstrip(' '))
            lin = ""
    print(lin.lstrip(' '), end="")
