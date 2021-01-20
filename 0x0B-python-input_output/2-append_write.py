#!/usr/bin/python3
"""file append"""
import os


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="UTF8") as f:
        total = f.write(text)

    return total
