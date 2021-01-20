#!/usr/bin/python3
""" class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """instanciation"""
        self.integer_validator("size", size)
        self._Square__size = size

    def area(self):
        """calculate area square"""
        return self._Square__size ** 2
