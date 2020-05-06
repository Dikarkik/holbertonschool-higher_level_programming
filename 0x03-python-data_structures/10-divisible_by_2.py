#!/usr/bin/python3
# function that finds all multiples of 2 in a list


def divisible_by_2(my_list=[]):
    if my_list == []:
        return None
    result = []
    for element in my_list:
        if element % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
