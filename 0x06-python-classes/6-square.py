#!/usr/bin/python3
""" class Square"""

class Square:
    """ a class square"""

    def __init__(self, size=0, position=(0,0)):
        """define class """

        self.size = size
        self.position = position

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self._Square__size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, int) or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if (not isinstance(i, int)) or i < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        if self._Square__size == 0:
            print()
        for i in range(0, self._position[1]):
            print()
        for i in range(0, self._Square__size):
            print(" "*self._position[0], end="")
            print("#"*self._Square__size)
