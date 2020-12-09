#!/usr/bin/python3
i = 122
while i >= 97:
    a = i
    if i % 2 != 0:
        a = a - 32
    print('{}'.format(chr(a)), end="")
    i -= 1
