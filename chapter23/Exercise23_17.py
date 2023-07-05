# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Alternative version of Dijkstra algorithm) An alternative version of the Dijkstra
algorithm can be described as follows:

Input: a weighted graph G = (V, E) with non-negative weights
Output: A shortest path tree from a source vertex s

1 while ShortestPathTree getShortestPath(s):
2   Let T be a set that contains the vertices whose
3       paths to s are known
4   Initially T contains source vertex s with cost[s] = 0
5   for each u in V – T
6       cost[u] = infinity
7
8   while size of T < n:
9       Find v in V – T with the smallest cost[u] + w(u, v) value
10          among all u in T
11      Add v to T and set cost[v] = cost[u] + w(u, v)
12      parent[v] = u

The algorithm uses cost[v] to store the cost of a shortest path from vertex v
to the source vertex s. cost[s] is 0. Initially assign infinity to cost[v] to
indicate that no path is found from v to s. Let V denote all vertices in the graph
and T denote the set of the vertices whose costs are known. Initially, the source
vertex s is in T. The algorithm repeatedly finds a vertex u in T and a vertex v
in V – T such that cost[u] + w(u, v) is the smallest, and moves v to T.
The shortest path algorithm given in the text coninously update the cost and
parent for a vertex in V – T. This algorithm initializes the cost to infinity for
each vertex and then changes the cost for a vertex only once when the vertex is
added into T. Implement this algorithm and use Listing 23.8, TestShortestPath.
py, to test your new algorithm.'''

from Graph import Graph
from WeightedGraph import WeightedGraph
from WeightedGraph import ShortestPathTree

def getShortestPath(graph, sourceVertex):
    # Create a ShortestPathTree instance with source vertex
    shortestPathTree = ShortestPathTree(sourceVertex, [], [], [], graph.vertices)

    # Create a set T to store vertices whose paths to s are know
    T = {sourceVertex}

    # Initialize cost and parent for each vertex
    cost = {v: float('inf') for v in graph.vertices}
    parent = {v: -1 for v in graph.vertices}

    # Set cost of source vertex to 0
    cost[sourceVertex] = 0

    while len(T) < graph.getSize():
        # Find the vertex v in V - T with the smallest cost[u] + w(u, v)
        minCost = float('inf')
        minVertex = None

        for u in T:
            for edge in graph.neighbors[u]:
                if edge.v not in T:
                    newCost = cost[u] + edge.weight
                    if newCost < minCost:
                        minCost = newCost
                        minVertex = edge.v

        # Add the vertex v to T and update its cost and parent
        T.add(minVertex)
        cost[minVertex] = minCost
        parent[minVertex] = u

    # Update the shortestPathTree with the final ost and parent values
    shortestPathTree.costs = [cost[v] for v in graph.vertices]
    shortestPathTree.parent = [parent[v] for v in graph.vertices]
    return shortestPathTree
# Test program
graph = WeightedGraph(vertices=["A", "B", "C", "D", "E", "f"],
                          edges=[
                              (0, 1, 2), (0, 3, 8),
                              (1, 0, 2), (1, 2, 7), (1, 3, 3),
                              (2, 1, 8), (2, 3, 4) ,(2, 4, 5), (2, 5, 6),
                              (3, 0, 7), (3, 1, 3), (3, 2, 4), (3, 4, 6),
                              (4, 2, 5), (4, 3, 6), (4, 5, 9),
                              (5, 2, 6), (5, 4, 9),
                          ])
sourceVertex = 0 # Index of the source vertex

shortestPathTree = getShortestPath(graph, sourceVertex)
shortestPathTree.printAllPaths()

