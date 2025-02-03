#!/usr/bin/python3
""" Module for BaseGeometry class and Rectangle class """


class BaseGeometry:
    """ BaseGeometry class xoxoxoxoxoxoxoxoxox """
    def area(self):
        """ Raises an Exception with the message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value and checks if it is an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ BaseGeometry class and Rectangle class xoxoxo """

    def __init__(self, width, height):
        """ Initializes an instance and validates the values """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the rectangle and validates the values """
        return self.__width * self.__height

    def __str__(self):
        """ Returns the string representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Initializes an instance i love rocknroll """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Returns the string representation of the square """
        return "[Square] {}/{}".format(self.__size, self.__size)
