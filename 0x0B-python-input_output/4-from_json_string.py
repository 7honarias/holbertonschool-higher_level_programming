#!/usr/bin/python3
"""From json string to object"""
import json


def from_json_string(my_str):
    """return an obj"""
    my_str = json.loads(my_str)

    return(my_str)