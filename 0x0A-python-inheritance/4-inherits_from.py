#!/usr/bin/python3
""" function that returns True if the object is an insta e of class"""


def inherits_from(obj, a_class):
    """compare function"""

    if type(obj) != a_class and isinstance(obj, a_class):
        return(True)
    else:
        return(False)
