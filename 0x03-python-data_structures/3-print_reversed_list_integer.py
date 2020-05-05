#!/usr/bin/python3
# function that prints all integers of a list, in reverse order.


def print_reversed_list_integer(my_list=[]):
    if len(my_list) <= 0:
        return
    for element in my_list[::-1]:
        print("{:d}".format(element))
