#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = abs(number)
temp = temp % 10
if number < 0 and temp != 0:
    temp = temp * -1
print('Last digit of {0} is {1} and is'.format(number, temp), end="")
if temp > 5:
    print(' greater that 5')
elif temp is 0:
    print(' 0')
else:
    print(' less than 6 and not 0')
