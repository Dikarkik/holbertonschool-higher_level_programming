#!/usr/bin/python3
"""2. Exact same object"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance 
    of the specified class"""
    if type(obj) == a_class:
        return True
    return False
