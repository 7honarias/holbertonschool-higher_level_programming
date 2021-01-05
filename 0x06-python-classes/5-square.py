#!/usr/bin/python3
""" class Square"""


class Square:
    """Class define square"""

    def __init__(self, size=0):
        """ Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it: """

        self.size = size

    def my_print(self):
        """ function print with #"""

        if self._Square__size == 0:
            print()
        else:
            for x in range(0, self._Square__size):
                print("{}".format("#" * self._Square__size))

    def area(self):
        """ return the area of square """

        return self._Square__size ** 2

    @property
    def size(self):
        """getter of size"""

        return self._Square__size

    @size.setter
    def size(self, value):
        """ setter of size"""

        if not isinstance(value, int):
            raise TypeError("size must be an interger")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value
