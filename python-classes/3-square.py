#!/usr/bin/python3
"""Square class with a private instance attribute size"""


class Square:
    """Class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes the data."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
