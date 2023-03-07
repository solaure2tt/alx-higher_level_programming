#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if str[i] > 'a' and str[i] < 'z':
            if i == len(str) - 1:
                print("{}".format(chr(ord(str[i]) - 32)))
            else:
                print("{}".format(chr(ord(str[i]) - 32)), end="")
        else:
            continue
