#!/usr/bin/python3
""" Module for is_same_class method """


def is_same_class(obj, a_class):
    """ Returns True if the object is exactly
    an instance of the specified class """
    return type(obj) is a_class
