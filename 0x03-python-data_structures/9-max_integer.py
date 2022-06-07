#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = None
    if my_list:
        maxi = my_list[0]
        for item in my_list:
            if item > maxi:
                maxi = item
    return maxi
