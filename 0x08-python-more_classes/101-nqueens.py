#!/usr/bin/python3
import sys

my_list = []
if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    N = int(sys.argv[1])
except:
    print("N must be a number")
    sys.exit(1)

if N < 4:
        print("N must be at least 4")
        sys.exit(1)
p = 1
for x in range(1, N-1):
    j = 0
    my_list = []
    p = p + 1
    while j < N:
        ubic = [j, x]
        my_list.append(ubic)
        if x + p > N-1:
            x = x + p - N - 1
        else:
            x += p
        j += 1
    print(my_list)
