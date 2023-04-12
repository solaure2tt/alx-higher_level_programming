#!/usr/bin/python3
"""Module to write the json of an object in a file"""
import json


def save_to_json_file(my_obj, filename):
    """ write the JSON representation of an object in a file
    Args:
        my_obj (str): object
        filename (str): text file
    Return: json representation
    """
    with open(filename, mode="w") as myFile:
        json.dump(my_obj, myFile)
