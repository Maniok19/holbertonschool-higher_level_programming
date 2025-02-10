#!/usr/bin/python3
""" Module that contains a class Student that defines a student"""


class Student:
    """ Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """ Constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method that retrieves a dictionary representation"""
        return self.__dict__
