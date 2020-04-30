#!/usr/bin/python3
import sys


def arguments():
    n = len(sys.argv)
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(n - 1))
    for i in range(1, n):
        print("{:d}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    arguments()
