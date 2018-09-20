"""
File: testlistiterator.py

A tester program for list iterator implementation.
"""

from arraylist import ArrayList
from arraysortedlist import ArraySortedList

def test(listType):
    """Expects a list type as an argument and runs some tests
    on objects of that type.""" 
    print("Create a list with 1-9")
    lyst = listType(range(1, 10))
    print("Length:", len(lyst))
    print("Items (first to last):", lyst)
    
    # Create and use a list iterator
    listIterator = lyst.listIterator()
    print("Forward traversal: ", end="")
    listIterator.first()
    while listIterator.hasNext(): 
            print(listIterator.next(), end = " ")

    print("\nBackward traversal: ", end="")
    listIterator.last()
    while listIterator.hasPrevious(): 
            print(listIterator.previous(), end=" ")

    print("\nInserting 10 before 3: ", end="")
    listIterator.first()
    for count in range(3):
            listIterator.next()
#    listIterator.insert(10)
    print(lyst)
    print("Removing 2: ", end="")
    listIterator.first()
    for count in range(2): 
            listIterator.next()
    listIterator.remove()
    print(lyst)

    print("Removing all items")
    listIterator.first()
    while listIterator.hasNext():
            listIterator.next()
            listIterator.remove()
    print("Length:", len(lyst))
    
    

test(ArraySortedList)
    
