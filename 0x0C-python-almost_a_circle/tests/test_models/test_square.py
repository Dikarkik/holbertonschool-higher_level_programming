#!/usr/bin/python3
"""Unittest for ``/models/square.py``

class Square:
    0. __init__(self, size, x=0, y=0, id=None)
    1. __str__(self)
    2. size(self)
    3. size(self, value)
    4. update(self, *args, **kwargs)
    5. to_dictionary(self)

python3 -m unittest tests/test_models/test_square.py
"""

import unittest
from models.square import Square
import pep8


class TestSquare(unittest.TestCase):
    """
    ------------------------------------------------------------
    0. __init__(self, size, x=0, y=0, id=None)
    ------------------------------------------------------------
    """
    def test_init_valid(self):
        s = Square(1, 0, 0, 11)
        self.assertEqual(s.id, 11)

    def test_init_miss_argument(self):
        """ TypeError: __init__() missing 1
        required positional argument: 'size' """
        self.assertRaises(TypeError, Square)

    def test_init_more_args(self):
        self.assertRaises(TypeError, Square, 1, 0, 0, 11, 999)
    """
    ------------------------------------------------------------
    1. __str__(self)
    ------------------------------------------------------------
    """
    def test_str(self):
        s = Square(1, 0, 0, 11)
        self.assertEqual(s.__str__(), "[Square] (11) 0/0 - 1")
        s = Square(3, 6, 6, 11)
        self.assertEqual(s.__str__(), "[Square] (11) 6/6 - 3")

    """
    ------------------------------------------------------------
    2. size(self) ---@property---
    ------------------------------------------------------------
    """
    def test_size_getter_valid(self):
        s = Square(1, 0, 0, 11)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)

    """
    ------------------------------------------------------------
    3. size(self, value) ---@size.setter---
    ------------------------------------------------------------
    """
    def test_size_setter_valid(self):
        s = Square(1, 0, 0, 11)
        s.size = 33
        self.assertEqual(s.width, 33)
        self.assertEqual(s.height, 33)

    def test_size_setter_typeError(self):
        """ TypeError: width must be an integer """
        self.assertRaises(TypeError, Square, "abc")
        self.assertRaises(TypeError, Square, (1,))
        self.assertRaises(TypeError, Square, [1])
        self.assertRaises(TypeError, Square, 1.1)
        self.assertRaises(TypeError, Square, {1, 2})

    def test_size_setter_valueError(self):
        """ ValueError: width must be > 0 """
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)

    """
    ------------------------------------------------------------
    4. update(self, *args, **kwargs)
    ------------------------------------------------------------
    """
    def test_update_args(self):
        s = Square(1)
        s.update(11, 2, 8, 8)
        dir_example = {'_Rectangle__y': 8, '_Rectangle__x': 8,
                       'id': 11, '_Rectangle__height': 2,
                       '_Rectangle__width': 2}
        self.assertDictEqual(s.__dict__, dir_example)
        s.update(33, 1, 1, 1)
        dir_example = {'_Rectangle__y': 1, '_Rectangle__x': 1,
                       'id': 33, '_Rectangle__height': 1,
                       '_Rectangle__width': 1}
        self.assertDictEqual(s.__dict__, dir_example)

    def test_update_kwargs(self):
        s = Square(1)
        s.update(size=3, id=11, y=1, x=1)
        dir_example = {'_Rectangle__y': 1, '_Rectangle__x': 1,
                       'id': 11, '_Rectangle__height': 3,
                       '_Rectangle__width': 3}
        self.assertDictEqual(s.__dict__, dir_example)
        s.update(id=33)
        dir_example = {'_Rectangle__y': 1, '_Rectangle__x': 1,
                       'id': 33, '_Rectangle__height': 3,
                       '_Rectangle__width': 3}
        self.assertDictEqual(s.__dict__, dir_example)

    def test_update_mix_args(self):
        s = Square(1)
        s.update(11, 2, height=8, width=8)
        dir_example = {'_Rectangle__y': 0, '_Rectangle__x': 0,
                       'id': 11, '_Rectangle__height': 2,
                       '_Rectangle__width': 2}
        self.assertDictEqual(s.__dict__, dir_example)

    def test_update_invalid_keys(self):
        s = Square(1, 0, 0, 11)
        s.update(key1=1, key2=1)
        dir_example = {'_Rectangle__y': 0, '_Rectangle__x': 0,
                       'id': 11, '_Rectangle__height': 1,
                       '_Rectangle__width': 1}
        self.assertDictEqual(s.__dict__, dir_example)

    """
    ------------------------------------------------------------
    5. to_dictionary(self)
    ------------------------------------------------------------
    """
    def test_to_dictionary(self):
        s = Square(1, 0, 0, 11)
        new_dic = s.to_dictionary()
        dic_example = dict({'id': 11, 'size': 1, 'x': 0, 'y': 0})
        self.assertDictEqual(new_dic, dic_example)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")