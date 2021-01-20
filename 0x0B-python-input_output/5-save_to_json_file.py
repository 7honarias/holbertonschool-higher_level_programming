#!/usr/bin/python3
"""Save Object to a file"""
import os
import json

def save_to_json_file(my_obj, filename):
    """json string return nothing"""
    with open(filename, mode="w", encoding="UTF8") as f:
        my_obj = json.dumps(my_obj)
        f.write(my_obj)
