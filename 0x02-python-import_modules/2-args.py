#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if (len(argv) - 1) == 1:
        print("{:d} argument:".format(len(argv) - 1))
    elif (len(argv - 1) == 0:
        print("{:d} arguments.".format(len(argv) - 1))
    else:
        print("{:d} arguments:".format(len(argv) - 1))

        for i in argv:
            if argv.index(i) == 0:
                continue
            print("{:d}: {:s}".format(argv.index(i), i))
