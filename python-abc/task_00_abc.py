#!/usr/bin/python3
""" Module for task 0 """
from abc import ABC, abstractmethod


class Animal(ABC):
    """ Animal class """
    @abstractmethod
    def sound(self):
        """ Abstract method sound """
        pass


class Dog(Animal):
    """ Dog class """
    def sound(self):
        """ Dog sound """
        return "Bark"


class Cat(Animal):
    """ Cat class """
    def sound(self):
        """ Cat sound """
        return "Meow"
