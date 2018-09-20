"""
File: randlist.py

Defines a function to generate a list of
numbers in arbitrary order.
"""

import random

def makeRandomList(size):
    lyst = []
    for count in range(size):
        while True:
            number = random.randint(1, size)
            if not number in lyst:
                lyst.append(number)
                break
    return lyst
