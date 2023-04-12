#!/usr/bin/python3
"""this module implements the Pascal's Triangle"""


def pascal_triangle(n):
    """return the n Pascal's traingle
    Args:
        n (int): number for the triagnle
    """
    res = []
    if n > 0:
        for i in range(n):
            res.append([])
            res[i].append(1)
            for j in range(1, i):
                res[i].append(res[i - 1][j - 1] + res[i - 1][j])
            if i != 0 and n != 0:
                res[i].append(1)
    return res
