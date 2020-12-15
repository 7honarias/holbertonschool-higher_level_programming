#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Function that replace a element
    Args:
        my_list: list to print
    Returns:
        my_list always
    """
    if (idx < 0) or (len(my_list) <= idx):
        return (my_list)

    my_list[idx] = element
    return (my_list)
