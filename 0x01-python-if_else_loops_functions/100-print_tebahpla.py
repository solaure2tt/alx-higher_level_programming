#!/usr/bin/python3
x = 122
while x >= 97:
    if x % 2 == 0:
        ch = chr(x)
    else:
        ch = chr(x - 32)
    print("{}".format(ch), end="")
    x = x - 1
