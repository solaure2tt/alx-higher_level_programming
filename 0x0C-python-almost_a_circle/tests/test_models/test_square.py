#!/usr/bin/python3
"""module to test Square module"""
import unittest
import io
import os
import sys
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO


class TestSquare(unittest.TestCase):
    """class to test Square class"""

    def setUp(self):
        """initialization of a rectangle"""
        self.r = Square(3)

    def tearDown(self):
        """delete an instance wich were created"""
        del self.r

    def test_width(self):
        """test the width getter of the instance created"""
        self.assertEqual(self.r.width, 3)

    def test_height(self):
        """test the height getter of the instance created"""
        self.assertEqual(self.r.height, 3)

    def test_x(self):
        """test the x position getter and setter"""
        self.assertEqual(self.r.x, 0)
        self.r.x = 1
        self.assertEqual(self.r.x, 1)

    def test_y(self):
        """test the y getter and setter"""
        self.assertEqual(self.r.y, 0)
        self.r.y = 1
        self.assertEqual(self.r.y, 1)

    def test_squareid(self):
        """test a id of a square instance"""
        r1 = Square(2, 1, 1, 333)
        self.assertEqual(r1.id, 333)

    def set_width(self):
        """update the width"""
        self.r.width = 11
        self.assertEqual(self.r.width, 11)

    def set_height(self):
        """update the width"""
        self.r.height = 8
        self.assertEqual(self.r.height, 8)

    def test_type_different_from_int(self):
        """test paramter of type different to int"""
        with self.assertRaises(TypeError):
            Square("hi")
        with self.assertRaises(TypeError):
            Square(True)
        with self.assertRaises(TypeError):
            Square([1, 2])
        with self.assertRaises(TypeError):
            Square(2.5)
        with self.assertRaises(TypeError):
            Square(4, "hi")
        with self.assertRaises(TypeError):
            Square(4, True)
        with self.assertRaises(TypeError):
            Square(4, [1, 2])
        with self.assertRaises(TypeError):
            Square(4, 1, "3")
        with self.assertRaises(TypeError):
            Square(4, 1, False)
        with self.assertRaises(TypeError):
            Square(4, 1, [1, 2, 3])

    def test_value_inferior_to_0(self):
        """test case negative value"""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -1)
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_area(self):
        """Test the area method"""
        r1 = Square(10, 1, 2)
        self.assertEqual(r1.area(), 100)

    def test_display(self):
        """Test the display method"""
        captureout = StringIO()
        sys.stdout = captureout
        r1 = Square(6)
        r1.display()
        sys.stdout = sys.__stdout__
        output = ("######\n" +
                  "######\n" +
                  "######\n" +
                  "######\n" +
                  "######\n" +
                  "######\n")
        self.assertEqual(captureout.getvalue(), output)

    def test_display_sizetwo(self):
        """Test the display method"""
        captureout = StringIO()
        sys.stdout = captureout
        r1 = Square(2)
        r1.display()
        sys.stdout = sys.__stdout__
        output = ("##\n" +
                  "##\n")
        self.assertEqual(captureout.getvalue(), output)

    def test_str(self):
        """test str overrinding"""
        r1 = Square(4, 1, 1, 222)
        self.assertEqual(r1.__str__(), "[Square] (222) 1/1 - 4")

    def test_display_takinCare_xy(self):
        """Test the display method"""
        captureout = StringIO()
        sys.stdout = captureout
        r1 = Square(2, 2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        output = ("\n\n  ##\n" +
                  "  ##\n")
        self.assertEqual(captureout.getvalue(), output)

    def test_updateId(self):
        """test update method for id"""
        self.r.update(111)
        self.assertEqual(self.r.id, 111)

    def test_updateWidth(self):
        """test update method for width"""
        self.r.update(111, 8)
        self.assertEqual(self.r.size, 8)

    def test_updateHeight(self):
        """test update method for the height"""
        self.r.update(111, 8, 9)
        self.assertEqual(self.r.size, 8)

    def test_updateX(self):
        """test update method for x"""
        self.r.update(11, 8, 2)
        self.assertEqual(self.r.x, 2)

    def test_updateY(self):
        """test update method for y"""
        self.r.update(111, 8, 2, 3)
        self.assertEqual(self.r.id, 111)
        self.assertEqual(self.r.size, 8)
        self.assertEqual(self.r.x, 2)
        self.assertEqual(self.r.y, 3)

    def test_updateKwargsId(self):
        """test update with kwargs id"""
        self.r.update(id=112)
        self.assertEqual(self.r.id, 112)

    def test_updateKwargs(self):
        """test update with kwargs width"""
        self.r.update(id=567, size=12, x=3, y=1)
        self.assertEqual(self.r.size, 12)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 1)
        self.assertEqual(self.r.id, 567)

    def test_updateKArgswargs(self):
        """test update with kwargs with args"""
        self.r.update(67, size=3, x=3, y=1)
        self.assertEqual(self.r.id, 67)

    def test_to_dictionnarytype(self):
        """Test the type return by to_dictionnary"""
        r1 = Square(7, 4)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dictionnary(self):
        """Test the rsult return by to_dictionnary"""
        r1 = Square(7, 1, 1, 98)
        r1_dict = r1.to_dictionary()
        res = {'id': 98, 'x': 1, 'size': 7, 'y': 1}
        self.assertEqual(r1_dict, res)

    def test_save_to_file(self):
        """test save file square.json"""
        try:
            os.remove("Square.json")
        except Exception as e:
            pass
        r1 = Square(7, 1, 2, 381)
        list_objs = [r1]
        Rectangle.save_to_file(list_objs)
        with open("Rectangle.json") as f:
            res = f.read()
        att = [{"x": 1, "y": 2, "id": 381, "size": 7}]
        self.assertEqual(att, json.loads(res))

    def test_from_json_string(self):
        """test the from json string"""
        list_input = [
                {'id': 89, 'size': 10},
                {'id': 7, 'size': 1}
                ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_load_from_file(self):
        """test the load from file"""
        r1 = Square(5, 3, 4)
        list_sq = [r1]
        Square.save_to_file(list_sq)
        list_load = Square.load_from_file()
        self.assertNotEqual(id(r1), id(list_load[0]))

    def test_create(self):
        """test an instance with all attrib"""
        r1 = Square(3, 1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(id(r1), id(r2))


if __name__ == '__main__':
    unittest.main()
