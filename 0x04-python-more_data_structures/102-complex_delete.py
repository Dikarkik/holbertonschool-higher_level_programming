#!/usr/bin/python3
# function that deletes keys with a specific value in a dictionary


def complex_delete(a_dictionary, value):
    ref_dic = {k: v for k, v in a_dictionary.items()}
    for key, d_value in ref_dic.items():
        if d_value == value:
            del a_dictionary[key]
    return a_dictionary
