#!/usr/bin/python3
""" 6. Find a peak
function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """ finds a peak """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    peak = list_of_integers[0]
    i = 0
    while i < len(list_of_integers):
        """ peak on extremes """
        if i == 0:
            if list_of_integers[i] > list_of_integers[i + 1]:
                return list_of_integers[i]
        if i == len(list_of_integers) - 1:
            if list_of_integers[i] > list_of_integers[i - 1]:
                return list_of_integers[i]

        """ some peak """
        if list_of_integers[i] > list_of_integers[i - 1]:
            if list_of_integers[i] > list_of_integers[i + 1]:
                return list_of_integers[0]

        i += 1
    return peak
