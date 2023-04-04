#!/usr/bin/python3
"""
        This module is to write a function
        that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Function that divide all elements
            of a matrix by a define number
            Args: matrix - matrix to divide div - number
    """

    res = []
    if type(matrix) == list:
        for ll in matrix:
            if type(ll) is not list:
                msg = "matrix must be a matrix "
                msg = msg + "(list of lists) of integers/floats"
                raise TypeError(msg)
            else:
                for x in ll:
                    if type(x) != int and type(x) != float:
                        msg = "matrix must be a matrix "
                        msg = msg + "(list of lists) of integers/floats"
                        raise TypeError(msg)
        if len(matrix) > 0:
            siz = len(matrix[0])
            for i in range(len(matrix)):
                if len(matrix[i]) != siz:
                    msg = "Each row of the matrix must have the same size"
                    raise TypeError(msg)
        if type(div) != int and type(div) != float:
            msg = "div must be a number"
            raise TypeError(msg)
        if div == 0:
            msg = "division by zero"
            raise ZeroDivisionError(msg)
    else:
        msg = "matrix must be a matrix "
        msg = msg + "(list of lists) of integers/floats"
        raise TypeError(msg)
    return [[round(x / div, 2) for x in row] for row in matrix]
