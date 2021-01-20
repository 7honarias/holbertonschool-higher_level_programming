#!/usr/bin/python3
"""file append"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as f:
        total = f.write(text)

    return total
