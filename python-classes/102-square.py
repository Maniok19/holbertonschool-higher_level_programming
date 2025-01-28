#!/usr/bin/python3
"""Square class with a private instance attribute size"""


class Square:
    """Class that defines a square with a private size attribute."""
    def __init__(self, size=0):
        """Initializes the data."""
        self.size = size

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compares two squares."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares two squares."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compares two squares."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compares two squares."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compares two squares."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compares two squares."""
        return self.area() >= other.area()
