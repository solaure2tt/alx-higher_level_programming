#!/usr/bin/python3
"""In this module we will create an
class square that inherited from a Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """create a class with an initialize it"""

    def __init__(self, size):
        """initialize a square
        Args: size - size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return the area of the rectangle"""
        if self.__size is not None:
            return (self.__size * self.__size)

    def __str__(self):
        """customize how to print a square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
