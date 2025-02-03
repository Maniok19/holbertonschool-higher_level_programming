#!/usr/bin/python3
"""Module that defines a base geometry class"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Defines a base class for shapes."""

    @abstractmethod
    def area(self):
        """Abstract method that should be
        implemented in child classes."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method that should be
        implemented in child classes."""
        pass


class Circle(Shape):
    """Defines a circle class."""
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        """Defines an area method for circles."""
        return 3.141592653589793 * self.__radius ** 2

    def perimeter(self):
        """Defines a perimeter method for circles."""
        return 2 * 3.141592653589793 * self.__radius


class Rectangle(Shape):
    """Defines a rectangle class."""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """Defines an area method for rectangles."""
        return self.__width * self.__height

    def perimeter(self):
        """Defines a perimeter method for rectangles."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Prints the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
