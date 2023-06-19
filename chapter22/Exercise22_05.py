# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Breadth-First Traversal) Implement the breadth-first traversal algorithm and
create a test program that invokes the algorithm, passing in the starting point for
the traversal. You should add a flag to the Vertex class which indicates whether a
vertex has been visited by the algorithm. For the following adjacency matrix, the
result would be A B E C F D G:
        [0, 1, 0, 0, 1, 0, 0],  # A
        [0, 0, 1, 0, 0, 0, 0],  # B
        [0, 0, 0, 1, 0, 0, 0],  # C
        [0, 0, 0, 0, 0, 0, 0],  # D
        [0, 0, 0, 0, 0, 0, 0],  # E
        [0, 0, 0, 0, 0, 0, 1],  # F
        [0, 0, 0, 0, 0, 0, 0],  # G
'''

from queue import Queue

class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False


class Graph:
    def __init__(self, adjacencyMatrix):
        self.adjacencyMatrix = adjacencyMatrix
        self.vertices = []
        for _ in range(len(adjacencyMatrix)):
            self.vertices.append(Vertex(None))

    def breadthFirstTraversal(self, start):
        if start >= len(self.adjacencyMatrix) or start < 0:
            print("Invalid starting point for traversal.")
            return

        queue = Queue()
        queue.put(start)
        self.vertices[start].visited = True

        while not queue.empty():
            current = queue.get()
            print(self.vertices[current].label, end=" ")

            for neighbor in range(len(self.adjacencyMatrix[current])):
                if self.adjacencyMatrix[current][neighbor] == 1 and not self.vertices[neighbor].visited:
                    queue.put(neighbor)
                    self.vertices[neighbor].visited = True


# Test program
adjacencyMatrix = [
    [0, 1, 0, 0, 1, 0, 0],  # A
    [0, 0, 1, 0, 0, 0, 0],  # B
    [0, 0, 0, 1, 0, 0, 0],  # C
    [0, 0, 0, 0, 0, 0, 0],  # D
    [0, 0, 0, 0, 0, 0, 0],  # E
    [0, 0, 0, 0, 0, 0, 1],  # F
    [0, 0, 0, 0, 0, 0, 0]   # G
]

graph = Graph(adjacencyMatrix)

# Perform breadth-first traversal starting from vertex A (index 0)
print("Breadth-First Traversal:")
graph.breadthFirstTraversal(0)

