#!/usr/bin/python3
"""1. Square with size"""


class Square:
    """Class that defines a square by:
        - Private instance attribute: size
        - Instantiation with size (no type/value verification)
    """

    def __init__(self, size):
        """Args:
        self: object instance.
        size: size of the square.
        """
        self.__size = size
