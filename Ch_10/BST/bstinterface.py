"""
File: BSTinterface.py
Author: Ken Lambert
"""

class BSTInterface(object):
    """Interface for all binary search trees."""

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
        """Supports a preorder traversal on a view of self."""
        return None

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        return None

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        return None

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        return None

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        return None

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        return False

    def __contains__(self, item):
        """Returns True if item is in self, or
        False otherwise."""
        return True

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
        return None

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass

    def add(self, item):
        """Adds item to self."""
        pass

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        pass

    def replace(self, item, newItem):
        """Precondition: item == newItem.
        Raises: KeyError if item != newItem.
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        return None

