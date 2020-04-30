#!/usr/bin/python3
import sys


def args_addition():
    n = len(sys.argv)
    total = 0
    for i in range(1, n):
        total = total + int(sys.argv[i])
    print("{:d}".format(total))

if __name__ == "__main__":
    args_addition()
