# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Traveling salesperson problem) The traveling salesperson problem (TSP) is
to find the shortest round-trip route that visits each city exactly once and then
returns to the starting city. The problem is equivalent to finding the shortest
Hamiltonian cycle in Programming Exercise 22.14. Add the following method
in the WeightedGraph class:
# Return the shortest cycle
# Return null if no such cycle exists
def getShortestHamiltonianCycle():'''

from Graph import Graph, Edge

class WeightedGraph(Graph):
    def __init__(self, vertices=[], edges=[], weights=[]):
        super().__init__(vertices, edges)
        self.weights = weights

    def getWeight(self, u, v):
        indexU = self.getIndex(u)
        indexV = self.getIndex(v)
        if indexU == -1 or indexV == -1:
            return float('inf')
        for edge in self.neighbors[indexU]:
            if edge.v == indexV:
                return self.weights[edge.u][edge.v]
        return float('inf')

    def getShortestHamiltonianCycle(self):
        # Initialize variables
        numVertices = self.getSize()
        shortestCycle = None

        # Recursive function to find the shortest Hamiltonian cycle
        def backtrack(vertex, pathLength, path):
            nonlocal shortestCycle

            if len(path) == numVertices:
                # Check if the last vertex has an edge to the starting vertex
                if self.hasEdge(vertex, path[0]):
                    path.append(path[0])
                    cycleLength = pathLength + self.getWeight(vertex, path[0])

                    # Update the shortest cycle
                    if shortestCycle is None or cycleLength < shortestCycle[0]:
                        shortestCycle = (cycleLength, path.copy())

                    path.pop()
                return

            for nextVertex in self.getNeighbors(vertex):
                if nextVertex not in path:
                    weight = self.getWeight(vertex, nextVertex)
                    path.append(nextVertex)
                    backtrack(nextVertex, pathLength + weight, path)
                    path.pop()

        # Start the backtracking from each vertex
        for startVertex in range(numVertices):
            path = [startVertex]
            backtrack(startVertex, 0, path)

        return shortestCycle[1] if shortestCycle is not None else None


# Create a weighted graph
graph = WeightedGraph()

# Add vertices
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addVertex("E")
graph.addVertex("F")

# Add edges
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("A", "D")
graph.addEdge("A", "E")
graph.addEdge("B", "C")
graph.addEdge("B", "D")
graph.addEdge("B", "E")
graph.addEdge("C", "D")
graph.addEdge("C", "E")
graph.addEdge("D", "E")
graph.addEdge("E", "F")
graph.addEdge("F", "A")

# Find the shortest Hamiltonian cycle
shortestCycle = graph.getShortestHamiltonianCycle()

# Print the cycle
if shortestCycle:
    print("Shortest Hamiltonian Cycle:", shortestCycle)
else:
    print("No Hamiltonian Cycle found in the graph.")
