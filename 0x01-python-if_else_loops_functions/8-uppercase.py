#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            char_to_print = chr(ord(c)-32)
        else:
            char_to_print = c
        print("{}".format(char_to_print), end='')
    print("{}".format(''))
