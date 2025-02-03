#!/usr/bin/python3
""" Duck typing - first element of a sequence """
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """ Shape class """
    @abstractmethod
    def area(self):
        """ Abstract method area """
        pass

    @abstractmethod
    def perimeter(self):
        """ Abstract method perimeter """
        pass


class Circle(Shape):
    """ Circle class """
    def __init__(self, radius):
        """ Circle class """
        self.__radius = radius

    def area(self):
        """ Area of a circle """
        return self.__radius ** 2 * pi

    def perimeter(self):
        """ Perimeter of a circle """
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """ Rectangle class """
    def __init__(self, width, height):
        """ Rectangle class """
        self.__width = width
        self.__height = height

    def area(self):
        """ Area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Perimeter of a rectangle """
        return 2 * (self.__width + self.__height)


def shape_info(obj):
    """ Print the area of the shape """
    print("Area: {}\nPerimeter: {}".format(obj.area(), obj.perimeter()))
