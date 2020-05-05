#!/usr/bin/python3
# function that prints all integers of a list.


def print_list_integer(my_list=[]):
    for element in my_list:
        print("{:d}".format(element))

if __name__ == "__main__":
    print_list_integer()
