"""
File: arraydict.py
Author: Ken Lambert
"""

from abstractdict import AbstractDict, Item

class ArrayDict(AbstractDict):
    """Represents an array-based dictionary."""

    def __init__(self, sourceCollection = None):
        """Will copy items to the collection from sourceCollection
        if it's present."""
        self._items = list()
        AbstractDict.__init__(self, sourceCollection)

    # Accessors
    def __iter__(self):
        """Serves up the keys in the dictionary."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor].key
            cursor += 1    

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        index = self._index(key)
        if index == -1: raise KeyError("Missing: " + str(key))
        return self._items[index].value

    # Mutators
    def __setitem__(self, key, value):
        """If the key is not in the dictionary,
        adds the key and value to it.
        Othwerise, replaces the old value with the new
        value."""
        index = self._index(key)
        if index == -1:
            self._items.append(Item(key, value))
            self._size += 1
        else:
            self._items[index].value = value

    def pop(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Removes the key and returns the associated value if the
        key in in the dictionary, or returns the default value
        otherwise."""
        index = self._index(key)
        if index == -1: raise KeyError("Missing: " + str(key))
        self._size -= 1
        return self._items.pop(index).value

    def _index(self, key):
        """Helper method for key search."""
        index = 0
        for entry in self._items:
            if entry.key == key:
                return index
            index += 1
        return -1       

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
    main(ArrayDict)

