#!/usr/bin/python3
"""Module for VerboseList class."""


class VerboseList(list):
    """Defines a verbose list class."""
    def append(self, item):
        """Appends an item to the list."""
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, x):
        """Extends the list with another"""
        super().extend(x)
        print("Extended the list with {} items.".format(len(x)))

    def remove(self, item):
        """Removes an item from the list"""
        super().remove(item)
        print("Removed {} from the list.".format(item))

    def pop(self, index=-1):
        """Pops an item from the list"""
        item = super().pop(index)
        print("Popped {} from the list.".format(item))
        return item
