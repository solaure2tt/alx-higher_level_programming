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


        return (self.__size * self.__size)

    def my_print(self):
        """function that prints in stdout the square 
        with the character #"""


        if self.__size:
            if self.__size == 0:
                print()
            else:
                for i in range(self.__size):
                    for j in range(self.__size):
                        print("#", end="")
                    print()

    @property
    def size(self):
        """to retrieve a property"""

        if self.__size:
            return (self.__size)

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
