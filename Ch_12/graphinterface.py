"""
File: graphinterface.py
"""

class GraphInterface(object):
    """Interface for all graphs."""

    def __init__(self, sourceCollection = None):
        self._edgeCount = 0
        self._vertices = {}
        AbstractCollection.__init__(self, sourceCollection)
        
    # Methods for clearing, marks, sizes, string rep

    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return True
    
    def __len__(self):
        """-Returns the number of items in self."""
        return 0

    def clear(self):
        """Clears the graph."""
        pass

    def clearEdgeMarks(self):
        """Clears all the edge marks."""
        pass
    
    def clearVertexMarks(self):
        """Clears all the vertex marks."""
        pass
    
    def sizeEdges(self):
        """Returns the number of edges."""
        return 0
    
    def sizeVertices(self):
        """Returns the number of vertices."""
        return 0
    
    def __str__(self):
        """Returns the string representation of the graph."""
        return ""

    def add(self, label):
        """For compatibility with other collections."""
        pass

    # Vertex related methods
    
    def addVertex(self, label):
        """Adds a vertex with the given label to the graph."""
        pass
        
    def containsVertex (self, label):
        return False
    
    def getVertex(self, label):
        return None
    
    def removeVertex(self,  label):
        """Returns True if the vertex was removed, or False otherwise."""
        return True
    
    # Methods related to edges

    def addEdge(self, fromLabel, toLabel, weight):
        """Connects the vertices with an edge with the given weight."""
        pass
    
    def containsEdge(self, fromLabel, toLabel):
        """Returns True if an edge connects the vertices,
        or False otherwise."""
        return False
    
    def getEdge(self, fromLabel, toLabel):
        """Returns the edge connecting the two vertices, or None if
        no edge exists."""
        return None
    
    def removeEdge(self, fromLabel, toLabel): 
        """Returns True if the edge was removed, or False otherwise."""
        return True
    
    # Iterators
    
    def __iter__(self):
        """Supports iteration over a view of self (the vertices)."""
        return None
        
    def edges(self):
        """Supports iteration over the edges in the graph."""
        return None
    
    def vertices(self):
        """Supports iteration over the vertices in the graph."""
        return None

    def incidentEdges(self, label):
        """Supports iteration over the incident edges of the
        given verrtex."""
        return None
    
    def neighboringVertices(self, label):
        """Supports iteration over the neighboring vertices of the
        given verrtex."""
        return None
    
