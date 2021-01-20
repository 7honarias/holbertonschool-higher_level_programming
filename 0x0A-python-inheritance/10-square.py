#!/usr/bin/python3
""" class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self._Square__size = size

    def area(self):
        return self._Square__size ** 2        
