#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, number % 10))
elif number == 0:
    print("Last digit of {} is {} and is 0".format(number, number % 10))
else:
    if number < 0:
        print("Last digit of {} is {}".format(number, (number * -1) % 10))
    else:
        print("Last digit of {} is {}".format(number, number % 10))
