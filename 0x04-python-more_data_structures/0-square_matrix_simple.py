#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return matrix
    res = []
    for row in matrix:
        rowres = []
        for i in row:
            rowres.append(i**2)
        res.append(rowres)
    return res
