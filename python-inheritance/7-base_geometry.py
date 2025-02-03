#!/usr/bin/python3
""" Module for BaseGeometry class """


class BaseGeometry:
    """A class for basic geometric operations."""

    def area(self):
        """Raises an Exception indicating that the method
        is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer and greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
