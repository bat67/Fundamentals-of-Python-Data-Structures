"""
File: algorithms.py
Algorithms configured for profiling.

"""

from profiler import Profiler

def selectionSort(lyst, profiler):
    i = 0
    while i < len(lyst) - 1:         # Do n - 1 searches
        minIndex = i                 # for the largest
        j = i + 1                    
        while j < len(lyst):         # Start a search
            profiler.comparison()
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:            # Exchange if needed
            swap(lyst, minIndex, i, profiler)
        i += 1

def bubbleSort(lyst, profiler):
    n = len(lyst)
    while n > 1:                       # Do n - 1 bubbles
        i = 1                          # Start each bubble
        while i < n:
            profiler.comparison()
            if lyst[i] < lyst[i - 1]:  # Exchange if needed
                swap(lyst, i, i - 1, profiler)
            i += 1
        n -= 1

def bubbleSort2(lyst, profiler):
    n = len(lyst)
    while n > 1:
        swapped = False
        i = 1                          
        while i < n:
            if lyst[i] < lyst[i - 1]:  # Exchange if needed
                swap(lyst, i, i - 1, profiler)
                swapped = True
                if trace: print(lyst)
            i += 1
            profiler.comparison()
        if not swapped: return
        n -= 1

def insertionSort(lyst, profiler):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            profiler.comparison()
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                profiler.exchange()
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        profiler.exchange()
        i += 1

def swap(lyst, i, j, profiler):
    """Exchanges the elements at positions i and j."""
    profiler.exchange()
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
