#!/usr/bin/python3
"""Module to compute the json of an object"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object
    Args:
        my_obj (str): object
    Return: json representation
    """
    return json.dumps(my_obj)
