#!/usr/bin/python3
""" write in file"""
import os


def write_file(filename="", text=""):
    """return num of characters written"""
    with open(filename, mode="w", encoding="UTF8") as f:
        total = f.write(text)

    return(total)
