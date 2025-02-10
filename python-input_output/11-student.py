#!/usr/bin/python3
""" Module that contains a class Student """


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes included
        Otherwise, all attributes are retrieved.
        """
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with those in json
        """
        for key, value in json.items():
            setattr(self, key, value)
