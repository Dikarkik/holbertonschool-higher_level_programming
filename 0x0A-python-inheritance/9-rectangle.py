#!/usr/bin/python3
"""8. Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle"""

    def __init__(self, width, height):
        """Instantiation, using integer_validator() to
        detect exceptions.

        Arguments:
            width [int] -- must be positive integer
            height [int] -- must be positive integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
