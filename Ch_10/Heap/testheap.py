"""
File: testheap.py

A tester program for array heaps.
"""

from arrayheap import ArrayHeap

def main():
    heap = ArrayHeap()
    print "Adding D B A C F E G"
    heap.add("D")
    heap.add("B")
    heap.add("A")
    heap.add("C")
    heap.add("F")
    heap.add("E")
    heap.add("G")

    print "\nPeek:", heap.peek()

    print "\nString:\n" + str(heap)

    print "Iterator: "
    iterator = iter(heap)
    while True:
        try:
            print iterator.next(),
        except Exception, e:
            print e
            break
    
    # Use a for loop instead
    print "\nfor loop: "
    for item in heap:
        print item,

    print "\n\nRemovals: "
    while not heap.isEmpty(): print heap.pop(),

if __name__ == "__main__":
    main()




