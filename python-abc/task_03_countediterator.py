#!/usr/bin/python3
"""CountedIterator module."""


class CountedIterator:
    """CountedIterator class that inherits from list."""
    def __init__(self, iterable):
        """Initialize the CountedIterator object."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item in the iteration."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated."""
        return self.count
