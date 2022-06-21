#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nbr_printed = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            nbr_printed += 1
    except Exception:
        pass
    finally:
        print()
    return nbr_printed
