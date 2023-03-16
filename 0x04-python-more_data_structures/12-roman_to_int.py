#!/usr/bin/python3
def roman_to_int(roman_string):
    ro = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    res = 0
    x = len(roman_string)
    for (i, r) in enumerate(roman_string):
        if i < x - 1 and ro[r] < ro[roman_string[i + 1]]:
            res -= ro[r]
        else:
            res += ro[r]
    return res
