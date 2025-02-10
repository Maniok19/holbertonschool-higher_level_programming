#!/usr/bin/python3
""" Module that contains a function that converts a CSV file to JSON"""
import csv
import json


def convert_csv_to_json(filename):
    """Converts a CSV file to JSON"""

    data = []
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("file not found")
        return False

    with open("data.json", "w") as f:
        f.write(json.dumps(data))
    return True
