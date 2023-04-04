#!/usr/bin/python3
""" This module is to say the name of someone """


def say_my_name(first_name, last_name=""):
    """ this function will print the name
        Args: first_name - my first name
            last_name - the last name
    """
    if type(first_name) is not str:
        msg = "first_name must be a string"
        raise TypeError(msg)
    if type(last_name) is not str:
        msg = "last_name must be a string"
        raise TypeError(msg)
    print("My name is {:s} {:s}".format(first_name, last_name))
