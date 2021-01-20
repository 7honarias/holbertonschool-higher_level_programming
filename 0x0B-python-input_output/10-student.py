#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function return dict"""
        dir1 = vars(self)
        if attrs != None:
            dir2 = {}
            for i in attrs:
                if i in self.__dict__:
                    dir2[i] = dir1[i]
            return(dir2)
        else:
            return(dir1)
