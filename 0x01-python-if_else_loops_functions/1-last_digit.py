#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10

if number < 0:
    lastDigit = number % -10

if number > 5:
    message = "and is greater than 5"
elif number == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, lastDigit, message))
