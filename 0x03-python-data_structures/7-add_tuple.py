#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    res2 = []
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            res. append(0)
            res.append(0)
        else:
            res.append(tuple_a[0])
            res.append(0)
    else:
        res.append(tuple_a[0])
        res.append(tuple_a[1])
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            res2. append(0)
            res2.append(0)
        else:
            res2.append(tuple_a[0])
            res2.append(0)
    else:
        res2.append(tuple_b[0])
        res2.append(tuple_b[1])
    return (res[0] + res2[0], res[1] + res2[1])
