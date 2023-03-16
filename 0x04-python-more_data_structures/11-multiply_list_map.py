#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if len(my_list) == 0:
        return my_list
    return (list(map(lambda x: x * number, my_list)))
