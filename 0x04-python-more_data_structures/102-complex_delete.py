#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    res = []
    f = 0
    for k, v in a_dictionary.items():
        if v == value:
            f = 1
            res.append(k)
    if f == 0:
        return a_dictionary
    [a_dictionary.pop(ke) for ke in res]
    return a_dictionary
