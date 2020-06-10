#!/usr/bin/python3
""" Unittest for ``/models/base.py``

class Base:
    0. __init__(self, id=None)
    1. to_json_string(list_dictionaries)
    2. save_to_file(cls, list_objs)
    3. from_json_string(json_string)
    4. create(cls, **dictionary)
    5. load_from_file(cls)

python3 -m unittest tests/test_models/test_base.py
"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestBase(unittest.TestCase):
    """
    ------------------------------------------------------------
    0. __init__(self, id=None)
    ------------------------------------------------------------
    """
    def test_valid(self):
        obj = Base(11)
        self.assertEqual(obj.id, 11)

    def test_id_increment(self):
        """ test if __nb_objects is correctly incrementing """
        obj1 = Base()
        nb_objects_value = obj1.id
        obj2 = Base()
        self.assertEqual(obj2.id, nb_objects_value + 1)
        obj3 = Base()
        self.assertEqual(obj3.id, nb_objects_value + 2)

    def test_id_negative(self):
        obj = Base(-3)
        self.assertEqual(obj.id, -3)

    """
    ------------------------------------------------------------
    1. to_json_string(list_dictionaries) ---@staticmethod---
    ------------------------------------------------------------
    """
    def test_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_with_1_dict(self):
        list_dictionaries = [
            {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        ]
        self.assertEqual(Base.to_json_string(list_dictionaries),
                         json.dumps(list_dictionaries))

    def test_list_with_2_dict(self):
        list_dictionaries = [
            {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8},
            {'x': 1, 'width': 1, 'id': 2, 'height': 5, 'y': 5}
        ]
        self.assertEqual(Base.to_json_string(list_dictionaries),
                         json.dumps(list_dictionaries))

    """
    ------------------------------------------------------------
    2. save_to_file(cls, list_objs) - --@classmethod---
    ------------------------------------------------------------
    """
    def test_none(self):
        Rectangle.save_to_file(None)
        with open('Rectangle.json', encoding='utf-8') as file:
            result = file.read()
        self.assertEqual(result, "[]")

    def test_1_rectangle(self):
        json_example = '[{"id": 1, "x": 0, "y": 0, "width": 1, "height": 1}]'
        rec = Rectangle(1, 1, 0, 0, 1)
        Rectangle.save_to_file([rec])
        with open('Rectangle.json', encoding='utf-8') as file:
            result = file.read()
        self.assertEqual(json.loads(result),
                         json.loads(json_example))

    def test_2_rectangles(self):
        rec1 = Rectangle(1, 1, 0, 0, 1)
        rec2 = Rectangle(2, 2, 0, 0, 2)
        json_example = '[{"id": 1, "x": 0, "y": 0, "width": 1, "height": 1}, \
                     {"id": 2, "x": 0, "y": 0, "width": 2, "height": 2}]'
        Rectangle.save_to_file([rec1, rec2])
        with open('Rectangle.json', encoding='utf-8') as file:
            result = file.read()
        self.assertEqual(json.loads(result),
                         json.loads(json_example))

    def test_1_square(self):
        square = Square(1, 0, 0, 1)
        json_example = '[{"id": 1, "x": 0, "y": 0, "size": 1}]'
        Square.save_to_file([square])
        with open('Square.json', encoding='utf-8') as file:
            result = file.read()
        self.assertEqual(json.loads(result), json.loads(json_example))

    def test_2_squares(self):
        square1 = Square(1, 0, 0, 1)
        square2 = Square(2, 0, 0, 2)
        json_example = str('[{"id": 1, "x": 0, "y": 0, "size": 1},\
                {"id": 2, "x": 0, "y": 0, "size": 2}]')
        Square.save_to_file([square1, square2])
        with open('Square.json', encoding='utf-8') as file:
            result = file.read()
        self.assertEqual(json.loads(result), json.loads(json_example))

    """
    ------------------------------------------------------------
    3. from_json_string(json_string) ---@staticmethod---
    ------------------------------------------------------------
    """
    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_list_with_1_dictionary(self):
        a_list = [{'size': 1, 'y': 0, 'x': 0, 'id': 1}]
        a_json = json.dumps(a_list)
        self.assertEqual(Base.from_json_string(a_json), a_list)

    def test_list_with_2_dictionary(self):
        a_list = [
            {'size': 1, 'y': 0, 'x': 0, 'id': 1},
            {'size': 2, 'y': 0, 'x': 0, 'id': 2}]
        a_json = json.dumps(a_list)
        self.assertEqual(Base.from_json_string(a_json), a_list)

    """
    ------------------------------------------------------------
    4. create(cls, **dictionary) ---@classmethod---
    ------------------------------------------------------------
    """
    def test_valid(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(print(r1), print(r2))

    def test_typeError(self):
        """ TypeError: create() takes 1 positional argument
         but 2 were given """
        self.assertRaises(TypeError, Rectangle.create, None)
        self.assertRaises(TypeError, Rectangle.create, 1)
        self.assertRaises(TypeError, Rectangle.create, "abc")
        self.assertRaises(TypeError, Rectangle.create, [1])
        self.assertRaises(TypeError, Rectangle.create, (1,))

    def test_empty_dir(self):
        self.assertEqual(Rectangle.create(**{}), None)

    """
    ------------------------------------------------------------
    5. load_from_file(cls) ---@classmethod---
    ------------------------------------------------------------
    """
    def test_json_empty(self):
        with open("Rectangle.json", mode='w', encoding='utf-8') as file:
            file.write('[]')
        list_empty = Rectangle.load_from_file()
        self.assertEqual(print(list_empty), print("[]"))

    def test_json_with_1_rectangle(self):
        with open("Rectangle.json", mode='w', encoding='utf-8') as file:
            file.write('[{"id": 1, "x": 0, "y": 0, "width": 1, "height": 1}]')
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(print(list_rectangles[0]),
                         print("[Rectangle](1) 0/0 1/1"))

    def test_json_with_2_rectangle(self):
        with open("Rectangle.json", mode='w', encoding='utf-8') as file:
            file.write('[{"id": 1, "x": 0, "y": 0, "width": 1, "height": 1}, \
                {"id": 2, "x": 0, "y": 0, "width": 2, "height": 2}]')
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(print(list_rectangles[0]), print(
            "[Rectangle](1) 0/0 1/1"))
        self.assertEqual(print(list_rectangles[1]), print(
            "[Rectangle](2) 0/0 2/2"))

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")