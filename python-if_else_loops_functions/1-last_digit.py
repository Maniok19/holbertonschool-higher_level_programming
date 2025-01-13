#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    sup = "and is greater than 5"
if last_digit == 0:
    sup = "and is 0"
elif last_digit < 6:
    sup = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {:s}".format(number, last_digit, sup))
