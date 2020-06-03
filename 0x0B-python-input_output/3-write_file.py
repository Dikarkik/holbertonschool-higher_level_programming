#!/usr/bin/python3
"""3. Write to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file and
    returns the number of characters written:

    Args:
        filename (str, optional): name to create the file
        text (str, optional): must be str

    Returns:
        [int]: number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
