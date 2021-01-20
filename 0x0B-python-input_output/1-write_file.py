#!/usr/bin/python3
""" write in file"""


def write_file(filename="", text=""):
    """return num of characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        total = f.write(text)

    return(total)
