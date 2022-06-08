#!/usr/bin/python3
def best_score(a_dictionary):
    b_key = None
    b_score = None
    if a_dictionary:
        for key, value in a_dictionary.items():
            if not b_score or b_score < value:
                b_score = value
                b_key = key
    return b_key
