#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            ch = chr(ord(str[i]) - 32)
        else:
            ch = str[i]
        print("{}".format(ch), end="")
    print()
