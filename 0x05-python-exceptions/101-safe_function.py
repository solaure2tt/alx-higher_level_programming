#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except (Exception) as e:
        sys.stderr.write('Exception: ' + str(e) + '\n')
        res = None
    return (res)
