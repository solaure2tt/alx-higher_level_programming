#!/usr/bin/python3
"""Module to load object form a json file"""
import json


def load_from_json_file(filename):
    """deserilize a json file
    Args:
        filename (str): text file
    Return: object
    """
    with open(filename) as myFile:
        return json.load(myFile)
