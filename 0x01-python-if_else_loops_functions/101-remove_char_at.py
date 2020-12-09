#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    cp = ""
    for x in str:
        if i == n:
            i += 1
            continue
        cp += x
        i += 1
    return (cp)
