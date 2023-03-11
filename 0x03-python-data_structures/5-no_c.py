#!/usr/bin/python
def no_c(my_string):
    res = ""
    if len(my_string) > 0:
        for i in range(0, len(my_string)):
            if (my_string[i] != 'c') and (my_string[i] != 'C'):
                res = res + my_string[i]
    return res
