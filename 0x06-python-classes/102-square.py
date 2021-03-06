#!/usr/bin/python3
""" class square """


class Square:
    """ a class """

    def __init__(self,  size=0):
        """ constructor
        Argumemts:
        size{int} -- the size of square """

        self.size = size

    def area(self):
        """ return the area of square """

        return self._Square__size * self._Square__size

    @property
    def size(self):
        """ return the square size """

        return self._Square__size

    @size.setter
    def size(self, value):
        """ updates the square size """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
