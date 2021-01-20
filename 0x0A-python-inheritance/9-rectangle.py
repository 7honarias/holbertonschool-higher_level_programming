#!/usr/bin/python3
""" class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""
    def __init__(self, width, height):
        """inistanciation of atributes"""
        self.integer_validator("width", width)
        self._Rectangle__width = width
        self.integer_validator("height", height)
        self._Rectangle__height = height

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """return string"""
        return ("[Rectangle] {}/{}".format(self._Rectangle__width, self._Rectangle__height))
