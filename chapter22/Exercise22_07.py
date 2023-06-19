# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find a cycle) Add a new method in Graph to find cycle in the graph with the
following header:
    def getACycle(self):
The method returns a list af integers that contains all the vertices in a path from u
to v in this order. Using the BFS approach, you can obtain a shortest path u to
v. If there is no path u to v, the method returns None.'''

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

    def getACycle(self):
        queue = Queue()
        for start in range(len(self.adjacencyMatrix)):
            queue.put(start)
            self.vertices[start].visited = True

            while not queue.empty():
                current = queue.get()

                for neighbor in range(len(self.adjacencyMatrix[current])):
                    if self.adjacencyMatrix[current][neighbor] == 1 and self.vertices[neighbor].visited:
                        # Found a cycle
                        cycle = [neighbor, current]  # Append the last two vertices of the cycle
                        prevVertex = current

                        while prevVertex != start:
                            cycle.append(prevVertex)
                            prevVertex = self.getPrevVisitedVertex(prevVertex)

                        cycle.append(start)
                        cycle.reverse()  # Reverse the cycle to get the correct order
                        return cycle

                    if self.adjacencyMatrix[current][neighbor] == 1 and not self.vertices[neighbor].visited:
                        queue.put(neighbor)
                        self.vertices[neighbor].visited = True

        return None

    def getPrevVisitedVertex(self, vertex):
        for prevVertex in range(len(self.adjacencyMatrix[vertex])):
            if self.adjacencyMatrix[prevVertex][vertex] == 1 and self.vertices[prevVertex].visited:
                return prevVertex

        return None


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

# Find a cycle in the graph
print("\nCycle:")
cycle = graph.getACycle()
if cycle is not None:
    print("->".join([str(vertex) for vertex in cycle]))
else:
    print("No cycle found.")
