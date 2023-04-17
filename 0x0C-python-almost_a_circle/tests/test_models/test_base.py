#!/usr/bin/python3
"""module to test base module"""
import unittest
import os
import sys
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """class to test base class"""

    def test_no_and_arg(self):
        """test the initialization base method"""
        """ase = __import__("base").Base"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        """test the to json string method"""
        r1 = Rectangle(10, 7, 2, 8, 166)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = [{"x": 2, "width": 10, "id": 166, "height": 7, "y": 8}]
        self.assertEqual(json.loads(json_dictionary), res)

    def test_to_json_none(self):
        """test the json to string with none value"""
        s1 = Square(1, 0, 0, 39)
        json_dict = s1.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, [])

    def test_to_json_empty(self):
        """test the json to string with empty value"""
        s1 = Square(1, 0, 0, 45)
        json_dict = s1.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, [])

    def test_to_json_notlist(self):
        """test the case of not a list"""
        with self.assertRaises(TypeError):
            json_string = Base.to_json_string("bonjour")


if __name__ == '__main__':
    unittest.main()
