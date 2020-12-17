#!/usr/bin/python3
def search_replace(my_list, search, replace):

    """Write a function that replaces all occurrences of
    an element by another in a new list.

    my_list: is the initial list
    search: is the element to replace in the list
    replace: is the new element"""

    new_list = list(map(lambda a: replace if (a == search) else a, my_list))
    return (new_list)
