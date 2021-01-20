#!/usr/bin/python3
""" to json string"""
import json


def to_json_string(my_obj):
    """function to json string"""
    my_obj = json.dumps(my_obj)

    return my_obj
