#!/usr/bin/python3
"""8. Create object from a JSON file"""


def load_from_json_file(filename):
    import json
    with open(filename, encoding='utf-8') as file:
        obj = json.loads(file.read())
    return obj
