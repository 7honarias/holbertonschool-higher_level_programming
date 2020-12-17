#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)

    x = 0
    for element in a_dictionary:
        if a_dictionary[element] > x:
            x = a_dictionary[element]
            ids = element
    return (ids)
