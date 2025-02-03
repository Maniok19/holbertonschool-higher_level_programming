#!/usr/bin/python3
"""Module for VerboseList class."""


class VerboseList(list):
    """VerboseList class that inherits from list."""
    def append(self, item):
        """Append an item to the list and print a message."""
        print("Added {} to the list.".format(item))
        super().append(item)

    def extend(self, items):
        """Extend the list and print a message."""
        print("Extended the list with {} items.".format(len(items)))
        super().extend(items)

    def remove(self, value):
        """Remove a value from the list and print a message."""
        print("Removed {} from the list.".format(value))
        super().remove(value)

    def pop(self, index=-1):
        """pop an item from the list and notify"""
        value = super().pop(index)
        print("Popped {} from the list.".format(value))
        super().pop(index)
