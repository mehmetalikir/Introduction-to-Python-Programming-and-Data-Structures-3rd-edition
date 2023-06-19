# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Topological sort) Expand the Programing Exercise 22.3 by adding a method
that carries out a topological sort to display the sequence of vertices in a directed
graph. For example, consider the following adjacency matrix:
        [0, 0, 0, 1, 1, 0],  # Agree Funding
        [0, 0, 0, 0, 0, 1],  # Install Software
        [1, 0, 0, 0, 0, 0],  # Planning Meeting
        [0, 1, 0, 0, 0, 0],  # Purchase Hardware
        [0, 1, 0, 0, 0, 0],  # Purchase Software
        [0, 0, 0, 0, 0, 0]  # Train Users
In this directed graph the sequence of nodes would be "Planning Meeting" ->
"Agree Funding" ->  "Purchase Hardware"/ "Purchase Software" (these two are
concurrent, so either could be listed first) -> "Train Users".
    The sorting algorith should work backwards by iteratively finding a vertex
with no successors, adding it to a stack, and removing the vertex from the graph
At the end of the operation, the stack will contain the sorted data. If the graph
has cycles, then an error message should be printed.'''

class Vertex:
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label


class Graph:
    def __init__(self, matrix, vertices):
        self.adjacencyMatrix = matrix
        self.vertices = vertices

    def __str__(self):
        details = ""
        for vertex in self.vertices:
            details += f"[{vertex}] "
        return details

    def deleteVertex(self, vertex):
        verticesLength = len(self.vertices)
        if vertex == verticesLength-1:
            self.deleteRow(vertex)
            self.deleteColumn(vertex)
            self.vertices.pop(vertex)
        else:
            for row in range(vertex, verticesLength-1):
                self.moveRow(row, verticesLength)

            for col in range(vertex, verticesLength - 1):
                self.moveColumn(col, verticesLength-1)

            self.deleteRow(verticesLength-1)
            self.deleteColumn(verticesLength-1)

            for v in range(vertex, verticesLength-1):
                self.vertices[v] = self.vertices[v+1]
            self.vertices.pop(verticesLength-1)


    def deleteRow(self, row):
        self.adjacencyMatrix.pop(row)

    def deleteColumn(self, row):
        for x in range(row):
            self.adjacencyMatrix[x].pop(row)

    def moveRow(self, row, length):
        for col in range(length):
            self.adjacencyMatrix[row][col] = self.adjacencyMatrix[row+1][col]

    def moveColumn(self, col, length):
        for row in range(length):
            self.adjacencyMatrix[row][col] = self.adjacencyMatrix[row][col+1]

    def noSuccessor(self):
        for row in range(0, len(self.vertices)):
            isEdge = False
            for col in range(0, len(self.vertices)):
                if self.adjacencyMatrix[row][col] > 0:
                    isEdge = True
                    break
            if not isEdge:
                return row
        return -1

    def topologicalSort(self):
        stack = []
        for count in range(len(self.vertices)):
            vertex = self.noSuccessor()
            if vertex == -1:
                print("Error - graph has cycles")
                return
            stack.append(self.vertices[vertex].label)
            self.deleteVertex(vertex)
        return stack



def main():
    tasks = ["Agree Funding", "Install Software", "Planning Meeting",
             "Purchase Hardware", "Purchase Software", "Train Users"]

    adjacencyMatrix = [
        [0, 0, 0, 1, 1, 0],  # Agree Funding
        [0, 0, 0, 0, 0, 1],  # Install Software
        [1, 0, 0, 0, 0, 0],  # Planning Meeting
        [0, 1, 0, 0, 0, 0],  # Purchase Hardware
        [0, 1, 0, 0, 0, 0],  # Purchase Software
        [0, 0, 0, 0, 0, 0]  # Train Users
    ]

    vertices = []
    for task in tasks:
        vertices.append(Vertex(task))

    graph = Graph(adjacencyMatrix, vertices)

    print(graph)
    for row in graph.adjacencyMatrix:
        print(row)

    stack = graph.topologicalSort()

    print("Sorting order: ")
    while stack:
        print(stack.pop() + ", ", end="")


main()
