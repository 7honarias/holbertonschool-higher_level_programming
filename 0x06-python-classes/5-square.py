#!/usr/bin/python3
""" class Square"""


class Square:
    def __init__(self, size=0):
        """ Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it: """

        self.size = size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an interger")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def my_print(self):
        for x in range(0, self._Square__size):
            print("#"*self._Square__size)
        if self._Square__size == 0:
            print()
