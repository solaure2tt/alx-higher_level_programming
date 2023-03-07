#!/usr/bin/python3
def pow(a, b):
    res = a
    if b < 0:
        for i in range(2, ((-1) * b) + 1):
            res = res * a
        res = 1 / res
    elif b == 0:
        res = 1
    else:
        for i in range(2, b + 1):
            res = res * a
    return res
