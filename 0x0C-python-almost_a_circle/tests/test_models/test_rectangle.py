#!/usr/bin/python3
"""module to test Rectangle module"""
import unittest
import io
import os
import sys
import json
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    """class to test base class"""

    def setUp(self):
        """initialization of a rectangle"""
        self.r = Rectangle(3, 6)

    def tearDown(self):
        """delete an instance wich were created"""
        del self.r

    def test_width(self):
        """test the width getter of the instance created"""
        self.assertEqual(self.r.width, 3)

    def test_height(self):
        """test the height getter of the instance created"""
        self.assertEqual(self.r.height, 6)

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

    def test_rectangleid(self):
        """test a di of a rectangle instance"""
        r1 = Rectangle(2, 2, 1, 1, 300)
        self.assertEqual(r1.id, 300)

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
            Rectangle("hi", 2)
        with self.assertRaises(TypeError):
            Rectangle(True, 2)
        with self.assertRaises(TypeError):
            Rectangle([1, 2], 2)
        with self.assertRaises(TypeError):
            Rectangle(2.5, 2)
        with self.assertRaises(TypeError):
            Rectangle(2, "2")
        with self.assertRaises(TypeError):
            Rectangle(2, False)
        with self.assertRaises(TypeError):
            Rectangle(2, [1, 1, 3])
        with self.assertRaises(TypeError):
            Rectangle(4, 3, "hi")
        with self.assertRaises(TypeError):
            Rectangle(4, 3, True)
        with self.assertRaises(TypeError):
            Rectangle(4, 3, [1, 2])
        with self.assertRaises(TypeError):
            Rectangle(4, 3, 1, "3")
        with self.assertRaises(TypeError):
            Rectangle(4, 3, 1, False)
        with self.assertRaises(TypeError):
            Rectangle(4, 3, 1, [1, 2, 3])

    def test_value_inferior_to_0(self):
        """test case negative value"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 1, -1)

    def test_area(self):
        """Test the area method"""
        self.assertEqual(self.r.area(), 18)
        r1 = Rectangle(10, 5, 1, 2)
        self.assertEqual(r1.area(), 50)

    def test_display(self):
        """Test the display method"""
        captureout = StringIO()
        sys.stdout = captureout
        r1 = Rectangle(6, 3)
        r1.display()
        sys.stdout = sys.__stdout__
        output = ("######\n" +
                  "######\n" +
                  "######\n")
        self.assertEqual(captureout.getvalue(), output)

    def test_display_sizetwo(self):
        """Test the display method"""
        captureout = StringIO()
        sys.stdout = captureout
        r1 = Rectangle(2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        output = ("##\n" +
                  "##\n")
        self.assertEqual(captureout.getvalue(), output)

    def test_str(self):
        """test str overrinding"""
        r1 = Rectangle(4, 4, 1, 1, 222)
        self.assertEqual(r1.__str__(), "[Rectangle] (222) 1/1 - 4/4")

    def test_display_takinCare_xy(self):
        """Test the display method"""
        captureout = StringIO()
        sys.stdout = captureout
        r1 = Rectangle(2, 2, 2, 2)
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
        self.assertEqual(self.r.width, 8)

    def test_updateHeight(self):
        """test update method for the height"""
        self.r.update(111, 8, 9)
        self.assertEqual(self.r.height, 9)

    def test_updateX(self):
        """test update method for x"""
        self.r.update(11, 8, 9, 2)
        self.assertEqual(self.r.x, 2)

    def test_updateY(self):
        """test update method for y"""
        self.r.update(111, 8, 9, 2, 3)
        self.assertEqual(self.r.id, 111)
        self.assertEqual(self.r.width, 8)
        self.assertEqual(self.r.height, 9)
        self.assertEqual(self.r.x, 2)
        self.assertEqual(self.r.y, 3)

    def test_updateKwargsId(self):
        """test update with kwargs id"""
        self.r.update(id=112)
        self.assertEqual(self.r.id, 112)

    def test_updateKwargs(self):
        """test update with kwargs width"""
        self.r.update(id=567, height=3, width=12, x=3, y=1)
        self.assertEqual(self.r.width, 12)
        self.assertEqual(self.r.height, 3)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 1)
        self.assertEqual(self.r.id, 567)

    def test_updateKArgswargs(self):
        """test update with kwargs with args"""
        self.r.update(67, height=3, width=12, x=3, y=1)
        self.assertEqual(self.r.id, 67)

    def test_to_dictionnarytype(self):
        """Test the type return by to_dictionnary"""
        r1 = Rectangle(7, 4)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dictionnary(self):
        """Test the rsult return by to_dictionnary"""
        r1 = Rectangle(7, 4, 1, 1, 97)
        r1_dict = r1.to_dictionary()
        res = {'id': 97, 'x': 1, 'width': 7, 'height': 4, 'y': 1}
        self.assertEqual(r1_dict, res)

    def test_save_to_file(self):
        """test save file rectangle.json"""
        try:
            os.remove("Rectangle.json")
        except Exception as e:
            pass
        r1 = Rectangle(4, 7, 1, 2, 31)
        list_objs = [r1]
        Rectangle.save_to_file(list_objs)
        with open("Rectangle.json") as f:
            res = f.read()
        att = [{"x": 1, "y": 2, "id": 31, "height": 7, "width": 4}]
        self.assertEqual(att, json.loads(res))

    def test_from_json_string(self):
        """test the from json string"""
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_create(self):
        """test an instance with all attrib"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(id(r1), id(r2))

    def test_load_from_file(self):
        """test the load from file"""
        r1 = Rectangle(7, 5, 3, 4)
        list_rec = [r1]
        Rectangle.save_to_file(list_rec)
        list_load = Rectangle.load_from_file()
        self.assertNotEqual(id(r1), id(list_load[0]))


if __name__ == '__main__':
    unittest.main()
