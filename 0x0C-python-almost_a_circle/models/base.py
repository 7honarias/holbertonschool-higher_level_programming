#!/usr/bin/python3
"""imprt json turtle"""
import json
import turtle
import csv
""" class base"""


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init of class base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return ([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save file json"""
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dictionaries.append(dictionary)
            json_string = Base.to_json_string(list_dictionaries)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """from json to string"""
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """create a new instance"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = cls(1, 1)
        elif cls is Square:
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load form file Rectangle.json Square.json"""
        import os
        my_list = list()
        my_file = cls.__name__ + ".json"
        if os.path.isfile(my_file):
            with open(my_file, mode="r", encoding='utf-8') as f:
                text = f.read()
                list_output = cls.from_json_string(text)
                for diction in list_output:
                    dum = cls.create(**diction)
                    my_list.append(dum)
                return (my_list)
        return(my_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save file in csv"""
        filename = cls.__name__ + ".csv"
        list_dictionary = list(map(cls.to_dictionary, list_objs))
        keys = list()
        for key in list_dictionary[0]:
            keys.append(key)

        with open(filename, mode="w") as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(list_dictionary)

    @classmethod
    def load_from_file_csv(cls):
        """ load_from_file_csv """
        filename = '{}.csv'.format(cls.__name__)
        try:
            with open(filename, mode='r', newline='') as file:
                dic_list = csv.DictReader(file)
                my_list = []
                for dicts in dic_list:
                    dictionary = {}
                    for key in dicts:
                        dictionary[key] = int(dicts[key])
                    my_list.append(dictionary)
                return [cls.create(**dicts) for dicts in my_list]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangle, list_squares):
        """draw in turtle our squares or rectangle"""
        turtle.getscreen()
        for obj in list_rectangle:
            turtle.pu()
            turtle.setpos(obj.x, obj.y)
            for i in range(2):
                turtle.pd()
                turtle.fd(obj.width)
                turtle.right(90)
                turtle.fd(obj.height)
                turtle.right(90)
            turtle.pu()

        for obj in list_squares:
            turtle.pu()
            turtle.setpos(obj.x, obj.y)
            for i in range(2):
                turtle.pd()
                turtle.fd(obj.width)
                turtle.right(90)
                turtle.fd(obj.height)
                turtle.right(90)
            turtle.pu()
