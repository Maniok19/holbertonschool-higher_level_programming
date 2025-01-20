#!/usr/bin/python3
"""Module that prints a name"""


def say_my_name(first_name, last_name=""):
    """Function that prints a name
    Args:
        first_name: string
        last_name: string
    return:
    None"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if first_name == "" and last_name == "":
        print("My name is")
    elif first_name == "":
        print("My name is {:s}".format(last_name))
    elif last_name == "":
        print("My name is {:s}".format(first_name))
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
