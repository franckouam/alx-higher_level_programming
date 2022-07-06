#!/usr/bin/python3
"""
Writting JSON module
"""
import json


def to_json_string(my_obj):
    """Returns a string representation of an object"""
    return json.dumps(my_obj)
