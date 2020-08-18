#!/usr/bin/python3
""" 6. Find a peak
function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """ finds a peak """
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[len(list_of_integers) - 1]
