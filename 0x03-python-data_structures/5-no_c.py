#!/usr/bin/python3
def no_c(my_string):
    res = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            res = res + c
    return res
