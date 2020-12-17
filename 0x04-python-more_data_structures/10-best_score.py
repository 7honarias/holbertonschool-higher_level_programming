#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        li_values = sorted(a_dictionary.values())
        for name, value in a_dictionary.items():
            if value == li_values[-1]:
                return(name)
    return (None)
