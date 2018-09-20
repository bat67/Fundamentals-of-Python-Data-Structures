"""
File: timing2.py
Prints the running times for problem sizes that double,
using a nested loop.
"""

import time

problemSize = 1000
print("%12s%10s" % ("Problem Size", "Seconds"))
for count in range(5):
    
    start = time.time()
    # The start of the algorithm
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            work += 1
            work -= 1
   # The end of the algorithm
    elapsed = time.time() - start
    
    print("%12d%10.3f" % (problemSize, elapsed))
    problemSize *= 2
