#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = argv
    if (len(args) - 1) == 1:
        print("{:d} argument:".format(len(args) - 1))
    elif (len(args) - 1) == 0:
        print("{:d} arguments.".format(len(args) - 1))
    else:
        print("{:d} arguments:".format(len(args) - 1))

        for i in args:
            if args.index(i) == 0:
                continue
            print("{:d}: {:s}".format(args.index(i), i))
