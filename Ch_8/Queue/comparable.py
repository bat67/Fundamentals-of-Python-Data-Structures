"""
File: comparable.py
Author: Ken Lambert

Wrapper class for tagging data with priority values.

To instantiate, use

<variable> = Comparable(<datum>, <optional int priority value>)

The priority value is 1 default.
"""

class Comparable(object):

    def __init__(self, data, priority = 1):
        self._data = data
        self._priority = priority

    def __str__(self):
        """Returns the string rep of the contained datum."""
        return str(self._data)

    def __eq__(self, other):
        """Returns True if the contained priorities are equal
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other): return False
        return self._priority == other._priority

    def __lt__(self, other):
        """Returns True if self's priority < other's priority,
        or False otherwise."""
        return self._priority < other._priority

    def __le__(self, other):
        """Returns True if self's priority <= other's priority,
        or False otherwise."""
        return self._priority <= other._priority

    def getData(self):
        """Returns the contained datum."""
        return self._data 

    def getPriority(self):
        """Returns the contained priority."""
        return self._priority 
