#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list = dir(hidden_4)
    for i in list:
        if i[0] != "_":
            print(i)
