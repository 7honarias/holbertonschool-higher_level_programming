#!/usr/bin/python3
""" inserts a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """ filename is file to open,
    search_string is string to search"""
    with open(filename, mode='r', encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, mode='w', encoding="utf-8") as f:
        for t in lines:
            f.write(t)
            if search_string in t:
                f.write(new_string)
