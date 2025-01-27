#!/usr/bin/python3
"""Rectangle class with a private instance attribute width and height"""


class Rectangle:
    """Rectangle class with a private instance attribute width and height"""
    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the rectangle with the character #."""
        return "{}".format('\n'.join(['#' * self.width for
                                     i in range(self.height)]))

    def __repr__(self):
        """Returns the string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)
