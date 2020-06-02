#!/usr/bin/python3
"""7. Integer validator"""


class BaseGeometry:
    """class based on 6-base_geometry.py"""

    def area(self):
        """Public instance method: that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates 'value'

            Arguments:
                name [string] -- you can assume name is always a string
                value [int] -- must be an integer

            Raises:
                TypeError: if 'value' is not integer
                ValueError: if 'value' is less or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value+1 == value:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
