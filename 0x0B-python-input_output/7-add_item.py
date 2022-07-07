#!/usr/bin/python3

"""
Saving object from system args module
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
olds = []
try:
    olds = load_from_json_file("add_item.json")
except Exception:
    pass
args = sys.argv[1:]
save_to_json_file(olds+args, "add_item.json")
