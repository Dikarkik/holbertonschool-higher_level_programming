#!/usr/bin/python3
import hidden_4


def print_names():
    list = dir(hidden_4)
    for e in list:
        if e[0] != '_' and e[1] != '_':
            print(e)

if __name__ == "__main__":
    print_names()
