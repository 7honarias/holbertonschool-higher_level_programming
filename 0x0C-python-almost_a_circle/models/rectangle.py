#!/usr/bin/python3
"""import Base"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return(self.__x)

    @x.setter
    def x(self, value):
        """set of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get of y"""
        return(self.__y)

    @y.setter
    def y(self, value):
        """ set of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return area """
        return(self.__width * self.__height)

    def display(self):
        """ print rectangle with char #"""
        wx = " " * self.__x
        wd = "#" * self.__width
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(wx + wd)

    def __str__(self):
        """print class """
        return("[Rectangle] ({}) {}/{} - {}/{}"
               .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ update of values"""
        my_list = (super()
                   .__init__, "self.width", "self.height", "self.x", "self.y")
        if args:
            my_list[0](args[0])
            for i in range(1, len(args)):
                exec(my_list[i] + "= args[i]")
        if kwargs:
            for i in kwargs:
                exec("self." + i + " = kwargs[i]")

    def to_dictionary(self):
        """return dictionary"""
        dictionary = {
                    "id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y
                    }
        return dictionary
