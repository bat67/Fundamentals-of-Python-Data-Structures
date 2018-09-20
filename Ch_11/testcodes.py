"""
File: testcodes.py
"""

def keysToIndexes(keys, n, hash = lambda key: key):
    """Returns the array indexes corresponding to the
    hashed keys for an array of length n."""
    return list(map(lambda key: hash(key) % n, keys))

def stringHash(item):
    """Generates an integer key from a string."""
    if len(item) > 4 and \
       (item[0].islower() or item[0].isupper()):
        item = item[1:]           # Drop first letter
    sum = 0
    for ch in item:
        sum += ord(ch)
    if len(item) > 2:
        sum -= 2 * ord(item[-1])  # Subtract last ASCII
    return sum



