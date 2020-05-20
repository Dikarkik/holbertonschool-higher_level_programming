#!/usr/bin/python3
"""4. Access and update private attribute"""


class Square:
    """class Square that defines a square by:
        - Private instance attribute: size
        - Instantiation with optional size = 0
    """

    def __init__(self, size=0, position=(0, 0)):
        """Args:
        self: object instance.
        size: size of the square.
        position: must be a tuple of 2 positive integers.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        self.check_position(position)
        self.__position = position

    @property
    def size(self):
        """Returns: [int] -- size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of 'size' attribute

            Arguments:
                value {int} -- new size of the square

            Raises:
                TypeError: When value does not a int
                ValueError: When value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns: [tuple] -- position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for __position"""
        self.check_position(value)
        self.__position = value

    def area(self):
        """Returns the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
        else:
            print()

    def check_position(self, value):
        """Check if value is a tuple of 2 positive integers"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
