#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): name of the text file. Defaults to "".
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
