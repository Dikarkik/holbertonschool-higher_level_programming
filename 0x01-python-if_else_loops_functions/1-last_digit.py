#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    print("Last digit of {} is {}".format(number, (number * -1) % 10))
else:
    print("Last digit of {} is {}".format(number, number % 10))
