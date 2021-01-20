#!/usr/bin/python3
""" class Rectangle"""


class BaseGeometry():
    """ declarations"""

    def area(self):
        """calculate area"""
        return(self._Rectangle__width * self._Rectangle__height)

    def integer_validator(self, name, value):
        """validate integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self._Rectangle__width = width
        self.integer_validator("height", height)
        self._Rectangle__height = height

        self.area()

    def __str__(self):
        """return string"""
        return ("[Rectangle] {}/{}".format(self._Rectangle__width, self._Rectangle__height))
