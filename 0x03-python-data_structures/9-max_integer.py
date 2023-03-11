#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        max_list = my_list[0]
        for i in range(0, len(my_list)):
            if my_list[i] > max_list:
                max_list = my_list[i]
        return max_list
    else:
        return "None"
