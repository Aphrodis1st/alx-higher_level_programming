#!/usr/bin/python3
"""A function to sperate words in python"""
'''
File_name: 0-rectangle.py
Created: 12-Jan-2024
Author: Aphrodis Uwineza (Aphrodis1st)
Size: Large
Project: 0x08-python-more_classes
Status: Not yet submitted.
'''


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
