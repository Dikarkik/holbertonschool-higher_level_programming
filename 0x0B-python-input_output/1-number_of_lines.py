#!/usr/bin/python3
"""1. Number of lines"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file

    Args:
        filename (str, optional): text file. Defaults to "".

    Returns:
        [int]: number of lines
    """
    num_lines = 0

    with open(filename, encoding='utf-8') as file:
        for a_line in file:
            num_lines += 1

    return num_lines
