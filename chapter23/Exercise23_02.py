# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Implement Prim’s algorithm using an adjacency matrix) The text implements
Prim’s algorithm using lists for adjacent edges. Implement the algorithm using
an adjacency matrix for weighted graphs.'''

import sys  # Import sys


class PrimAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
        self.key = [sys.maxsize] * self.V
        self.parent = [None] * self.V
        self.mstSet = [False] * self.V

    def getMinimumKey(self):
        minKey = sys.maxsize
        minIndex = None

        # Find the vertex with the minimum key value among the vertices not yet included in MST
        for v in range(self.V):
            if self.key[v] < minKey and not self.mstSet[v]:
                minKey = self.key[v]
                minIndex = v

        return minIndex

    def printMST(self):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(self.parent[i], "-", i, "\t", self.graph[i][self.parent[i]])

    def primMST(self):
        self.key[0] = 0  # Start with the first vertex as the root
        self.parent[0] = -1  # Set the parent of the root as -1

        # Construct the MST by repeatedly adding the vertex with the minimum key value
        for _ in range(self.V):
            u = self.getMinimumKey()
            self.mstSet[u] = True  # Include the selected vertex in the MST

            # Update key values and parent array for the adjacent vertices of the selected vertex
            for v in range(self.V):
                if self.graph[u][v] > 0 and not self.mstSet[v] and self.graph[u][v] < self.key[v]:
                    self.key[v] = self.graph[u][v]
                    self.parent[v] = u

        self.printMST()


# Example usage
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim = PrimAlgorithm(graph)
prim.primMST()
