"""
File: ermodel.py
Author: Ken Lambert

Defines the classes ERModel, Patient, and Condition for an
emergency room scheduler.
"""

from linkedpriorityqueue import LinkedPriorityQueue

class Condition(object):
    """Represents a condition."""

    def __init__(self, rank):
        self._rank = rank

    def __eq__(self, other):
        return self._rank == other._rank

    def __lt__(self, other):
        return self._rank < other._rank

    def __le__(self, other):
        return self._rank <= other._rank

    def __str__(self):
        """Returns the string rep of a condition."""
        if   self._rank == 1: return "critical"
        elif self._rank == 2: return "serious"
        else:                 return "fair"

class Patient(object):
    """Represents a patient with a name and a condition."""

    def __init__(self, name, condition):
        self._name = name
        self._condition = condition

    def __eq__(self, other):
        return self._condition == other._condition

    def __lt__(self, other):
        return self._condition < other._condition

    def __le__(self, other):
        return self._condition <= other._condition

    def __str__(self):
        """Returns the string rep of a patient."""
        return self._name + " / " + str(self._condition)

class ERModel(object):
    """Model of a scheduler."""

    def __init__(self):
        pass

    def isEmpty(self):
        """Returns True if there are patients in the model
        or False otherwise."""
        return True

    def schedule(self, p):
        """Adds a patient to the schedule."""
        pass

    def treatNext(self):
        """Returns the patient treated or None if there are none."""
        return None
