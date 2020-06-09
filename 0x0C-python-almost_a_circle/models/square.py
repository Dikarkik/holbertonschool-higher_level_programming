#!/usr/bin/python3
""" Module: Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines a Square """
    def __init__(self, size, x=0, y=0, id=None):
        """constructor

        Args:
            size (int): width and height
            x (int, optional): must be integer. Defaults to 0.
            y (int, optional): must be integer. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """define format

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ retrieves size value """
        return self.width

    @size.setter
    def size(self, value):
        """ set width and height value """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """using *args: assign an argument to each attribute
        Order must be id, size, x, y

        using **kwargs: assigns a key/value argument to attributes
        **kwargs can be thought of as a
        double pointer to a dictionary: key/value
        **kwargs must be skipped if *args exists and is not empty

        Args:
            *args: “no-keyword argument”
            **kwargs: “key-worded argument”

        """
        data = ("id", "size", "x", "y")
        if args:
            for i, elem in enumerate(args):
                if i == 1:
                    setattr(self, "width", elem)
                    setattr(self, "height", elem)
                else:
                    setattr(self, data[i], elem)
        elif kwargs:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                elif key in data:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square
        Must contain: id, size, x, y

        Returns:
            dict: representation of s Square
        """
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['size'] = self.width
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary
