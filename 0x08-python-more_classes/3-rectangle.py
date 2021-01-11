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
        re_area = self.__width * self.__height
        return(re_area)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return("")
        re_perim = (self.__width + self.__height) * 2
        return(re_perim)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return""
        else:
            for h in range(self.__height):
                for w in range(self.height - 1):
                    print('#' * self.__width)
                return '#' * self.width
