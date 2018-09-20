"""
File: testpriorityqueue.py
Author: Ken Lambert
A tester program for priority queue implementations.
"""

from linkedpriorityqueue import LinkedPriorityQueue
from comparable import Comparable
import random

def test(queueType):
    # Test any implementation with same code
    print("VERIFY THAT IT BEHAVES LIKE A REGULAR QUEUE.")
    q = queueType()
    print("Length:", len(q))
    print("Empty:", q.isEmpty())
    print("Add 1-10")
    for i in range(10):
        q.add(i + 1)
    print("Peeking:", q.peek())
    print("Items (front to rear):",  q)
    print("Length:", len(q))
    print("Empty:", q.isEmpty())
    theClone = queueType(q)
    print("Items in clone (front to rear):",  theClone)
    theClone.clear()
    print("Length of clone after clear:",  len(theClone))
    print("Pop 3 items:", end = " ")
    for count in range(3): print(q.pop(), end = " ")
    print("\nQueue: ", q)
    print("Adding 11 and 12:")
    for item in range(11, 13): q.add(item)
    print("Queue: ", q)    
    print("Popping items (front to rear): ", end="")
    while not q.isEmpty(): print(q.pop(), end=" ")
    print("\nLength:", len(q))
    print("Empty:", q.isEmpty())
    print("Create with 11 items:")
    q = queueType(range(1, 12))
    print("Items (front to rear):",  q)

    print("\nVERIFY THAT IT BEHAVES LIKE A PRIORITY QUEUE.")
    lyst = list(range(1, 20, 2))
    random.shuffle(lyst)
    print("The items added: ", lyst)
    q = LinkedPriorityQueue(lyst)
    print("The queue: ", q)
    q.add(16)
    q.add(17)
    print("Adding 16 and 17: ", q)
    print("Add some random strings with random priorities attached:")
    q.clear()
    for s in "VERIFY THAT":
        c = Comparable(s, random.randint(1, 3))
        print((c.getData(), c.getPriority()))
        q.add(c)
    print("The queue: ", q)
        
    
    

test(LinkedPriorityQueue)
