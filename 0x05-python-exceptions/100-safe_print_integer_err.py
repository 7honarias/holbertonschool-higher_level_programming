#!/usr/bin/python3
def validation(value):
    x = value
    if value < 0:
        x = value * -1
    if type(value) != int:
        raise TypeError


def safe_print_integer_err(value):
    try:
        validation(value)
        print("{:d}".format(value))
    except TypeError:
        return (False)
    return (True)
