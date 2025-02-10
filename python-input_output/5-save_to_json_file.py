#!/usr/bin/python3
"""Module for saving objects to JSON files."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        obj = json.dumps(my_obj)
        f.write(obj)
