#!/usr/bin/python3
""" Module for Square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a Square instance with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
