#!/usr/bin/python3
"""3. Area of a square"""


class Square:
    """class Square that defines a square by:
        - Private instance attribute: size
        - Instantiation with optional size = 0
    """

    def __init__(self, size=0):
        """Args:
        self: object instance.
        size: size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area
        """
        return self.__size * self.__size
