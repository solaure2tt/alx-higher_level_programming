#!/usr/bin/python3
"""
    Addition two integer or float
    the result must be an integer
"""
def add_integer(a, b=98):
    """This function is to add two integer"""
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, int):
        if isinstance(b, int):
            return (a + b)
        else:
            raise TypeError("b must be an integer")
    else :
        raise TypeError("a must be an integer")
