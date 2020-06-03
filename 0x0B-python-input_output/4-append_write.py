#!/usr/bin/python3
"""4. Append to a file"""


def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
