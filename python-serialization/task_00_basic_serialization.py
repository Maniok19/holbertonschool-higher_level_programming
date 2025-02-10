#!/usr/bin/python3
""" Module that contains a function that serializes and deserializes"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes and saves to a file"""
    with open(filename, "a") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes a file"""
    with open(filename, "r") as f:
        return json.load(f)
