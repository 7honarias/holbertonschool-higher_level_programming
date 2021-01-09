#!/usr/bin/python3
""" here are comment"""


def print_square(size):
    """function that prints a square with the character #

    Args:
        size (int): is the size length of the square

    Raises:
        TypeError: must be an integer, otherwise raise
        ValueError: if size is less than 0, raise
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        [print("#", end="") for x in range(0, size)]
        print()
