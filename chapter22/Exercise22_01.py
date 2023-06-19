# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Test whether a graph is connected) Write  a program that reads a graph from a
file and determines whether of vertices(n). The vertices are labeled
as 0, 1, ... n-1. Each subsequent line, with the format u v1 v2 ..., describes
edges (u, v1), (u, v2) and so on. Figure 22.19 gives the examples of two
files for their corresponding graphs.

File_algo1          point1 0            File
6                   point2 1            6
012                 point3 2            0123
103                 point4 3            103   points[0,1,2,3,4,5,6]
2034                point5 4            203
31245               point6 5            3012
4235                                    45
534                                     54


Your program should prompt the user to enter a URL for the file, should read
data from a file, create an instance g of Graph, invoke g.printEdges() to
display all edges, and invoke dfs() to obtain an instance tree of Tree. If
tree.getNumberOfVerticeFound() is the same as the number of vertices in
the graph, the graph is connected.

Output :
#Please enter URL: example.com.txt
The number of vertices is 6
0 (0): (0,1) (0,2)
1 (1): (1,0) (1,3)
2 (2): (2,0) (2,3) (2,4)
3 (3): (3,1) (3,2) (3,4) (3,5)
4 (4): (4,2) (4,3) (4,5)
5 (5): (5,3) (5,4)
The graph is connected
'''

from queue import Queue

class Graph:
    def __init__(self, vertices=[], edges=[]):
        # Initializes the Graph class with optional vertices and edges
        self.vertices = vertices
        self.neighbors = self.getAdjacencyLists(edges)

    def getAdjacencyLists(self, edges):
        # Returns a list of adjacency lists for each vertex
        neighbors = [[] for _ in range(len(self.vertices))]
        for u, *v_list in edges:
            for v in v_list:
                neighbors[u].append(v)
        return neighbors

    def getSize(self):
        # Returns the number of vertices in the graph
        return len(self.vertices)

    def getVertices(self):
        # Returns a list of all vertices in the graph
        return self.vertices

    def getVertex(self, index):
        # Returns the vertex at the given index
        return self.vertices[index]

    def getIndex(self, v):
        # Returns the index of the given vertex
        return self.vertices.index(v)

    def getNeighbors(self, index):
        # Returns a list of neighbors for the vertex at the given index
        return self.neighbors[index]

    def getDegree(self, v):
        # Returns the degree of the given vertex
        return len(self.neighbors[self.getIndex(v)])

    def printEdges(self):
        # Prints all edges in the graph
        for u, neighbors in enumerate(self.neighbors):
            print(f"{u} ({len(neighbors)}): ", end="")
            for v in neighbors:
                print(f"({u},{v}) ", end="")
            print()

    def clear(self):
        # Clears the graph by resetting vertices and neighbors
        self.vertices = []
        self.neighbors = []

    def addVertex(self, vertex):
        # Adds a vertex to the graph
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.neighbors.append([])

    def addEdge(self, u, v):
        # Adds an edge between the given vertices
        if u in self.vertices and v in self.vertices:
            self.neighbors[u].append(v)

    def dfs(self, v):
        # Performs a depth-first search starting from the given vertex
        searchOrders = []
        parent = len(self.vertices) * [-1]
        isVisited = len(self.vertices) * [False]
        self.dfsHelper(v, parent, searchOrders, isVisited)
        return Tree(v, parent, searchOrders, self.vertices)

    def dfsHelper(self, v, parent, searchOrders, isVisited):
        # Helper function for DFS traversal
        searchOrders.append(v)
        isVisited[v] = True
        for neighbor in self.neighbors[v]:
            if not isVisited[neighbor]:
                parent[neighbor] = v
                self.dfsHelper(neighbor, parent, searchOrders, isVisited)

    def bfs(self, v):
        # Performs a breadth-first search starting from the given vertex
        searchOrders = []
        parent = len(self.vertices) * [-1]
        isVisited = len(self.vertices) * [False]
        queue = Queue()
        queue.put(v)
        isVisited[v] = True
        while not queue.empty():
            u = queue.get()
            searchOrders.append(u)
            for neighbor in self.neighbors[u]:
                if not isVisited[neighbor]:
                    queue.put(neighbor)
                    parent[neighbor] = u
                    isVisited[neighbor] = True
        return Tree(v, parent, searchOrders, self.vertices)


class Tree:
    def __init__(self, root, parent, searchOrders, vertices):
        # Initializes the Tree class with root, parent, searchOrders, and vertices
        self.root = root
        self.parent = parent
        self.searchOrders = searchOrders
        self.vertices = vertices

    def getRoot(self):
        # Returns the root of the tree
        return self.root

    def getParent(self, index):
        # Returns the parent of the vertex at the given index
        return self.parent[index]

    def getSearchOrders(self):
        # Returns the search orders of the tree
        return self.searchOrders

    def getNumberOfVerticesFound(self):
        # Returns the number of vertices found in the tree
        return len(self.searchOrders)

    def getPath(self, index):
        # Returns the path from the root to the vertex at the given index
        path = []
        while index != -1:
            path.append(self.vertices[index])
            index = self.parent[index]
        return path

    def printPath(self, index):
        # Prints the path from the root to the vertex at the given index
        path = self.getPath(index)
        print(f"A path from {self.vertices[self.root]} to {self.vertices[index]}: ", end="")
        print(" ".join(map(str, path[::-1])))

    def printTree(self):
        # Prints the tree, showing the root and edges
        print(f"Root is: {self.vertices[self.root]}")
        print("Edges: ", end="")
        for i in range(len(self.parent)):
            if self.parent[i] != -1:
                print(f"({self.vertices[self.parent[i]]},{self.vertices[i]})", end=" ")
        print()


# Prompt the user to enter the file URL
fileUrl = input("Please enter the URL for the file: ")

# Read data from the file
with open(fileUrl, 'r') as file:
    vertices = list(map(int, file.readline().strip()))
    graph = Graph(vertices)
    for line in file:
        edge = list(map(int, line.strip().split()))
        u = edge[0]
        v_list = edge[1:]
        for v in v_list:
            graph.addEdge(u, v)

# Display all edges in the graph
print("The number of vertices is", graph.getSize())
graph.printEdges()

# Perform depth-first search (DFS) to obtain a tree instance
startVertex = 0  # Choose a starting vertex
tree = graph.dfs(startVertex)

# Check if the graph is connected
if tree.getNumberOfVerticesFound() == graph.getSize():
    print("The graph is connected")
else:
    print("The graph is not connected")

# Example usage of tree methods
print(tree.getNumberOfVerticesFound(), graph.getSize())
tree.printPath(2)
