#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Function that prints a list
    Args:
        my_list: list to print
        idx: index
        element: number to change
    Returns:
        new list
    """
    if idx < 0 or len(my_list) <= idx:
        return (my_list)
    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
