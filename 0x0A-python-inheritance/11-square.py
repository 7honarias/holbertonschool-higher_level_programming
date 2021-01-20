#!/usr/bin/python3
"""modele square 2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """instanciation"""
        self.integer_validator("size", size)
        self._Square__size = size

    def area(self):
        """return area square"""
        return self._Square__size ** 2

    def __str__(self):
        """print in class"""
        return ("[Square] {}/{}"
                .format(self._Square__size, self._Square__size))
