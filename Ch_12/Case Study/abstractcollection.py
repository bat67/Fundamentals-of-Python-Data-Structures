"""
File: abstractcollection.py

Common data and method implementations for collections.
Assumes that each collection type supports an iterator and
an add method.
"""

class AbstractCollection(object):
    """Represents an abstract collection for all collection types."""

    def __init__(self, sourceCollection):
        """Will copy items to self from sourceCollection
        if it's present."""
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __len__(self):
        """-> The number of items in self."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """-> The string representation of the collection, using the
        format [<item-1>, <item-2>, . . ., <item-n>]."""
        return "[" + ", ".join(map(str, self)) + "]"

    def __add__(self, other):
        """Returns a new collection consisting of the
        items in self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other): return False
        if len(self) != len(other): return False
        otherItems = iter(other)
        for item in self:
            if item != next(otherItems):
                return False
        return True
