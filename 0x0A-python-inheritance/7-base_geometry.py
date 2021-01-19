#!/usr/bin/python3
""" class BaseGeometry"""


class BaseGeometry:
    """ declarations"""

    def area(self):
        """ calculate area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validator int"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
