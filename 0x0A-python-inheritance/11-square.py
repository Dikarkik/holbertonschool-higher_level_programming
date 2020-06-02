#!/usr/bin/python3
"""11. Square #2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        """Instantiation, using integer_validator() to
        detect exceptions.

        Arguments:
            size [int] -- must be positive integer
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the rectangle"""
        return self.__size * self.__size

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
