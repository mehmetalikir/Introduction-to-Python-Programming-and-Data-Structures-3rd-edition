# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Implement Dijkstra’s algorithm using an adjacency matrix) The text implements
Dijkstra’s algorithm using lists for adjacent edges. Implement the algorithm
using an adjacency matrix for weighted graphs.'''

import sys

def getShortestPath(graph, source):
    numVertices = len(graph)
    t = set()  # Set of vertices whose paths to source are known
    cost = [sys.maxsize] * numVertices  # Cost of the shortest path from source to each vertex
    parent = [None] * numVertices  # Parent vertex of each vertex in the shortest path tree

    cost[source] = 0

    while len(t) < numVertices:
        u = None
        minCost = sys.maxsize

        # Find the vertex with the smallest cost not in T
        for v in range(numVertices):
            if v not in t and cost[v] < minCost:
                u = v
                minCost = cost[v]

        t.add(u)

        # Update the cost and parent of each neighboring vertex of u
        for v in range(numVertices):
            if v not in t and graph[u][v] > 0 and cost[v] > cost[u] + graph[u][v]:
                cost[v] = cost[u] + graph[u][v]
                parent[v] = u

    return parent

# Example usage
graph = [
    [0, 4, 2, 0, 0],
    [4, 0, 1, 5, 0],
    [2, 1, 0, 8, 10],
    [0, 5, 8, 0, 2],
    [0, 0, 10, 2, 0]
]

source = 0
shortestPathTree = getShortestPath(graph, source)

print("Vertex\tParent")
print("--------------")
for v in range(len(shortestPathTree)):
    print(v, "\t\t", shortestPathTree[v])
