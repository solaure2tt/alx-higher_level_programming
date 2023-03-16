#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list
    res = []
    for x in my_list:
        if x == search:
            res.append(replace)
        else:
            res.append(x)
    return res
