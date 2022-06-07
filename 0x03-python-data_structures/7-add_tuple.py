#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b = 0, 0
    for tupl in (tuple_a, tuple_b):
        if len(tupl) > 0:
            a += tupl[0]
        if len(tupl) > 1:
            b += tupl[1]
    return a, b
