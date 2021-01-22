#!/usr/bin/python3
import json
""" class base"""


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return ([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if len(list_objs) <= 1:
            return ([])
        new_list = []
        for i in list_objs:
            new_list += [i.to_dictionary()]
        my_f = cls.__name__ + ".json"
        with open(my_f, mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """from json to string"""
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        s = cls