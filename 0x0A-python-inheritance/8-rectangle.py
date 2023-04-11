#!/usr/bin/python3
"""In this module we will create an
class rectangle that inherited form BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """create a class with an initialize it"""

    def __init__(self, width, height):
        """ method that initialize a Rectangle
        Args: width - width of the rectangle
            height - height of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
