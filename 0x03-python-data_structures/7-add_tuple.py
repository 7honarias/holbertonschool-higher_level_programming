#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_b) == 0:
        a = 0
        b = 0
    elif len(tuple_b) == 1:
        a = tuple_b[0]
        b = 0
    else:
        a = tuple_b[0]
        b = tuple_b[1]

    ret_a = tuple_a[0] + a
    ret_b = tuple_a[1] + b

    new_tuple = (ret_a, ret_b)
    return (new_tuple)
