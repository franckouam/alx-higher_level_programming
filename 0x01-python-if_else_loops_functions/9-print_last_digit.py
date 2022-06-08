#!/usr/bin/python3
def print_last_digit(number):
	if number < 0:
	    number = -1 * number
	if number // 10 == 0:
	    print("{}".format(number), end="")
	    return number
	else:
	    print("{}".format(number % 10), end="")
	    return number % 10
