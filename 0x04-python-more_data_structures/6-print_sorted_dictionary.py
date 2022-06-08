#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        keys = sorted(a_dictionary)
        keys.sort()
        for key in keys:
            print("{}: {}".format(key, a_dictionary.get(key)))
