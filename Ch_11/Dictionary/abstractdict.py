"""
File: abstractdict.py
Author: Ken Lambert
"""
from abstractcollection import AbstractCollection

class AbstractDict(AbstractCollection):
    """Common data and method implementations for dictionaries."""

    def __init__(self, sourceCollection):
        """Will copy items to the collection from sourceDictionary
        if it's present."""
        AbstractCollection.__init__(self)
        if sourceCollection:
            for key, value in sourceCollection:
                self[key] = value

    def __str__(self):
        return " {" + ", ".join(map(str, self.items())) + "}"

    def __add__(self, other):
        """Returns a new dictionary containing the contents
        of self and other."""
        result = type(self)(map(lambda item: (item.key, item.value),
                                self.items()))
        for key in other:
            result[key] = other[key]
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for key in self:
            if not key in other:
                return False
        return True

    def keys(self):
        """Returns an iterator on the keys in the dictionary."""
        return iter(self)

    def values(self):
        """Returns an iterator on the values in the dictionary."""
        return iter(map(lambda key: self[key], self))

    def items(self):
        """Returns an iterator on the entries in the dictionary."""
        return iter(map(lambda key: Item(key, self[key]), self))

class Item(object):
    """Represents a dictionary item.
    Supports comparisons by key."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        if type(self) != type(other): return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other): return False
        return self.key < other.key

    def __le__(self, other):
        if type(self) != type(other): return False
        return self.key <= other.key
