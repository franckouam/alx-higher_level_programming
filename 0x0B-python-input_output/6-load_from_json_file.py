#!/usr/bin/python3

"""
Loading object from a JSON file module.
"""


import json

def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    res = None
    with open(filename, 'r') as f:
        res = json.load(f)
    return res
