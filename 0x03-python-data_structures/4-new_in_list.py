#!/usr/bin/pyhton3
def new_in_list(my_list, idx, element):
    if (idx >= 0) and (idx < len(my_list)):
        my_list_copy = my_list.copy()
        my_list_copy[idx] = element
        return my_list_copy
    else:
        return my_list
