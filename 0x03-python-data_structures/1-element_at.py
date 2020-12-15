#!/usr/bin/python3
def element_at(my_list, idx):
    """Function that add a element
    Args:
        my_list: list to print
        idx: index to add
    Returns:
        my_list modific or None
    """
    if idx < 0 or len(my_list) <= idx:
        return (None)

    return(my_list[idx])
