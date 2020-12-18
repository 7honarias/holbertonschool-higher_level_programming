#!/usr/bin/python3
def weight_average(my_list=[]):
    top, inf = 0, 0
    if my_list:
        for item in my_list:
            top += (item[0] * item[1])
            inf += item[1]

        return (top/inf)

    return (0)
