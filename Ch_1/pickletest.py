"""
Author: Ken Lambert
Demonstrates the use of pickle to save and load objects with files.
"""

import pickle

lyst = [60, "A string object", 1977]
fileObj = open("items.dat", "wb")
for item in lyst:
    pickle.dump(item, fileObj)
fileObj.close()

lyst = list()
fileObj = open("items.dat", "rb")
while True:
    try:
        item = pickle.load(fileObj)
        lyst.append(item)
    except EOFError:
        fileObj.close()
        break
print(lyst)
