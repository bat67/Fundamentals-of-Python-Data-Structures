"""
File: testqueue.py
Author: Ken Lambert
A tester program for queue implementations.
"""


from arrayqueue import ArrayQueue
from linkedqueue import LinkedQueue

def test(queueType):
    # Test any implementation with same code
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
    q = queueType(range(1, 11))
    print("Items (front to rear):",  q)
    print("Popping two items: ", q.pop(), q.pop(), q)
    print("Adding five items: ", end = "")
    for count in range(5):
        q.add(count)
    print(q)

#test(ArrayQueue)
#test(LinkedQueue)
