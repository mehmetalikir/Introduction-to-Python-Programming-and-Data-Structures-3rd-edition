# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Get bipartite sets) Add a new method Graph to retun two bipartite sets if the
graph is bipartite:
    def getBipartite(self):
The method returns a list that contains two sublist, each of which contains a set
of vertices. If the graph is not bipartite, the method returns None'''

from queue import Queue

class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.color = None


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

    def isBipartite(self):
        for start in range(len(self.adjacencyMatrix)):
            if not self.vertices[start].visited:
                queue = Queue()
                queue.put(start)
                self.vertices[start].visited = True
                self.vertices[start].color = "Red"

                while not queue.empty():
                    current = queue.get()

                    for neighbor in range(len(self.adjacencyMatrix[current])):
                        if self.adjacencyMatrix[current][neighbor] == 1:
                            if not self.vertices[neighbor].visited:
                                queue.put(neighbor)
                                self.vertices[neighbor].visited = True
                                self.vertices[neighbor].color = "Blue" if self.vertices[current].color == "Red" else "Red"
                            elif self.vertices[neighbor].color == self.vertices[current].color:
                                return False

        return True

    def getBipartite(self):
        if not self.isBipartite():
            return None

        bipartite_sets = [[], []]
        for vertex in self.vertices:
            if vertex.color == "Red":
                bipartite_sets[0].append(vertex.label)
            elif vertex.color == "Blue":
                bipartite_sets[1].append(vertex.label)

        return bipartite_sets


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

# Check if the graph is bipartite
print("\nIs Bipartite?")
if graph.isBipartite():
    print("Yes")
else:
    print("No")

# Get the bipartite sets
print("Bipartite Sets:")
bipartite_sets = graph.getBipartite()
if bipartite_sets is not None:
    for i, subset in enumerate(bipartite_sets):
        print("Set {}: {}".format(i + 1, subset))
else:
    print("The graph is not bipartite.")
