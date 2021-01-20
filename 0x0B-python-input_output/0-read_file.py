#!/usr/bin/python3
"""read a file"""


def read_file(filename=""):
    """function read file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
