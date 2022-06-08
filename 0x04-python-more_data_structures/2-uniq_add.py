#!/usr/bin/python3
def uniq_add(my_list=[]):
    already = []
    summ = 0
    if my_list:
        for i in my_list:
            if i not in already:
                summ += i
                already.append(i)
    return summ
