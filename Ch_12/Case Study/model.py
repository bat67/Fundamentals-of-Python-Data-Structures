"""
File: model.py
The model for testing graph processing algorithms.
"""

from graph import LinkedDirectedGraph

class GraphDemoModel(object):
    """The model class for the application."""

    def __init__(self):
        self._graph = None
        self._startLabel = None

    def createGraph(self, rep, startLabel):
        """Creates a graph from rep and startLabel.
        Returns a message if the graph was successfully
        created or an error message otherwise."""
        self._graph = LinkedDirectedGraph()
        self._startLabel = startLabel
        edgeList = rep.split()
        for edge in edgeList:
            if not '>' in edge:
                # A disconnected vertex
                if not self._graph.containsVertex(edge):
                    self._graph.addVertex(edge)
                else:
                    self._graph = None
                    return "Duplicate vertex"
            else:
                # Two vertices and an edge
                bracketPos = edge.find('>')
                colonPos = edge.find(':')
                if bracketPos == -1 or colonPos == -1 or \
                   bracketPos > colonPos:
                    self._graph = None
                    return "Problem with > or :"
                fromLabel = edge[:bracketPos]
                toLabel = edge[bracketPos + 1:colonPos]
                weight = edge[colonPos + 1:]
                if weight.isdigit():
                    weight = int(weight)
                if not self._graph.containsVertex(fromLabel):
                    self._graph.addVertex(fromLabel)
                if not self._graph.containsVertex(toLabel):
                    self._graph.addVertex(toLabel)
                if self._graph.containsEdge(fromLabel, toLabel):
                    self._graph = None
                    return "Duplicate edge"
                self._graph.addEdge(fromLabel, toLabel, weight)
        vertex = self._graph.getVertex(startLabel)
        if vertex is None:
            self._graph = None
            return "Start label not in graph"
        else:
            vertex.setMark()
            return "Graph created successfully"

    def getGraph(self):
        """Returns the string rep of the graph or None if
        it is unavailable"""
        if not self._graph:
            return None
        else:
            return str(self._graph)

    def getStartLabel(self):
        return self._startLabel

    def run(self, algorithm):
        """Runs the given algorithm on the graph and
        returns its result, or None if the graph is
        unavailable."""
        if self._graph is None:
            return None
        else:
            return algorithm(self._graph, self._startLabel)
   
