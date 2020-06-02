#!/usr/bin/python3
"""1. My list"""


class MyList(list):
    """class that inherits from <list>"""

    def print_sorted(self):
        """Public instance method that prints the list, but sorted"""
        print(sorted(self))
