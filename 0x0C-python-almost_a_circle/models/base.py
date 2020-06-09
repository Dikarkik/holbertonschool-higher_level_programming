#!/usr/bin/python3
"""Module: Base"""
import json


class Base:
    """ Base that allow serialize/deserialize """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
        if id is not None, assign the public
        instance attribute id with this argument value.
        Otherwise, increment __nb_objects and assign
        the new value to the public instance attribute id.

        Args:
            id (int, optional): id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list of dictionaries to JSON representation

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: the JSON string representation of list_dictionaries
            If list_dictionaries is None or empty, return the string: "[]"
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.
            If list_objs is None, save an empty list.
            The filename must be: <Class name>.json - example: Rectangle.json
            Must overwrite the file if it already exists

        Args:
            list_objs (list): list of instances who inherits of Base
            example: list of Rectangle or list of Square instances.
        """
        file_name = cls.__name__ + ".json"
        list_dictionaries = []

        if list_objs:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

        json_string = Base.to_json_string(list_dictionaries)

        with open(file_name, mode='w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON json_string

        Args:
            json_string (string): representing a list of dictionaries

        Returns:
            list: the list represented by json_string
            If json_string is None or empty, return an empty list
        """
        if json_string:
            return json.loads(json_string)
        return list([])

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Args:
            **dictionary: can be thought of as a double
            pointer to a dictionary

        Returns:
            object: isntance of a Rectangle or Square
        """
        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        must search the file: <Class name>.json
        example: Rectangle.json

        Returns:
            list: list of instances. The type of these instances
            depends on cls (current class using this method).
            If the file doesn’t exist, return an empty list.
        """
        from models.rectangle import Rectangle
        from models.square import Square

        file_name = cls.__name__ + ".json"
        list_dictionaries = []
        with open(file_name, mode='r', encoding='utf-8') as file:
            list_dictionaries = Base.from_json_string(file.read())

        list_instances = []
        for dictionary in list_dictionaries:
            new_instance = cls.create(**dictionary)
            list_instances.append(new_instance)

        return list_instances
