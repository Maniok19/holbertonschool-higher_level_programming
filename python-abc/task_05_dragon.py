#!/usr/bin/python3
""" Module for storing the Dragon class. """


class SwimMixin:
    """ Mixin class for swimming. """
    def swim(self):
        """ Swim method. """
        print("The creature swims!")


class FlyMixin:
    """ Mixin class for flying. """
    def fly(self):
        """ Fly method. """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """ Dragon class. """
    def roar(self):
        """ Roar method. """
        print("The dragon roars!")
