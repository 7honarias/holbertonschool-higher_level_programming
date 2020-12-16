#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if my_list:
        if idx < 0 or len(my_list) <= idx:
            return (my_list)
        x = my_list[idx]
        my_list.remove(x)
        return (my_list)
