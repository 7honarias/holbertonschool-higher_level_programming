#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (i >= 'a') and (i <= 'z'):
            print('{:c}'.format(ord(i) - 32), end = '')
        else:
            print('{:c}'.format(ord(i)), end = '')
    print()
