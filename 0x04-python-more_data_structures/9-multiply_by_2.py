#!/usr/bin/python3
# function that returns a new dictionary
# with all values multiplied by 2


def multiply_by_2(a_dictionary):
    new_dic = {}
    for elem in sorted(a_dictionary):
        new_dic[elem] = a_dictionary[elem] * 2
    return new_dic
