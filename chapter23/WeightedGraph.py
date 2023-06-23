from Graph import Graph
from Graph import Tree
from WeightedEdge import WeightedEdge

INFINITY = float('inf')  # 1e+308 Infinity value


class WeightedGraph(Graph):
    def __init__(self, vertices=[], edges=[]):
        super().__init__(vertices, edges)

    # Override this method in the Graph class
    def getAdjacnecyLists(self, edges):
        self.neighbors = []
        for i in range(len(self.vertices)):
            self.neighbors.append([])  # Each element is another list

        for edge in edges:
            u = edge[0]  # Access the first element of the edge list
            v = edge[1]  # Access the second element of the edge list
            w = edge[2]  # Access the third element of the edge list
            # Insert an edge (u, v, w)
            self.neighbors[u].append(WeightedEdge(u, v, w))

        # for edge in edges:
        #     u = edge.u
        #     v = edge.v
        #     w = edge.weight
        #     # Insert an edge (u, v, w)
        #     self.neighbors[u].append(WeightedEdge(u, v, w))

        return self.neighbors

    # Display edges with weights
    def printWeightedEdges(self):
        for i in range(len(self.neighbors)):
            print(str(self.getVertex(i))
                  + " (" + str(i), end="): ")
            for edge in self.neighbors[i]:
                print("(" + str(edge.u) + ", " + str(edge.v)
                      + ", " + str(edge.weight), end=") ")
            print()

    # Return the weight between two vertices
    def getWeight(self, u, v):
        for edge in self.neighbors[self.getIndex(u)]:
            if edge.v == self.getIndex(v):
                return edge.weight

    # Override the addEdge method to add a weighted edge
    def addEdge(self, u, v, w):
        if u in self.vertices and v in self.vertices:
            indexU = self.getIndex(u)
            indexV = self.getIndex(v)
            # Add an edge (u, v, w) to the graph
            self.neighbors[indexU].append(
                WeightedEdge(indexU, indexV, w))

    # Get a minimum spanning tree rooted at the specified vertex
    def getMinimumSpanningTree(self, startingVertex=0):
        # cost[v] stores the cost by adding v to the tree
        cost = self.getSize() * [INFINITY]
        cost[startingVertex] = 0  # Cost of source is 0

        parent = self.getSize() * [-1]  # Parent of a vertex
        totalWeight = 0;  # Total weight of the tree thus far

        T = []

        # Expand T
        while len(T) < self.getSize():
            # Find smallest cost v in V - T
            u = -1  # Vertex to be determined
            currentMinCost = INFINITY
            for i in range(self.getSize()):
                if i not in T and cost[i] < currentMinCost:
                    currentMinCost = cost[i]
                    u = i

            if u == -1:
                break
            else:
                T.append(u)  # Add a new vertex to T
            totalWeight += cost[u]  # Add cost[u] to the tree

            # Adjust cost[v] for v that is adjacent to u and v in V - T
            for e in self.neighbors[u]:
                if e.v not in T and cost[e.v] > e.weight:
                    cost[e.v] = e.weight
                    parent[e.v] = u

        return MST(startingVertex, parent, T, totalWeight,
                   self.vertices)

    # Find single source shortest paths
    def getShortestPath(self, sourceVertex):
        # cost[v] stores the cost of the path from v to the source
        cost = self.getSize() * [INFINITY]  # Initial cost to infinity
        cost[sourceVertex] = 0  # Cost of source is 0

        # parent[v] stores the previous vertex of v in the path
        parent = self.getSize() * [-1]

        # T stores the vertices whose path found so far
        T = []

        # Expand T
        while len(T) < self.getSize():
            # Find smallest cost v in V - T
            u = -1  # Vertex to be determined
            currentMinCost = INFINITY
            for i in range(self.getSize()):
                if i not in T and cost[i] < currentMinCost:
                    currentMinCost = cost[i]
                    u = i

            if u == -1:
                break
            else:
                T.append(u)  # Add a new vertex to T

            # Adjust cost[v] for v that is adjacent to u and v in V - T
            for e in self.neighbors[u]:
                if e.v not in T and cost[e.v] > cost[u] + e.weight:
                    cost[e.v] = cost[u] + e.weight
                    parent[e.v] = u

                    # Create a ShortestPathTree
        return ShortestPathTree(sourceVertex, parent, T, cost,
                                self.vertices)


# MST is a subclass of Tree, defined in the preceding chapter
class MST(Tree):
    def __init__(self, startingIndex, parent, T,
                 totalWeight, vertices):
        super().__init__(startingIndex, parent, T, vertices)
        # Total weight of all edges in the tree
        self.totalWeight = totalWeight

    def getTotalWeight(self):
        return self.totalWeight


# ShortestPathTree is an inner class in WeightedGraph
class ShortestPathTree(Tree):
    def __init__(self, sourceIndex, parent, T, costs, vertices):
        super().__init__(sourceIndex, parent, T, vertices)
        self.costs = costs

    # Return the cost for a path from the root to vertex v
    def getCost(self, v):
        return self.costs[v]

    # Print paths from all vertices to the source
    def printAllPaths(self):
        print("All shortest paths from "
              + str(self.vertices[self.root]) + " are:")
        for i in range(len(self.costs)):
            self.printPath(i)  # Print a path from i to the source
            print("(cost: " + str(self.costs[i]) + ")")  # Path cost

    def printPath(self, v):
        path = self.getPath(v)
        print("Path:", end=" ")
        for i in range(len(path)):
            print(path[i], end=" ")
            if i < len(path) - 1:
                print("->", end=" ")
        print()

    def getPath(self, vertexIndex):
        path = []
        while vertexIndex != -1:
            path.insert(0, self.vertices[vertexIndex])
            vertexIndex = self.parent[vertexIndex]
        return path
