#!/usr/bin/python3
def roman_to_int(roman_string):
    integer = 0
    if roman_string:
        conversions_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000 }
        for c in roman_string:
            integer += conversions_dict.get(c, 0)
    return integer
