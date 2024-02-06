#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file
"""
import sys
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]

if __name__ == '__main__':
    try:
        item_list = load_from_json("add_item.json")
    except FileNotFoundError:
        item_list = []
item_list.extend(sys.argv[1:])
save_to_json(item_list, "add_item.json")
