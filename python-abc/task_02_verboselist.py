#!/usr/bin/python3
"""Module for VerboseList class."""


class VerboseList(list):
    """VerboseList class that inherits from list."""
    def append(self, item):
        """Append an item to the list and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend the list and print a message."""
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, value):
        """Remove a value from the list and print a message."""
        super().remove(value)
        print("Removed [{}] from the list.".format(value))

    def pop(self, index=-1):
        """pop an item from the list and notify"""
        value = super().pop(index)
        print("Popped [{}] from the list.".format(value))
        return super().pop(index)
