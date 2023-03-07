#!/usr/bin/python3
for al in range(97, 123):
    char = chr(al)
    if char != 'q' and char != 'e':
        print("{}".format(char), end="")
