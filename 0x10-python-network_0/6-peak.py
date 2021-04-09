#!/usr/bin/python3
"""module find peak"""


def find_peak(list_of_integers):
    """
    finds a peak
    """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
