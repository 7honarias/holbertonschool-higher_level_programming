#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    names = list(filter(lambda x: (a_dictionary[x] == value), a_dictionary))
    for n in names:
        del a_dictionary[n]
    return (a_dictionary)
