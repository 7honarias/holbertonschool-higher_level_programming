#!/usr/bin/python3
"""only one function
"""


def text_indentation(text):
    """print text

    Args:
        text (text): text to print 

    Raises:
        TypeError: must be a string, otherwise
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    space = " "
    while len(text) > i:
        if text[i - 1] in ('.', ':', '?') and i != 0:
            if text[i] is space:
                print("\n")
                i += 1
                continue
            else:
                print("\n")
        print("{}".format(text[i]), end="")
        i += 1
