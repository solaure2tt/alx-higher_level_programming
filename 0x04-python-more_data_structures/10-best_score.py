#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    i = 0
    for k, v in a_dictionary.items():
        res = v
        i = i + 1
        if i > 0:
            break
    for ki, val in a_dictionary.items():
        if val > res:
            res = val
    for kk, vv in a_dictionary.items():
        if res == vv:
            return kk
