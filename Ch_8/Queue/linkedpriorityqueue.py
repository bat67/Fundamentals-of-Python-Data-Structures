"""
File: linkedpriorityqueue.py
"""

from node import Node
from linkedqueue import LinkedQueue

class LinkedPriorityQueue(LinkedQueue):
    """A link-based priority queue implementation."""


    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        LinkedQueue.__init__(self, sourceCollection)

    def add(self, item):
        """Adds item to its proper place in the queue."""
        if self.isEmpty() or item >= self._rear.data:
            LinkedQueue.add(self, item)
        else:
            probe = self._front
            trailer = None
            while item >= probe.data:
                trailer = probe
                probe = probe.next
            newNode = Node(item, probe)
            if trailer is None:
                self._front = newNode
            else:
                trailer.next = newNode
            self._size += 1
