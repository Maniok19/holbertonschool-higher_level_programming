#!/usr/bin/python3
""" Module that contains a function that returns
an object (Python data structure)"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string"""
    return json.loads(my_str)
