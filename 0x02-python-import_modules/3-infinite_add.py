#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    list = argv
    add = 0
    for i in list:
        if list.index(i) == 0:
            continue
        add += int(i)
    print('{}'.format(add))
