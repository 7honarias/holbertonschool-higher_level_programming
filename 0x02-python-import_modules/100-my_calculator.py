#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    arguments = argv
    size = len(arguments)
    if size != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = arguments[2]
    num1 = int(arguments[1])
    num2 = int(arguments[3])

    if operator == "+":
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))
    elif operator == "-":
        print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
    elif operator == "*":
        print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
    elif operator == "/":
        print("{} / {} = {}".format(num1, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
