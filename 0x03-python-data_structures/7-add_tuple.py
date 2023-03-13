#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    i = 0
    for x in tuple_a:
        i = i + 1
        if i > 2:
            break
        if x:
            res.append(x)
        else:
            res.append(0)
    i = 0
    for y in tuple_b:
        i + i + 1
        if i > 2:
            break
        if y:
            res[i] = res[i] + y
        i = i + 1
    return tuple(res)
