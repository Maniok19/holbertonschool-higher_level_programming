#!/usr/bin/python3
""" Module that contains a class MyClass"""


class MyClass:
    """ My class
    """

    def __init__(self, name):
        """ Constructor method"""
        self.name = name
        self.number = 0

    def __str__(self):
        """ Method that returns a string"""
        return "[MyClass] {} - {:d}".format(self.name, self.number)
