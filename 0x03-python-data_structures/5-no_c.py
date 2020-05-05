#!/usr/bin/python3
# function that removes all characters c and C from a string


def no_c(my_string):
    new_str = ""
    for c in my_string:
        if ord(c) != ord("c") and ord(c) != ord("C"):
            new_str = new_str + c
    return new_str
