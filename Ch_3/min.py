"""
File: min.py
"""

def ourMin(lyst, trace = False):
    """Returns the position of the minimum item."""
    minpos = 0
    current = 1
    while current < len(lyst):
        if lyst[current] < lyst[minpos]:
            minpos = current
            if trace: print current, minpos
        current += 1
    return minpos
