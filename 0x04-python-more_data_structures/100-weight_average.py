#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    s = 0
    n = 0
    for x, y in my_list:
        s = s + (x * y)
        n = n + y
    return (s / n)
