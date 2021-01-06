#!/usr/bin/python3


class Perro:
    def __init__(self, name, age=0):
        self.set_name(name)
        self.dog_age = age

        print("inicializo perrito")

    def say_hi(self):
        print("hello, I am {}".format(self.dog_name))


    def get_name(self):
        return (self.dog_name)

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Error nombre no puede ser number")
        self.dog_name = new_name

try:
    dog = Perro(3, 3)
except Exception as err:
    print(err)
