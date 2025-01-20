#!/usr/bin/python3
"""Module that adds 2 integers
description
    add_integer(a, b=98)
returns
    sum of a and b"""


def add_integer(a, b=98):
    """Function that adds 2 integers
    Args:
        a: integer or float"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
