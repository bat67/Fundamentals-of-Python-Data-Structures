"""
File: arrayheap.py

Defines the class ArrayHeap
"""

from abstractcollection import AbstractCollection

class ArrayHeap(AbstractCollection):

    def __init__(self, sourceCollection = None):
        self._heap = list()
        AbstractCollection.__init__(self, sourceCollection)

    def peek(self):
        if self.isEmpty():
            raise Exception("Heap is empty")
        return self._heap[0]

    def add(self, item):
        self._size += 1
        self._heap.append(item)
        curPos = len(self._heap) - 1
        while curPos > 0:
            parent = (curPos - 1) // 2
            parentItem = self._heap[parent]
            if parentItem <= item:
                break
            else:
                self._heap[curPos] = self._heap[parent]
                self._heap[parent] = item
                curPos = parent

    def pop(self):
        if self.isEmpty():
            raise Exception("Heap is empty")
        self._size -= 1
        topItem = self._heap[0]
        bottomItem = self._heap.pop(len(self._heap) - 1)
        if len(self._heap) == 0:
            return bottomItem
           
        self._heap[0] = bottomItem
        lastIndex = len(self._heap) - 1
        curPos = 0
        while True:
            leftChild = 2 * curPos + 1 
            rightChild = 2 * curPos + 2
            if leftChild > lastIndex:
                break
            if rightChild > lastIndex:
                maxChild = leftChild;
            else:
                leftItem  = self._heap[leftChild]
                rightItem = self._heap[rightChild]
                if leftItem < rightItem:
                    maxChild = leftChild
                else:
                    maxChild = rightChild
            maxItem = self._heap[maxChild]
            if bottomItem <= maxItem:
                break
            else:
                self._heap[curPos] = self._heap[maxChild]
                self._heap[maxChild] = bottomItem
                curPos = maxChild
        return topItem

    def __iter__(self):
        tempList = list(self._heap)
        resultList = []
        while not self.isEmpty():
            resultList.append(self.pop())
        self._heap = tempList
        self._size = len(self._heap)
        return iter(resultList)
      
    def __str__(self):
        def strHelper(position, level):
            result = ""
            if position < len(self):
                result += strHelper(2 * position + 2, level + 1)
                result += "|" * level
                result += str(self._heap[position]) + "\n"
                result += strHelper(2 * position + 1, level + 1)
            return result
        return strHelper(0, 0)

def main():
    heap = ArrayHeap()
    print("Adding D B A C F E G")
    heap.add("D")
    heap.add("B")
    heap.add("A")
    heap.add("C")
    heap.add("F")
    heap.add("E")
    heap.add("G")

    print("\nPeek:", heap.peek())

    print("\nString:\n" + str(heap))

    print("\nfor loop: ")
    for item in heap:
        print(item, end=" ")

    print("\n\nRemovals: ")
    while not heap.isEmpty(): print(heap.pop(), end=" ")

    heap = ArrayHeap(range(1, 8))
    print("\n\nHeap with 1..7:")
    print(heap)
    print("\nfor loop: ")
    for item in heap:
        print(item, end=" ")

if __name__ == "__main__":
    main()




