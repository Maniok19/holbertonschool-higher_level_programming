#!/usr/bin/python3
"""Module that prints a square with the character """


def print_square(size):
    """Function that prints a square with the character
    Args:
        size: integer
    return:
        None"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
