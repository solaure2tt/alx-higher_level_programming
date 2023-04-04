#!/usr/bin/python3
"""Module to test the max integer 
in a list with unittest
"""
import unittest
"""max_integer = __import__('6-max_integer').max_integer"""

"""Definition and usage of the class unittest"""
class Test_max_integer(unittest.TestCase):
    """This class is to instaciate a unittest module"""
    def test_max_integer(self):
        """This function is to test
        the function max_integer"""
        """self.assertEqual(max_integer.max_integer([]), None)"""
        """self.assertEqual(max_integer.max_integer([1, 4, 2, 6]), 6)
        self.assertEqual(max_integer.max_integer([1, 4, -6]), 4)
        self.assertEqual(max_integer.max_integer([None]), None)
        self.assertEqual(max_integer.max_integer([2]), 2)
        lst = [1, 2, float('inf')]
        self.assertEqual(max_integer(lst), float('inf'))
        lst = [3, -float('inf'), 1]
        self.assertEqual(max_integer(lst), 3)"""

    """def test_type(self):"""
        """
        Tests the cases that doesn't work
        """
        """lst = [1, "hello", 3, 6]
        self.assertRaises(TypeError, max_integer, lst)
        lst = None
        self.assertRaises(TypeError, max_integer, lst)

    suite = unittest.TestLoader().loadTestsFromTestCase(Test_max_integer)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)"""
