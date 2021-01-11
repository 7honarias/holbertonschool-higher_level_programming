#!/usr/bin/python3
''' 1-rectangle: python funtion that defines Rectangle type '''


class Rectangle:
    ''' define the rectangle type '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        re_area = self._Rectangle__width * self._Rectangle__height
        return(re_area)

    def perimeter(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return("")
        re_perim = (self._Rectangle__width + self._Rectangle__height) * 2
        return(re_perim)
