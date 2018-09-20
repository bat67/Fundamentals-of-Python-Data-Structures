"""
File: shorttest.py
"""

from graph import LinkedDirectedGraph

g = LinkedDirectedGraph()

# Insert vertices
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")

# Insert weighted edges
g.addEdge("A", "B", 3)
g.addEdge("A", "C", 2)
g.addEdge("B", "D", 1)
g.addEdge("C", "D", 1)
g.addEdge("D", "E", 2)

print(g)

print("Neighboring vertices of A:")
for vertex in g.neighboringVertices("A"):
    print(vertex)

print("Incident edges of A:")
for edge in g.incidentEdges("A"):
    print(edge)

