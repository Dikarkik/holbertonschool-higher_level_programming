#!/usr/bin/python3
""" Module: Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Defines a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor

        Args:
            width (int): width
            height (int): height
            x (int, optional): x position. Defaults to 0.
            y (int, optional): y position. Defaults to 0.
            id (int, optional): id.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ retrieves the width value """
        return self.__width

    @width.setter
    def width(self, width):
        """set the width value

        Args:
            width (int): must be a positive integer > 0
        """
        self.is_int_validator("width", width)
        self.is_under_or_equals_0_validator("width", width)
        self.__width = width

    @property
    def height(self):
        """ retrieves the height value """
        return self.__height

    @height.setter
    def height(self, height):
        """set the height value

        Args:
            height (int): must be a positive integer > 0
        """
        self.is_int_validator("height", height)
        self.is_under_or_equals_0_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """ retrieves the x value """
        return self.__x

    @x.setter
    def x(self, x):
        """set the x vlaue

        Args:
            x (int): must be a positive integer
        """
        self.is_int_validator("x", x)
        self.is_under_0_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """ retrieves the y value """
        return self.__y

    @y.setter
    def y(self, y):
        """set the y value

        Args:
            y (int): must be a positive integer
        """
        self.is_int_validator("y", y)
        self.is_under_0_validator("y", y)
        self.__y = y

    @staticmethod
    def is_int_validator(name_var, value):
        """raise error if value is not an integer

        Args:
            name_var (str): name in the error message
            value (int): must be integer

        Raises:
            TypeError: if value is not integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name_var))

    @staticmethod
    def is_under_or_equals_0_validator(name_var, value):
        """raise error if value is not > 0

        Args:
            name_var (str): name in the error message
            value (int): must be > 0

        Raises:
            ValueError: if value is not > 0
        """
        if value <= 0:
            raise ValueError("{} must be > 0".format(name_var))

    @staticmethod
    def is_under_0_validator(name_var, value):
        """raise error if value is not >= 0

        Args:
            name_var (str): name in the error message
            value (int): must be >= 0

        Raises:
            ValueError: if value is not >= 0
        """
        if value < 0:
            raise ValueError("{} must be >= 0".format(name_var))

    def area(self):
        """returns the area value of the Rectangle instance

        Returns:
            int: area of the Rectangle
        """
        return self.width * self.height

    def display(self):
        """print in stdout the Rectangle instance
        with the character # by taking care of x and y
        """
        print("\n" * self.y, end="")
        for y in range(0, self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """define format

        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """using *args: assign an argument to each attribute
        Order must be id, width, height, x, y

        using **kwargs: assigns a key/value argument to attributes
        **kwargs can be thought of as a
        doublepointer to a dictionary: key/value
        **kwargs must be skipped if *args exists and is not empty

        Args:
            *args: “no-keyword argument”
            **kwargs: “key-worded argument”

        """
        data = ("id", "width", "height", "x", "y")
        if args:
            for i, elem in enumerate(args):
                setattr(self, data[i], elem)
        elif kwargs:
            for key, value in kwargs.items():
                if key in data:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle
        Must contain: id, width, height, x, y

        Returns:
            dict: representation of a Rectangle
        """
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['width'] = self.width
        dictionary['height'] = self.height
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary
