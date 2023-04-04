#!/usr/bin/python3
"""In this file we will define a rectangle"""


class Rectangle:
    """This class is to defined a rectangle"""

    def __init__(self, width=0, height=0):
        """instanciation of a rectangle
        Args:
            width - the width of the rectangle
            height - the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve a width of the rectangle"""
        if self.__width:
            return self.__width
        else:
            return 0

    @width.setter
    def width(self, value):
        """set the value of the width
        Args: value - value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the value of the height"""
        if self.__height:
            return self.__height
        else:
            return 0

    @height.setter
    def height(self, value):
        """set the value of the height
        Args: value - value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
