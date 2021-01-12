#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        li_values = sorted(a_dictionary, key=a_dictionary.get, reverse=True)
        return (li_values[0])
    return (None)
