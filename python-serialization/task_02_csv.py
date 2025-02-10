#!/usr/bin/python3
""" Module that contains a function that converts a CSV file to JSON"""
import csv
import json


def convert_csv_to_json(filename):
    """Converts a CSV file to JSON"""
    if not isinstance(filename, str):
        print("Error: filename must be a string")
        return False
    try:
        with open(filename, "r", encoding="utf-8") as f:
            csv_r = csv.DictReader(f)
            data = [row for row in csv_r]
        output_filename = filename.rsplit(".", 1)[0] + ".json"
        with open(output_filename, "w", encoding="utf-8") as g:
            json.dump(data, g, indent=4)
        return True
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
