# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Create a graph and delete vertices) Implement a Vertex class that holds a label.
Also, implement a Graph class, the constructor of which-takes an adjacency matrix and
a list of Vertex objects(vertices). The Graph should contain methods for deleting a
specified vertex index. The specified vertex should be removed from the list of vertices
and the adjacency matrix should be updated to reflect the removal of the vertex by shifting
columns and rows left and up.
    Write a test program to create a graph and delete a vertex. You could test your
implementation using the adjacency matrix outlined in question 22.2 and deleting the
first vertex'''

class Vertex:
    def __init__(self, label):
        self.label = label


class Graph:
    def __init__(self, adjacency_matrix, vertices):
        self.adjacency_matrix = adjacency_matrix
        self.vertices = vertices

    def deleteVertex(self, index):
        if index >= len(self.vertices) or index < 0:
            print("Invalid vertex index.")
            return

        # Remove the specified vertex from the list of vertices
        del self.vertices[index]

        # Update the adjacency matrix by shifting columns and rows left and up
        for row in self.adjacency_matrix:
            del row[index]

        del self.adjacency_matrix[index]

    def printGraph(self):
        for row in self.adjacency_matrix:
            print(row)


# Test program
adjMatrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

vertices = [
    Vertex("A"),
    Vertex("B"),
    Vertex("C"),
    Vertex("D"),
    Vertex("E")
]

graph = Graph(adjMatrix, vertices)

print("Before deleting vertex:")
graph.printGraph()

# Delete the first vertex (index 0)
graph.deleteVertex(0)

print("\nAfter deleting vertex:")
graph.printGraph()
