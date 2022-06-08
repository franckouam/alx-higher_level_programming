#!/usr/bin/python3
def remove_char_at(str, n):
    res = str
    if n >= 0 and n < len(str):
        res = str[:n] + str[n+1:]
    return res
