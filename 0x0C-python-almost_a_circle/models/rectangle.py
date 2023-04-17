#!/usr/bin/python3
"""creation of a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle inherite from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instanziation of a rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of teh rectangle
            x (int): position
            y (int): position
            id (int): identifier
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width
        Args:
            value (int): value of width
        """
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height
        Args:
            value (int): value of the height
        """
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """retrieve the x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x
        Args:
            value (int): value of x
        """
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be > 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """retrieve the y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y
        Args:
            value (int): value of y
        """
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be > 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """returns the area value of the instance"""
        if self.__width is not None and self.__height is not None:
            return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance
        with the character #"""
        if self.__width is not None and self.__height is not None:
            for h in range(self.__y):
                print()
            for i in range(self.__height):
                for w in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        Args:
            args (list): list of arguments
            kwargs (dict): dictionary key value
        """
        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
                if len(args) > 2:
                    self.__height = args[2]
                    if len(args) > 3:
                        self.__x = args[3]
                        if len(args) > 4:
                            self.__y = args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is not None:
                            self.id = value
                    if key == "width":
                        self.__width = value
                    if key == "height":
                        self.__height = value
                    if key == "x":
                        self.__x = value
                    if key == "y":
                        self.__y = value

    def to_dictionary(self):
        """returns the dictionary representation of a rectangle"""
        dict = {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
        return dict
