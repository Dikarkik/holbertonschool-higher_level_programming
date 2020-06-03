#!/usr/bin/python3
"""7. Save Object to a file"""


def save_to_json_file(my_obj, filename):
    import json

    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
