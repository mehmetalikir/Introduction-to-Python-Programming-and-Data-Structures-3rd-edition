# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Minimum Spanning Tree) The minimum spanning tree contains just the minimum
number of connections necessary to connect the nodes in a graph. Extend
the breadth-first traversal algorithm form Programing Exercise 22.5 to include
an Edge class and record list of edges containing the minimum spanning tree for
a given graph. Consider the following adjacency matrix which contains additional
connections, making the graph moe complex:
        [0, 1, 0, 0, 1, 0, 0],  # A
        [0, 0, 1, 0, 0, 0, 0],  # B
        [0, 0, 0, 1, 0, 0, 0],  # C
        [0, 0, 0, 0, 0, 0, 0],  # D
        [0, 0, 0, 0, 0, 0, 0],  # E
        [0, 0, 0, 0, 0, 0, 1],  # F
        [0, 0, 0, 0, 0, 0, 0],  # G
A possible minimum spanning tree would be AB AC AD BE CF DG'''

class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False

    def __str__(self):
        return self.label

class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        return self.source.label + self.destination.label


class Graph:
    def __init__(self, matrix, vertices):
        self.adjacencyMatrix = matrix
        self.vertices = vertices

    def __str__(self):
        details = ""
        for v in self.vertices:
            details += f"[{str(v)}] "
        return details

    def getAdjUnvisited(self, vertex):
        for i in range(len(self.vertices)):
            if self.adjacencyMatrix[vertex][i] == 1 and self.vertices[i].visited == False:
                return i

        return -1

    def getMinimumSpanningTree(self, vertex):
        queue = []
        minimumSpanningTree = []
        self.vertices[vertex].visited = True
        #print(self.vertices[vertex])
        queue.append(vertex)
        while len(queue) > 0:
            vertex1 = queue.pop(0)
            vertex2 = self.getAdjUnvisited(vertex1)
            while not vertex2 == -1:
                self.vertices[vertex2].visited = True
                #print(self.vertices[vertex1], end="")
                #print(self.vertices[vertex2])
                minimumSpanningTree.append(Edge(self.vertices[vertex1], self.vertices[vertex2]))
                queue.append(vertex2)
                vertex2 = self.getAdjUnvisited(vertex1)

        return  minimumSpanningTree

        for i in range(len(self.vertices)-1):
            self.vertices[i].visited = False




def main():
    tasks = ["A", "B", "C", "D", "E", "F", "G"]

    adjacencyMatrix = [
        [0, 1, 1, 1, 0, 0, 0], #A
        [0, 0, 1, 1, 1, 0, 0], #B
        [0, 0, 0, 1, 0, 1, 0], #C
        [0, 0, 0, 0, 1, 1, 1], #D
        [0, 0, 0, 0, 0, 1, 1], #E
        [0, 0, 0, 0, 0, 0, 1], #F
        [0, 0, 0, 0, 0, 0, 0] #G
    ]

    vertices = []
    for t in tasks:
        vertices.append(Vertex(t))

    graph = Graph(adjacencyMatrix, vertices)

    print(graph)
    for r in graph.adjacencyMatrix:
        print(r)


    mst = graph.getMinimumSpanningTree(0)
    for e in mst:
        print(e)

main()
