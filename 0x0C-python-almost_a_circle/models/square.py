#!/usr/bin/python3
""" import Rectangle"""
from models.rectangle import Rectangle
"""implementation of class square"""


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init of class super base"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size of square"""
        return (self.width)

    @size.setter
    def size(self, value):
        """def size of square"""
        self.width = value
        self.height = value

    def __str__(self):
        """this return print class"""
        return("[Square] ({}) {}/{} - {}"
               .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """update value"""
        if args:
            my_list = ["self.id", "self.size", "self.x", "self.y"]
            for i in range(len(args)):
                exec(my_list[i] + "= args[i]")
        if kwargs:
            for key in kwargs:
                exec("self." + key + "= kwargs[key]")

    def to_dictionary(self):
        """to dictionary the square"""
        dictionary = {
                    "id": self.id,
                    "size": self.width,
                    "x": self.x,
                    "y": self.y
                    }
        return dictionary
