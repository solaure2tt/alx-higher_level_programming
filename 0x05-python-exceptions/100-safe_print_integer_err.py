#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        sys.stderr.write('Exception: ' + str(e) + '\n')
        return (False)
    else:
        return (True)
