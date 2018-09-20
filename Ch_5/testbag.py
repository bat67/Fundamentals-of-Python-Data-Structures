"""
File: testbag.py
Author: Ken Lambert
A tester program for bag implementations.
"""

from arraybag import ArrayBag
from linkedbag import LinkedBag

def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973]
    print("The list of items added is:", lyst)
    b1 = bagType(lyst)
    print("Expect 3:", len(b1))
    print("Expect the bag's string:", b1)
    print("Expect True:", 2013 in b1)
    print("Expect False:", 2012 in b1)
    print("Expect the items on separate lines:")
    for item in b1:
        print(item)
    b1.clear()
    print("Expect {}:", b1)
    b1.add(25)
    b1.remove(25)
    print("Expect {}:", b1)
    b1 = bagType(lyst)
    b2 = bagType(b1)
    print("Expect True:", b1 == b2)
    print("Expect False:", b1 is b2)
    print("Expect two of each item:", b1 + b2)
    for item in lyst:
        b1.remove(item)
    print("Expect {}:", b1)
    print("Expect crash with KeyError:")
    b2.remove(99)

#test(ArrayBag)
test(LinkedBag)
