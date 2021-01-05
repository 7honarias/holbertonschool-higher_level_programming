#!/usr/bin/python3
""" Class Square"""


class Square:
    """ Write a class Square
    that defines a square by: (baased on 0-square.py)

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module"""

    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
