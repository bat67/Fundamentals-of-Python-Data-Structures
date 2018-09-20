"""
File: Dictinterface.py
Author: Ken Lambert
"""

class DictInterface(object):
    """Interface for all dictionaries."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, which is an interable object
        over key/value pairs, if it's present."""
        pass

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return True
    
    def __len__(self):
        """Returns the number of items in self."""
        return 0

    def __str__(self):
        """Returns the string representation of self."""
        return ""

    def __iter__(self):
        """Serves up the keys in the dictionary."""
        return None

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        return False

    def __contains__(self, key):
        """Returns True if key is in self, or
        False otherwise."""
        return True

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        return None

    def get(self, key, defaultValue = None):
        """Returns the associated value if the key in in the
        dictionary, or returns the default value otherwise."""
        return defaultValue

    def keys(self):
        """Returns an iterator on the keys in the dictionary."""
        return iter(list())

    def values(self):
        """Returns an iterator on the values in the dictionary."""
        return iter(list())

    def items(self):
        """Returns a iterator on the items in the dictionary."""
        return iter(list())
    
    def __add__(self, otherDict):
        """Returns a dictionary containing the items of self and
        otherDict.  When keys are equal, the value in otherDict replaces
        the value in self."""
        return type(self)()

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass

    def add(self, item):
        """Adds item to self."""
        pass

    def pop(self, key):
        """recondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Removes the key and returns the associated value."""
        return None

    def __setitem__(self, key, value):
        """If the key is not in the dictionary,
        adds the key and value to it.
        Othwerise, replaces the old value with the new
        value."""
        pass


