#!/usr/bin/python3
"""creates a class Square that defines a square
    with an instance attribute wich can be optional
    and must be and integer
    """

class Square:
    """Definition of the class"""


    def __init__(self, size=0, position=(0, 0)):
        """initialization of square
        check if size is an integer before initialization
        Args: size - size of square
            position - position of the square
        """

        self.__size = size
        self.__position = position

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
                    if self.__position[0] > 0:
                        for l in range(self.__position[0]):
                            print(" ", end="")
                    for j in range(self.__size):
                        print("#", end="")
                    print()

    @property
    def size(self):
        """to retrieve a size"""

        if self.__size:
            return (self.__size)
    @property
    def position(self):
        """to retrieve a position"""

        if self.__position:
            return (self.__position)

    @position.setter
    def position(self, value):
        """set a position values
        Args: value - value of the position of the square"""


        if isinstance(value, tuple):
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    raise TypeError("position must be a tuple of 2 positive integers")
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @size.setter
    def size(self, value):
        """ set a value to attribute size depending on is type and value
        Args: value - value of the posito of the square"""


        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
