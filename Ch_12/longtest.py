"""
File: testundirected.py
"""
from graph import LinkedDirectedGraph

lyst = ["a", "b", "c", "d"]
g = LinkedDirectedGraph(lyst)
print("Expect 4 : " + str(g.sizeVertices()))
print("Expect 4 vertices a b c d and no edges: " + str(g))
      
# Mark vertices, count marks, clear marks, count marks
for vertex in g.vertices():
    vertex.setMark()
count = 0
for vertex in g.vertices():
    if vertex.isMarked():
        count += 1
print("Expect 4: " + str(count))
g.clearVertexMarks()
count = 0
for vertex in g.vertices():
    if vertex.isMarked():
        count += 1
print("Expect 0: " + str(count))
      
# Insert some edges
g.addEdge("a", "b", 1)
g.addEdge("c", "d", 2)
      
# Mark edges, count marks, clear marks, count marks
for edge in g.edges():
    edge.setMark();
count = 0;
for edge in g.edges():
    if edge.isMarked():
        count += 1
print("Expect 2: " + str(count))
g.clearEdgeMarks()
count = 0;
for edge in g.edges():
    if edge.isMarked():
        count += 1
print("Expect 0: " + str(count))
      
# Clear graph
g.clear()
        
# Insert vertices
g.addVertex("a")
g.addVertex("b")
g.addVertex("c")
g.addVertex("d")
g.addVertex("e")
g.addVertex("f")
g.addVertex("g")
g.addVertex("h")
g.addVertex("i")
g.addVertex("j")
      
# Test some vertex methods
result = ""
for vertex in g.vertices():
    result += str(vertex) + " "    
    print("Expect 10        :", g.sizeVertices())
    print("Expect a thru j  :", result)
    print("Expect True False :", g.containsVertex("a"), end = " ")
    print(g.containsVertex("x"))
print("Expect a b True False :", g.getVertex("a"), end = " ")
print(g.getVertex("b"), " ", g.removeVertex("j"))
print(g.containsVertex("j"))

vertex = g.getVertex("a")
vertex.setLabel("aaa", g)
print("Expect vertices aaa thru j :", g)
vertex.setLabel("a", g)

# Test some edge methods
print("Expect False False:", g.containsEdge("a", "b"),
      g.containsEdge("a", "a"))
g.addEdge("a","b", 1)
print("Expect True False False :", g.containsEdge("a", "b"),
      g.containsEdge("b", "a"), g.containsEdge("a", "a"))
g.addEdge("a","c", 2)
g.addEdge("e","c", 4)
g.addEdge("e","d", 5)
g.addEdge("e","f", 6)
g.addEdge("d","a", 7)
      
print("Expect True False True :", g.removeEdge("a","c"),
      g.containsEdge("a","c"), g.containsEdge ("d","a"))

edge = g.getEdge("e", "d")
edge.setWeight(55)
print("Expect 55 :", edge.getWeight())
edge.setWeight(5)

# Test incidentEdges
result = ""
for edge in g.getVertex("a").incidentEdges():
    result += str(edge) + " "  
print("Expect edges ab1 ad7 :", result)

# Test neighboringVertices 
result = ""
for vertex in g.neighboringVertices("a"):
    result += str(vertex) + " "    
print("Expect vertices bd :" + result)

# Test size methods and str for graph
print("Expect 9 and 5:", g.sizeVertices(), g.sizeEdges())
print("Expect 9 vertices and 5 edges : \n", g)
g.removeVertex("a")
print("Expect 8 and 3:", g.sizeVertices(), g.sizeEdges())
print("Expect vertices b thru i and  3 edges \n", g)



