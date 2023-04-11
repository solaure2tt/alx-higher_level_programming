#!/usr/bin/python3
""" In this module we willcreate the class MyList """


class MyList(list):
    """This class inherits from list """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
