#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = argv
    if (len(args) - 1) == 1:
        print("{} argument:".format(len(args) - 1))
    elif (len(args) - 1) == 0:
        print("{} arguments.".format(len(args) - 1))
    else:
        print("{} arguments:".format(len(args) - 1))

        for i in args:
            if args.index(i) == 0:
                continue
            print("{}: {}".format(args.index(i), i))
