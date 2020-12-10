#!/usr/bin/python3
from sys import argv
if __name__ == "__main__"
arguments = argv
size = len(arguments)
if size != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

operator = arguments[2]
num1 = int(arguments[1])
num2 = int(arguments[3])

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
