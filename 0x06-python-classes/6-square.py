#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Method for initialize a square object
           with validation of the data type of size variable.
        Args:
            size(int): Size of the side of the square.
            position(tuple): Position of the square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Method that calculate the area of a square.
        Args:
           Any Arguments
        Returns:
           The current square area.
        """
        return (self.__size) ** 2

    def my_print(self):
        """Method that prints in stdout the square
           with the character #
        Args:
           Any Arguments
        Returns:
           Always nothing.
        """
        if self.__size == 0:
            print()
        elif self.__position[1] > 0:
            blank_line = '\n' * self.__position[1]
            print(blank_line, end='')
        hash_symbol = '#' * self.__size
        space = ' ' * self.__position[0]
        for i in range(self.__size):
            print("{}{}".format(space, hash_symbol))

    @property
    def size(self):
        """Getter of size
        Args:
           Any Arguments
        Returns:
           The current value of size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size
        Args:
           value(int): Size of the side of the square.
        Return:
           Always nothing
        """
        if isinstance(value, int) is True:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        """Getter of position of the square.
        Args:
           Any Arguments.
        Returns:
           The current value of th position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of position of the square.
        Args:
           value(tuple): Position of the square.
        Return:
           Always nothing
        """
        error = 'position must be a tuple of 2 positive integers'
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(error)
        else:
            for i in value:
                if type(i) is not int or i < 0:
                    raise TypeError(error)
                else:
                    continue
        self.__position = value
