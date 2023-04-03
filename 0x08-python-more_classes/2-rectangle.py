#!/usr/bin/python3
"""In this file we will define a rectangle"""


class Rectangle:
    """This class is to defined a rectangle"""
    def __init__(self, width=0, height=0):
        """instanciation of a rectangle
        Args: width - the width of the rectangle
            height - the height of the rectangle
            """
        self.__width = width
        self.__height = height

    def area(self):
        """to calculate the area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    @property
    def width(self):
        """retrieve the with of the rectangle"""
        return self.width

    @width.setter
    def width(self, value):
        """set the with of the rectangle
        Args: value - value of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve a height"""
        return self.height

    @height.setter
    def height(self, value):
        """set the height of the rectangle
        Args: value - value of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
