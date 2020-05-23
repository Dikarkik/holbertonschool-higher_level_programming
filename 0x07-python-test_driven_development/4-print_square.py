#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """
    Prints a square with the character #
    Parameters:
        size: must be an integer (is the size length of the square)
    Raises:
        TypeError: If size is not integer
        ValueError: If size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
