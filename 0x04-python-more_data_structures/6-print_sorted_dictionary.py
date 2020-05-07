#!/usr/bin/python3
# function that prints a dictionary by ordered keys


def print_sorted_dictionary(a_dictionary):
    # keys = sorted(a_dictiona)
    for elem in sorted(a_dictionary):
        print("{}: ".format(elem), end="")
        print(a_dictionary.get(elem))
