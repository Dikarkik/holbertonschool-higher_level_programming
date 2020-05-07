#!/usr/bin/python3
# function that adds all unique integers in
# a list (only once for each integer)


def uniq_add(my_list=[]):
    uniq = set(my_list)
    total = 0
    for elem in uniq:
        total += elem
    return(total)
