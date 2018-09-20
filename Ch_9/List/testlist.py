"""
File: testlist.py

A tester program for list implementations.
"""

from arraylist import ArrayList
from linkedlist import LinkedList

def testList(ListType):
    """Expects a list type as an argument and runs some tests
    on objects of that type.""" 
    print("\nTESTING THE LIST TYPE " + str(ListType))
    lyst = ListType(["Ken", 60, 1973])
    print("Expect 3:     " + str(len(lyst)))
    print('Expect [Ken, 60, 1973]: ', end = "")
    print(lyst)
    print("Expect True:  " + str("Ken" in lyst))
    print("Expect False: " + str("Bill" in lyst))
    print("Expect 1:     " + str(lyst.index(60)))
    lyst.add("Sara")
    print('Expect [Ken, 60, 1973, Sara]: ', end = "")
    print(lyst)
    lyst.insert(2, "Sam")
    print('Expect [Ken, 60, Sam, 1973, Sara]: ', end = "")
    print(lyst)
    print('Expect Ken 60 Sam 1973 Sara: ', end = "")
    for i in range(len(lyst)):
         print(lyst[i], end = " ")
    lyst = ListType(range(ArrayList.DEFAULT_CAPACITY))
    print("\nExpect [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: ", end = "")
    print(lyst)
    print("Popping all, expect 9 8 7 6 5 4 3 2 1 0: ", end = "")
    while not lyst.isEmpty(): print(lyst.pop(), end = " ")
    print("\nRemoved all items: Expect []: ", end = "")
    print(lyst)
    lyst1 = ListType([3, 4])
    lyst2 = ListType([4, 5, 6])
    print("[3, 4] + [4, 5, 6] = ", end = "")
    print(lyst1 + lyst2)
    for i in range(len(lyst1)):
        lyst1[i] = 0
    print("Replace [3, 4] with [0, 0], expect [0, 0]: ", end = "")
    print(lyst1)

def testListIterator(ListType):
    """Expects a list type as an argument and runs some tests
    on a list iterator on that type."""
    print("\nTESTING A LIST ITERATOR FOR THE TYPE " + str(ListType) )
    print("Create a list with 1-9")
    lyst = ListType(range(1, 10))
    print("Length:", len(lyst))
    print("Items in list (first to last):", lyst)
    
    # Create and use a list iterator
    listIterator = lyst.listIterator()
    print("Forward traversal with list iterator: ", end="")
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
    listIterator.insert(10)
    print(lyst)
    print("Removing 2: ", end="")
    listIterator.first()
    for count in range(2): 
            listIterator.next()
    listIterator.remove()
    print(lyst)

    print("Replace all items with 0: ", end="")
    listIterator.first()
    while listIterator.hasNext():
            listIterator.next()
            listIterator.replace(0)
    print(lyst)

    print("Removing all items: Expect []: ", end = "")
    listIterator.first()
    while listIterator.hasNext():
            listIterator.next()
            listIterator.remove()
    print(lyst)
    print("Length:", len(lyst))
    
    

testList(ArrayList)
testListIterator(ArrayList)
testList(LinkedList)
#testListIterator(LinkedList)
    
