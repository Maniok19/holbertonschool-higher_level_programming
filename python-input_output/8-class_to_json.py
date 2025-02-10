#!/usr/bin/python3
""" Module that contains a function that returns the dictionary description"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__
