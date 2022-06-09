#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        to_delete = []
        for k, v in a_dictionary.items():
            if v == value:
                to_delete.append(k)
        for k in to_delete:
            del a_dictionary[k]
    return a_dictionary
