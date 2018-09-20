"""
File: linkedbag.py
Author: Ken Lambert
"""

from node import Node
from abstractdict import AbstractDict, Item

class LinkedDict(AbstractDict):
    """A link-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Include a reference to previous node for popping
        self._items = self._previousNode = None
        AbstractDict.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._items
        while not cursor is None:
            yield cursor.data.key
            cursor = cursor.next

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        index = self._index(key)
        if index is None: raise KeyError("Missing: " + str(key))
        return index.data.value

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = None

    def __setitem__(self, key, value):
        """If the key is not in the dictionary,
        adds the key and value to it.
        Othwerise, replaces the old value with the new
        value."""
        index = self._index(key)
        if index == None:
            self._items = Node(Item(key, value), self._items)
            self._size += 1
        else:
            index.data.value = value

    def pop(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Removes the key and returns the associated value if the
        key in in the dictionary, or returns the default value
        otherwise."""
        index = self._index(key)
        if index is None: raise KeyError("Missing: " + str(key))
        self._size -= 1
        # Two cases: either at the head or thereafter.
        if self._previousNode is None:
            self._items = self._items.next
        else:
            self._previousNode.next = index.next
        return index.data.value

    def _index(self, key):
        """Helper method for key search."""
        # Tracks the node before the node containing the key
        self._previousNode = None
        index = self._items
        while index != None:
            if index.data.key == key:
                return index
            self._previousNode = index
            index = index.next
        return None       
        
def main(dictionaryType = dict):
    d = dictionaryType()
    for key in range(1, 6):
        d[key] = "Value" + str(key)
    print("\nLength: ", len(d))
    print("\nThe dictionary:", d)
    aClone = dictionaryType(map(lambda item: (item.key, item.value), d.items()))
    print("\nA clone:", aClone)
    print("\nThe keys:", set(d.keys()))
    print("\nThe values:", list(d.values()))
    print("\nKey Value (using [])")
    for key in d:
        print(key, " ", d[key])
    print("\nDelete all keys:")
    for key in range(1, 6):
        print(d.pop(key))
    print("\nLength: ", len(d))
    newD = dictionaryType([(7, 8), (2, 3), (8, 9)])
    print("\nA clone:", aClone)
    print("\nA second dictionary:", newD)
    print("\nA Concatenate a clone and second:", aClone + newD)
    
# Include your dictionary type as an argument to main
if __name__ == "__main__":
    main(LinkedDict)

