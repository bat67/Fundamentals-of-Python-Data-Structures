"""
File: profiler.py

Case study for Chapter 11.
"""

from hashtable import HashTable

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

class Profiler(object):
    "Represents a profiler for hash tables."""

    def __init__(self):
        self._table = None
        self._collisions = 0
        self._probeCount = 0

    def test(self, table, data):
        """Inserts item into the table
        Preconditions: There is at least one empty cell or
        one previously occupied cell.
        There is not a duplicate item."""
        self._table = table
        self._collisions = 0
        self._probeCount = 0
        self._result = "Load Factor  Item Inserted  Home Index  Actual Index   Probes\n"
        for item in data:
            loadFactor = table.loadFactor()
            table.insert(item)
            homeIndex = table.homeIndex()
            actualIndex = table.actualIndex()
            probes = table.probeCount()
            self._probeCount += probes
            if probes > 0:
                self._collisions += 1
            line = "%8.3f%14d%12d%12d%14d" % (loadFactor, item,
                                               homeIndex, actualIndex,
                                               probes)
            self._result += line + "\n"
        self._result += "Total collisions: " + str(self._collisions) + \
                        "\nTotal probes: " + str(self._probeCount) + \
                        "\nAverage probes per collision: " + \
                        str(self._probeCount / float(self._collisions))
                        

    def __str__(self):
        if self._table is None:
            return "No test has been run yet."
        else:
            return self._result

    # Methods collisions() and probeCount() are exercises.
        
def main():
    # Create a table with 8 cells, an identity hash function,
    # and linear probing.
    table = HashTable(8, lambda x: x)
    # The data are the numbers from 10 through 70, by 10s
    data = range(10, 71, 10)
    profiler = Profiler()
    profiler.test(table, data)
    print(profiler)

if __name__ == "__main__":
    main()



        



