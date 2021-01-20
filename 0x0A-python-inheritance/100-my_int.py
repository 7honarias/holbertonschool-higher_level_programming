#!/usr/bin/python3
"""Modulo int"""


class MyInt(int):
    """class MyInt"""
    def __init__(self, size):
        """instantiation"""
        self._size = size

    def __ne__(self, other):
        """negative"""
        return int.__eq__(self, other)

    def __eq__(self, other):
        return int.__ne__(self, other)
