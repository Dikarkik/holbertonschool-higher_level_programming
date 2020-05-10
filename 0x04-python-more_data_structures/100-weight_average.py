#!/usr/bin/python3
# function that returns the weighted average of
# all integers tuple (<score>, <weight>)


def weight_average(my_list=[]):
    total = 0
    div = 0
    if my_list:
        for elem in my_list:
            total += elem[0] * elem[1]
            div += elem[1]
        return total / div
    else:
        return 0
