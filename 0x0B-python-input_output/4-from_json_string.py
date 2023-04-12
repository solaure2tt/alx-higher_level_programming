#!/usr/bin/python3
"""Module to desrialize an object"""
import json


def from_json_string(my_str):
    """ returns the object represented by a JSON string
    Args:
        my_str (str): json string
    Return: object
    """
    return json.loads(my_str)
