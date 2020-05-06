#!/usr/bin/python3
# function that finds the biggest integer of a list


def max_integer(my_list=[]):
    biggest = 0
    if my_list:
        for element in my_list:
            if biggest < element:
                biggest = element
    else:
        return None
    return biggest
