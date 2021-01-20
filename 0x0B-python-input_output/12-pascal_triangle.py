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
            for i in range(i):
                if i == 0:
                    list_r = [1]
                    continue
                if i == n - 1:
                    list_r += [1]
                else:
                    
            list_a = list_r
            list_t += list_r



                
