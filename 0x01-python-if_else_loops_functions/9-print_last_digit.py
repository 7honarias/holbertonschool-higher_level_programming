#!/usr/bin/python3
def print_last_digit(number):
    i = abs(number)
    print("{:d}".format(i % 10), end="")

    return (i % 10)
