#!/usr/bin/python3
"""creates a class Square that defines a square
    with an instance attribute wich can be optional
    and must be and integer
    """


class Square:
    """Definition of the class"""
    def __init__(self, size=0):
        """initialization of square
        check if size is an integer before initialization
        Args: size - size of the square
        """
        self.__size = size

    def area(self):
        """function that returns the current square area"""
        if self.__size:
            return ((self.__size) * (self.__size))

    @property
    def size(self):
        """to retrieve a property"""
        if self.__size:
            return (self.__size)
        else:
            return (0)

    @size.setter
    def size(self, value):
        """ set a value to attribute size depnding on is type and value
        Args: value - value of the size of the square"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def __le__(self, sec):
        """iferior or equal operand comparison"""
        return self.area() <= sec.area()

    def __lt__(self, sec):
        """inferior opeand comparison"""
        return self.area() < sec.area()

    def __ge__(self, sec):
        """superior or equal operand comparison"""
        return self.area() >= sec.area()

    def __ne__(self, sec):
        """difference operand comparaison"""
        return self.area() != sec.area()

    def __gt__(self, sec):
        """superior operand comparison"""
        return self.area() > sec.area()

    def __eq__(self, sec):
        """equal operand comparison"""
        return self.area() == sec.area()
