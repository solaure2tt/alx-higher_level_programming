#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return 0
    li = set(my_list)
    res = 0
    for x in li:
        res = res + x
    return res
