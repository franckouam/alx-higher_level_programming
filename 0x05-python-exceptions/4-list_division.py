#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            div_res = 0
            try:
                div_res = my_list_1[i] / my_list_2[i]
            except TypeError:
                print("wrong type")
            except ZeroDivisionError:
                print("division by 0")
            else:
                pass
            finally:
                result_list.append(div_res)
    except IndexError:
        print("out of range")
    else:
        pass
    return result_list

