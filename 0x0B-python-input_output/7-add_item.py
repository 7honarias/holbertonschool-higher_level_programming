#!/usr/bin/python3
"""Load, add, save"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
read_list = []
if os.path.isfile(filename):
    read_list = load_from_json_file(filename)
save_to_json_file(read_list + sys.argv[1:], filename)
