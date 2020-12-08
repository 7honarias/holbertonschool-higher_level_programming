#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    temp = number % 10
if number < 0:
    temp = number % -10

print('Last digit of {0} is {1} and is'.format(number, temp), end="")

if temp > 5:
    print(' greater that 5')
elif temp == 0:
    print(' 0')
else:
    print(' less than 6 and not 0')
