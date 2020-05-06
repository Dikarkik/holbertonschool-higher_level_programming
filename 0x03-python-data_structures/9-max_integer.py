#!/usr/bin/python3
# function that finds the biggest integer of a list


def max_integer(my_list=[]):
    if my_list == []:
        return None
    biggest = my_list[0]
    for element in my_list:
        if biggest < element:
            biggest = element
    return biggest
