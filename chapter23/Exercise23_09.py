# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find a minimum spanning tree) Write a program that reads a connected graph of
European capitals from a file and displays its minimum spanning tree. Each line in the file
describes an edge in the form of capital1, capital2 and weight, where capital1 and capital2 are
capitals and weight is the distance between them. Each triplet in this form describes an edge and
its weight. Note that we assume the graph is undirected, i.e., the graph has an edge(u,v), it also
has an edge(v,u). Only one edge is represented in the file. When you construct a graph, both edges
need to be added. Your program should read data from the file called Capitals.txt, create an
instance g of WeightGraph, invoke g.printWeightedEdges() to display all edges, invoke
getMinimumSpanningTree() to obtain an instance tree of MST, invoke tree.printTree() to
display the tree. The ile is in the following format:
Amsterdam, Athens, 2873
Amsterdam, Berlin, 667
Amsterdam, Brussels, 212
Amsterdam, Bucharest, 2243
Amsterdam, Budapest, 1411
Amsterdam, Dublin, 934
Amsterdam, Lisbon, 2235
Amsterdam, London, 544
Amsterdam, Madrid, 1775
Amsterdam, Paris, 510
Amsterdam, Rome, 1655
Amsterdam, Sofia, 2170
Athens, Amsterdam, 2873
Athens, Berlin, 2332
Athens, Brussels, 2810
...

Print:
The number of capitals is 13
0 (Amsterdam): (Amsterdam, Athens, 2873.0) (Amsterdam, Berlin, 667.0) (Amsterdam, Brussels, 212.0) (...'''

import heapq

class WeightedEdge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


class WeightedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacencyList = [[] for _ in range(vertices)]
        self.vertexNames = {}
        self.parent = [None] * vertices  # Parent attribute for minimum spanning tree

    def addEdge(self, edge):
        u, v, weight = edge.u, edge.v, edge.weight
        self.adjacencyList[u].append((v, weight))
        self.adjacencyList[v].append((u, weight))

    def printWeightedEdges(self):
        for u in range(self.vertices):
            for v, weight in self.adjacencyList[u]:
                print(f"{self.getVertexName(u)} - {self.getVertexName(v)}: {weight}")

    def getVertexName(self, vertex):
        if vertex in self.vertexNames:
            return self.vertexNames[vertex]
        else:
            return str(vertex)

    def getMinimumSpanningTree(self):
        visited = [False] * self.vertices
        mst = WeightedGraph(self.vertices)
        minHeap = []
        startingVertex = 0  # Start from the vertex 0

        visited[startingVertex] = True

        for v, weight in self.adjacencyList[startingVertex]:
            minHeap.append((weight, startingVertex, v))

        heapq.heapify(minHeap)

        while minHeap:
            w, u, v = heapq.heappop(minHeap)

            if visited[v]:
                continue

            visited[v] = True
            mst.addEdge(WeightedEdge(u, v, w))
            mst.parent[v] = u  # Update the parent attribute for the minimum spanning tree

            for nextV, nextW in self.adjacencyList[v]:
                if not visited[nextV]:
                    heapq.heappush(minHeap, (nextW, v, nextV))

        return mst


class WeightedTree:
    def __init__(self, rootVertex, parent):
        self.rootVertex = rootVertex
        self.parent = parent

    def printTree(self, graph):
        for vertex in range(len(self.parent)):
            if vertex != self.rootVertex and self.parent[vertex] is not None:
                print(f"{graph.getVertexName(vertex)} - {graph.getVertexName(self.parent[vertex])}")

    def getVertexName(self, vertex):
        if vertex in self.vertexNames:
            return self.vertexNames[vertex]
        else:
            return str(vertex)


# Read the data from the file
with open("Capitals.txt", "r") as file:
    lines = file.readlines()

# Construct the weighted graph
capitals = []
for line in lines:
    capital1, capital2, weight = line.strip().split(", ")
    capitals.append(capital1)
    capitals.append(capital2)

capitalIndices = {capital: index for index, capital in enumerate(set(capitals))}
numCapitals = len(capitalIndices)

graph = WeightedGraph(numCapitals)

for line in lines:
    capital1, capital2, weight = line.strip().split(", ")
    u = capitalIndices[capital1]
    v = capitalIndices[capital2]
    weight = float(weight)
    graph.addEdge(WeightedEdge(u, v, weight))
    graph.vertexNames[u] = capital1
    graph.vertexNames[v] = capital2

# Display the number of capitals
print(f"The number of capitals is {numCapitals}")

# Display all edges in the graph
graph.printWeightedEdges()

# Get the minimum spanning tree
mst = graph.getMinimumSpanningTree()

# Create a WeightedTree object from the minimum spanning tree graph
mstTree = WeightedTree(0, mst.parent)

# Display the minimum spanning tree
mstTree.printTree(graph)
