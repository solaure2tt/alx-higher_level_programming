#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if len(my_list) > 0:
        for i in range(0, len(my_list)):
            print("{}".format(my_list[i]))
