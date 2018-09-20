"""
File: setinterface.py
Author: Ken Lambert
"""

class SetInterface(object):
    """Interface for all set types."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        pass

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return True
    
    def __len__(self):
        """-Returns the number of items in self."""
        return 0

    def __str__(self):
        """Returns the string representation of self."""
        return ""

    def __iter__(self):
        """Supports iteration over a view of self."""
        return None

    def __add__(self, other):
        """Returns a new set containing the contents
        of self and other."""
        return None

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        return False

    def __or__(self, other):
        """Returns the union of self and other."""
        return self

    def __and__(self, other):
        """Returns the intersection of self and other."""
        return self
        
    def __sub__(self, other):
        """Returns the difference of self and other."""
        return self

    def issubset(self, other):
        """Returns True if self is a subset of other
        or False otherwise."""
        return self


    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass

    def add(self, item):
        """Adds item to self."""
        pass

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        postcondition: item is removed from self."""
        pass
