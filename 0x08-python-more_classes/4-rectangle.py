#!/usr/bin/python3
"""class Rectangle

Raises:
    TypeError: width must be an integer
    ValueError: width must be >= 0
    TypeError: height must be an integer
    ValueError: width must be >= 0
    TypeError: rect_1 must be an instance of Rectangle
    TypeError: rect_2 must be an instance of Rectangle
"""


class Rectangle:
    """def rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self._Rectangle__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self._Rectangle__width = value

    @property
    def height(self):
        return(self._Rectangle__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self._Rectangle__height = value

    def area(self):
        re_area = self._Rectangle__width * self._Rectangle__height
        return(re_area)

    def perimeter(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return("")
        re_perim = (self._Rectangle__width + self._Rectangle__height) * 2
        return(re_perim)

    def __str__(self):
        s_rect = ""
        line = "#" * self._Rectangle__width + "\n"
        for i in range(0, self._Rectangle__height):
            s_rect += line
        return (s_rect[:-1])

    def __repr__(self):
        w = str(self._Rectangle__width)
        h = str(self._Rectangle__height)
        return ("Rectangle(" + w + ", " + h + ")")
