"""
File: abstractlist.py
Author: Ken Lambert
"""

from abstractcollection import AbstractCollection

class AbstractList(AbstractCollection):
    """Represents an abstract list."""

    def __init__(self, sourceCollection):
        """Maintains a count of modifications to the list."""
        self._modCount = 0
        AbstractCollection.__init__(self, sourceCollection)

    def getModCount(self):
        """Returns the count of modifications to the list."""
        return self._modCount

    def incModCount(self):
        """Increments the count of modifications to the list."""
        self._modCount += 1

    def index(self, item):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        position = 0
        for data in self:
            if data == item:
                return position
            else:
                position += 1
        if position == len(self):
            raise ValueError(str(item) + " not in list.")

    def remove(self, item):
        """Precondition: item is in self.
        Raises: ValueError if item in not in self.
        Postcondition: item is removed from self."""
        position = self.index(item)
        self.pop(position)

    def add(self, item):
        """Adds the item to the end of the list."""
        self.insert(len(self), item)

    def append(self, item):
        """Adds the item to the end of the list."""
        self.add(item)





