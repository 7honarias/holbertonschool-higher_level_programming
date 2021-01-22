#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        if args:
            my_list = ["self.id", "self.size", "self.x", "self.y"]
            for i in range(len(args)):
                exec(my_list[i] + "= args[i]")
        if kwargs:
            for key in kwargs:
                exec("self." + key + "= kwargs[key]")

    def to_dictionary(self):
        dictionary = {
                    "id": self.id,
                    "size": self.width,
                    "x": self.x,
                    "y": self.y
                    }
        return dictionary
