#!/usr/bin/python3
"""create object from a json file"""
import os
import json


def load_from_json_file(filename):
    with open(filename, mode="r", encoding="UTF8") as f:
        obj = f.read()
        m_list = json.loads(obj)

    return(m_list)
