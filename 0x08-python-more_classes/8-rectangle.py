#!/usr/bin/python3
"""In this file we will define a rectangle"""


class Rectangle:
    """This class is to defined a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __str__(self) -> str:
        rec = ""
        if self.__width != 0 and self.__height != 0:
            for col in range(self.__height):
                for line in range(self.__width):
                    try:
                        rec += str(self.print_symbol)
                    except Exception:
                        rec += type(self).print_symbol
                if col < self.__height - 1:
                    rec += "\n"
        return rec

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """to calculate the area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __repr__(self):
        """function repr for a rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete a rectangle and print a message to say bye"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
