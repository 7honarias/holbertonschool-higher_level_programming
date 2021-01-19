#!/usr/bin/python3
""" class that inherits from list"""


class MyList(list):
    """ function print_sorted"""

    def print_sorted(self):
        print(sorted(self))
