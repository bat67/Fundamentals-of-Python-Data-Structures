"""
File: testsortedlist.py
Author: Ken Lambert
A tester program for sorted list implementations.
"""

from arraysortedlist import ArraySortedList

def test(listType):
    """Expects a list type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973]
    print("The list of items added is:", lyst)
    L1 = listType(lyst)
    print("Expect 3:", len(L1))
    print("Expect the list's string:", L1)
    print("Expect True:", 2013 in L1)
    print("Expect False:", 2012 in L1)
    print("Expect the items on separate lines:")
    for item in L1:
        print(item)
    L1.clear()
    print("Expect []:", L1)
    L1.add(25)
    L1.remove(25)
    print("Expect []:", L1)
    L1 = listType(lyst)
    L2 = listType(L1)
    print("Expect True:", L1 == L2)
    print("Expect False:", L1 is L2)
    print("Expect two of each item:", L1 + L2)
    for item in lyst:
        L1.remove(item)
    print("Expect []:", L1)
    print("Expect crash with ValueError:")
    L2.remove(99)

test(ArraySortedList)
