#!/usr/bin/python3
"""creation of a square class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """instanziation of a square
        Args:
            size (int): width of the square
            x (int): position
            y (int): position
            id (int): identifier
        """
        self.__size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieve the size of the rectangle"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of size
        Args:
            value (int): value of size
        """
        if type(value) is int:
            if value >= 0:
                self.__width = value
                self.__height = value
                self.__size = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    def __str__(self):
        """str overloading method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        Args:
            args (list): list of arguments
            kwargs (dict): dictionary key value
        """
        if args and len(args) > 0:
            if type(args[0]) is not int and args[0] is not None:
                raise TypeError("id must be an integer")
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
                if len(args) > 2:
                    self.x = args[2]
                    if len(args) > 3:
                        self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is not None:
                            self.id = value
                    if key == "size":
                        self.size = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        dict = {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
        return dict
