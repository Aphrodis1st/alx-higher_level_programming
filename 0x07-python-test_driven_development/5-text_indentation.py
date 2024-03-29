#!/usr/bin/python3
"""Defines a text-indentation function."""
'''
Created: 12-Jan-2024
Author: Aphrodis Uwineza (Aphrodis1st)
Author: UMUTONI Kevine (simplykevine)
Size: Large
Project: 0x08-python-more_classes
Status: Not yet submitted.
'''


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
