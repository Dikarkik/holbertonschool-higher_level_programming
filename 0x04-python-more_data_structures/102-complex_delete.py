#!/usr/bin/python3
# function that deletes keys with a specific value in a dictionary


def complex_delete(a_dictionary, value):
    list_keys = []
    for key, d_value in a_dictionary.items():
        if d_value == value:
            list_keys.append(key)
    for elem in list_keys:
        del a_dictionary[elem]
    return a_dictionary
