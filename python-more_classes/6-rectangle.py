#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return "{}".format('\n'.join(['#' * self.width for i in range(self.height)]))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
    
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

