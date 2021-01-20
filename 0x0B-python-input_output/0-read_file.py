#!/usr/bin/python3
"""read a file"""
import os


def read_file(filename=""):
    """function read file"""
    with open(filename, encoding="UTF8") as f:
        print(f.read())
