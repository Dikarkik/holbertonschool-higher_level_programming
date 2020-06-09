#!/usr/bin/python3
""" Unittest for ``/models/rectangle.py``

class Rectangle:
    0. __init__(self, width, height, x=0, y=0, id=None)
    1. width(self)
    2. width(self, width)
    3. height(self)
    4. height(self, height)
    5. x(self)
    6. x(self, x)
    7. y(self)
    8. y(self, y)
    9. is_int_validator(self, name_var, value)
    10. is_under_or_equals_0_validator(self, name_var, value)
    11. is_under_0_validator(self, name_var, value)
    12. area(self)
    13. display(self)
    14. __str__(self)
    15. update(self, *args, **kwargs)
    16. to_dictionary(self)

python3 -m unittest tests/test_models/test_rectangle.py
"""

import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """
    ------------------------------------------------------------
    0. __init__(self, width, height, x=0, y=0, id=None)
    ------------------------------------------------------------
    """
    def test_init_valid(self):
        r = Rectangle(1, 1, 0, 0, 11)
        self.assertEqual(r.id, 11)

    def test_init_miss_arguments(self):
        """ TypeError: __init__() missing 2 required positional
        arguments: 'width' and 'height' """
        self.assertRaises(TypeError, Rectangle)
        """ TypeError: __init__() missing 1 required positional
        argument: 'height' """
        self.assertRaises(TypeError, Rectangle, 1)

    def test_init_more_args(self):
        self.assertRaises(TypeError, Rectangle, 1, 1, 0, 0, 11, 999)

    """
    ------------------------------------------------------------
    1. width(self) ---@property---
    ------------------------------------------------------------
    """
    def test_width_getter_valid(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)

    """
    ------------------------------------------------------------
    2. width(self, width) ---@width.setter---
    ------------------------------------------------------------
    """
    def test_width_setter_valid(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        r.width = 11
        self.assertEqual(r.width, 11)

    def test_width_setter_typeError(self):
        """ TypeError: width must be an integer """
        self.assertRaises(TypeError, Rectangle, "abc", 1)
        self.assertRaises(TypeError, Rectangle, (1,), 1)
        self.assertRaises(TypeError, Rectangle, [1], 1)
        self.assertRaises(TypeError, Rectangle, 1.1, 1)
        self.assertRaises(TypeError, Rectangle, {1, 2}, 1)

    def test_width_setter_valueError(self):
        """ ValueError: width must be > 0 """
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, -1, 1)

    """
    ------------------------------------------------------------
    3. height(self) ---@property---
    ------------------------------------------------------------
    """

    def test_height_getter_valid(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.height, 2)

    """
    ------------------------------------------------------------
    4. height(self, height) ---@height.setter---
    ------------------------------------------------------------
    """
    def test_height_setter_valid(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.height, 2)
        r.height = 22
        self.assertEqual(r.height, 22)

    def test_height_setter_typeError(self):
        """ TypeError: height must be an integer """
        self.assertRaises(TypeError, Rectangle, 1, "abc")
        self.assertRaises(TypeError, Rectangle, 1, (1,))
        self.assertRaises(TypeError, Rectangle, 1, [1])
        self.assertRaises(TypeError, Rectangle, 1, 1.1)
        self.assertRaises(TypeError, Rectangle, 1, {1, 2})

    def test_height_setter_ValueError(self):
        """ ValueError: height must be > 0 """
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, -1)

    """
    ------------------------------------------------------------
    5. x(self) ---@property---
    ------------------------------------------------------------
    """
    def test_x_getter_valid(self):
        r = Rectangle(1, 2, 5)
        self.assertEqual(r.x, 5)

    """
    ------------------------------------------------------------
    6. x(self, x) ---@x.setter---
    ------------------------------------------------------------
    """
    def test_x_setter_valid(self):
        r = Rectangle(1, 2, 5)
        self.assertEqual(r.x, 5)
        r.x = 55
        self.assertEqual(r.x, 55)

    def test_x_setter_typeError(self):
        """ TypeError: x must be an integer """
        self.assertRaises(TypeError, Rectangle, 1, 1, "abc")
        self.assertRaises(TypeError, Rectangle, 1, 1, (1,))
        self.assertRaises(TypeError, Rectangle, 1, 1, [1])
        self.assertRaises(TypeError, Rectangle, 1, 1, 1.1)
        self.assertRaises(TypeError, Rectangle, 1, 1, {1, 2})

    def test_x_setter_valueError(self):
        """ ValueError: x must be >= 0 """
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)

    """
    ------------------------------------------------------------
    7. y(self) ---@property---
    ------------------------------------------------------------
    """
    def test_y_getter_valid(self):
        r = Rectangle(1, 2, 5, 8)
        self.assertEqual(r.y, 8)

    """
    ------------------------------------------------------------
    8. y(self, x) ---@y.setter---
    ------------------------------------------------------------
    """
    def test_y_setter_valid(self):
        r = Rectangle(1, 2, 5, 8)
        self.assertEqual(r.y, 8)
        r.y = 88
        self.assertEqual(r.y, 88)

    def test_y_setter_typeError(self):
        """ TypeError: y must be an integer """
        self.assertRaises(TypeError, Rectangle, 1, 1, 0, "abc")
        self.assertRaises(TypeError, Rectangle, 1, 1, 0, (1,))
        self.assertRaises(TypeError, Rectangle, 1, 1, 0, [1])
        self.assertRaises(TypeError, Rectangle, 1, 1, 0, 1.1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 0, {1, 2})

    def test_y_setter_valueError(self):
        """ ValueError: y must be >= 0 """
        self.assertRaises(ValueError, Rectangle, 1, 1, 0, -1)

    """
    ------------------------------------------------------------
    9. is_int_validator(self, name_var, value) ---@staticmethod---
    ------------------------------------------------------------
    """
    def test_is_int_validator_valid(self):
        self.assertEqual(Rectangle.is_int_validator("x", 1), None)

    def test_is_int_validator_typeError(self):
        self.assertRaises(TypeError, Rectangle.is_int_validator, "x", "abc")

    """
    ------------------------------------------------------------
    10. is_under_or_equals_0_validator(self, name_var, value) ---@sm---
    ------------------------------------------------------------
    """
    def test_is_under_or_equals_0_validator_valid(self):
        self.assertEqual(
            Rectangle.is_under_or_equals_0_validator("x", 1), None)

    def test_is_under_or_equals_0_validator_typeError(self):
        self.assertRaises(
            TypeError, Rectangle.is_under_or_equals_0_validator, "x", "abc")

    """
    ------------------------------------------------------------
    11. is_under_0_validator(self, name_var, value) ---@staticmethod---
    ------------------------------------------------------------
    """
    def test_is_under_0_validator_valid(self):
        self.assertEqual(Rectangle.is_under_0_validator("x", 1), None)

    def test_is_under_0_validator_valueError(self):
        self.assertRaises(ValueError, Rectangle.is_under_0_validator, "x", -1)

    """
    ------------------------------------------------------------
    12. area(self)
    ------------------------------------------------------------
    """
    def test_area(self):
        r = Rectangle(1, 1)
        self.assertEqual(r.area(), 1)
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)
        r = Rectangle(5, 3)
        self.assertEqual(r.area(), 15)

    """
    ------------------------------------------------------------
    13. display(self)
    ------------------------------------------------------------
    """
    def test_display(self):
        from io import StringIO
        from unittest.mock import patch

        r = Rectangle(1, 1)
        display_example = "#\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r.display()
        self.assertEqual(fakeOutput.getvalue(), display_example)

        r = Rectangle(4, 2, 3, 3)
        display_example = "\n\n\n   ####\n   ####\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r.display()
        self.assertEqual(fakeOutput.getvalue(), display_example)

    """
    ------------------------------------------------------------
    14. __str__(self)
    ------------------------------------------------------------
    """
    def test_str(self):
        r = Rectangle(1, 1, 8, 8, 10)
        self.assertEqual(r.__str__(), "[Rectangle] (10) 8/8 1/1")
        r = Rectangle(1, 1, 1, 1, 11)
        self.assertEqual(r.__str__(), "[Rectangle] (11) 1/1 1/1")

    """
    ------------------------------------------------------------
    15. update(self, *args, **kwargs)
    ------------------------------------------------------------
    """
    def test_update_args(self):
        r = Rectangle(1, 1)
        r.update(11, 2, 2, 8, 8)
        dir_example = {'_Rectangle__y': 8, '_Rectangle__x': 8,
                       'id': 11, '_Rectangle__height': 2,
                       '_Rectangle__width': 2}
        self.assertDictEqual(r.__dict__, dir_example)
        r.update(33, 11, 11, 11, 11)
        dir_example = {'_Rectangle__y': 11, '_Rectangle__x': 11,
                       'id': 33, '_Rectangle__height': 11,
                       '_Rectangle__width': 11}
        self.assertDictEqual(r.__dict__, dir_example)

    def test_update_kwargs(self):
        r = Rectangle(1, 1)
        r.update(y=8, x=8, id=11, height=2, width=2)
        dir_example = {'_Rectangle__y': 8, '_Rectangle__x': 8,
                       'id': 11, '_Rectangle__height': 2,
                       '_Rectangle__width': 2}
        self.assertDictEqual(r.__dict__, dir_example)
        r.update(id=33)
        dir_example = {'_Rectangle__y': 8, '_Rectangle__x': 8,
                       'id': 33, '_Rectangle__height': 2,
                       '_Rectangle__width': 2}
        self.assertDictEqual(r.__dict__, dir_example)

    def test_update_mix_args(self):
        r = Rectangle(1, 1)
        r.update(11, 2, 2, height=8, width=8)
        dir_example = {'_Rectangle__y': 0, '_Rectangle__x': 0,
                       'id': 11, '_Rectangle__height': 2,
                       '_Rectangle__width': 2}
        self.assertDictEqual(r.__dict__, dir_example)

    def test_update_invalid_keys(self):
        r = Rectangle(1, 1, 0, 0, 11)
        r.update(key1=1, key2=1)
        dir_example = {'_Rectangle__y': 0, '_Rectangle__x': 0,
                       'id': 11, '_Rectangle__height': 1,
                       '_Rectangle__width': 1}
        self.assertDictEqual(r.__dict__, dir_example)

    """
    ------------------------------------------------------------
    16. to_dictionary(self)
    ------------------------------------------------------------
    """
    def test_to_dictionary(self):
        r = Rectangle(1, 1, 0, 0, 11)
        new_dic = r.to_dictionary()
        dic_example = dict({'id': 11, 'width': 1,
                            'height': 1, 'x': 0, 'y': 0})
        self.assertDictEqual(new_dic, dic_example)
