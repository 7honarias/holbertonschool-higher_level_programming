#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    index = 0

    if matrix:
        for lts in matrix:
            index = 0
            for num in lts:
                if index != len(lts) - 1:
                    print("{:d}".format(num), end=" ")
                    index += 1
                else:
                    print("{:d}".format(num), end="")
            print()
