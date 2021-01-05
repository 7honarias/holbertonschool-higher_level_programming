#!/usr/bin/python3
""" Class """


class Square:
    """Write a class Square that defines a square by"""


    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        return (self._Square__size * self._Square__size)
