#!/usr/bin/python3
"""creates a class Square that defines a square
    with an instance attribute wich can be optional
    and must be and integer
    """


class Square:
    """Definition of the class"""
    def __str__(self):
        """tells python to print the square like I want"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """initialization of square
        check if size is an integer before initialization
        Args: size - size of square
            position - position of the square
        """
        self.__size = size
        if isinstance(position, tuple) and len(position) == 2:
            if isinstance(position[0], int) and isinstance(position[1], int):
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = position
                else:
                    msg = "position must be a tuple of 2 positive integers"
                    raise TypeError(msg)
            else:
                msg = "position must be a tuple of 2 positive integers"
                raise TypeError(msg)
        else:
            msg = "position must be a tuple of 2 positive integers"
            raise TypeError(msg)

    def area(self):
        """function that returns the current square area"""
        return (self.__size * self.__size)

    def pos_print(self):
        """function that prints in stdout the square
        with the character #"""
        res = ""
        if self.__size:
            if self.__size == 0:
                return "\n"
            else:
                if self.__position[1] > 0:
                    for li in range(self.__position[1]):
                        res = res + "\n"
                for i in range(self.__size):
                    if self.__position[0] > 0:
                        for li in range(self.__position[0]):
                            res = res + " "
                    for j in range(self.__size):
                        res = res + "#"
                    res = res + "\n"
        else:
            res = res + "\n"
        return res

    @property
    def size(self):
        """to retrieve a size"""
        if self.__size:
            return (self.__size)
        else:
            return (0)

    @property
    def position(self):
        """to retrieve a position"""
        if self.__position:
            if isinstance(self.__position, tuple):
                if len(self.__position) == 2:
                    if isinstance(self.__position[0], int):
                        if isinstance(self.__position[1], int):
                            if self.__position[0] >= 0:
                                if self.__position[1] >= 0:
                                    return (self.__position)
                                else:
                                    msg = "position must be a tuple of 2 "
                                    msg = msg + "positive integers"
                                    raise TypeError(msg)
                            else:
                                msg = "position must be a tuple of 2 "
                                msg = msg + "positive integers"
                                raise TypeError(msg)
                        else:
                            msg = "position must be a tuple of "
                            msg = msg + "2 positive integers"
                            raise TypeError(msg)
                    else:
                        msg = "position must be a tuple of 2 positive integers"
                        raise TypeError(msg)
                else:
                    msg = "position must be a tuple of 2 positive integers"
                    raise TypeError(msg)
            else:
                msg = "position must be a tuple of 2 positive integers"
                raise TypeError(msg)
        else:
            msg = "position must be a tuple "
            msg = msg + "of 2 positive integers"
            raise TypeError(msg)

    @position.setter
    def position(self, value):
        """set a position values
        Args: value - value of the position of the square"""
        if isinstance(value, tuple):
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    msg = "position must be a tuple of 2 positive integers"
                    raise TypeError(msg)
            else:
                msg = "position must be a tuple of 2 positive integers"
                raise TypeError(msg)
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

    def my_print(self):
        """print square."""
        print(self.pos_print(), end="")
