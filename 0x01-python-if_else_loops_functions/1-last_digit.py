#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = abs(number)
temp = temp % 10
if number < 0:
    temp = temp * -1

if temp > 5:
    print('Last digit of {:d}'.format(number),
          'is {:d} and is greater that 5'.format(temp))
elif temp is 0:
    print('Last digit of {:d}'.format(number),
          'is {:d} and is 0'.format(temp))
else:
    print('Last digit of {:d}'.format(number),
          'is {:d} and is less than 6 and not 0'.format(temp))
