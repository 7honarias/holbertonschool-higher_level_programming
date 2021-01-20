#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """triangle pascal"""
    list_t = []
    if n <= 0:
        return(list_t)
    else:
        list_r = []
        for i in range(n):
            if i == 0:
                list_t = [1]
                continue
            if i == 1:
                list_a = [1, 1]
                continue
            for i in range(i):
                list_r[i]



                
