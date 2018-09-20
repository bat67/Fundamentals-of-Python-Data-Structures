"""
File: view.py
The view for testing graph processing algorithms.
"""

from model import GraphDemoModel

from algorithms import shortestPaths, spanTree, topoSort

class GraphDemoView(object):
    """The view class for the application."""

    def __init__(self):
        self._model = GraphDemoModel()

    def run(self):
        """Menu-driven command loop for the app."""
        menu = "Main menu\n" + \
               "  1  Input a graph from the keyboard\n" + \
               "  2  Input a graph from a file\n" + \
               "  3  View the current graph\n" \
               "  4  Single source shortest paths\n" \
               "  5  Minimum spanning tree\n" \
               "  6  Topological sort\n" \
               "  7  Exit the program\n"
        while True:
            command = self._getCommand(7, menu)
            if   command == 1: self._getFromKeyboard()
            elif command == 2: self._getFromFile()
            elif command == 3:
                print(self._model.getGraph())
            elif command == 4:
                print("Paths:\n", self._model.run(shortestPaths))
            elif command == 5:
                print("Tree:", \
                      " ".join(map(str, self._model.run(spanTree))))
            elif command == 6:
                print("Sort:", \
                      " ".join(map(str, self._model.run(topoSort))))
            else: break

    def _getCommand(self, high, menu):
        """Obtains and returns a command number."""
        prompt = "Enter a number [1-" + str(high) + "]: "
        commandRange = list(map(str, range(1, high + 1)))
        error = "Error, number must be 1 to " + str(high)
        while True:
            print(menu)
            command = input(prompt)
            if command in commandRange:
                return int(command)
            else:
                print(error)

    def _getFromKeyboard(self):
        """Inputs a description of the graph from the keyboard
        and creates the graph."""
        rep = ""
        while True:
            edge = input("Enter an edge or return to quit: ")
            if edge == "": break
            rep += edge + " "
        startLabel = input("Enter the start label: ")
        print(self._model.createGraph(rep, startLabel))

    def _getFromFile(self):
        """Inputs a description of the graph from a file
        and creates the graph."""
        # Exercise
            
# Start up the application

GraphDemoView().run()

            
