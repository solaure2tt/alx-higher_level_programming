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
        Args: size -  size of the square
        """

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
