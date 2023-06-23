# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Kruskal’s algorithm) The text introduced Prim’s algorithm for finding a minimum
spanning tree. Kruskal’s algorithm is another well-known algorithm for
finding a minimum spanning tree. The algorithm repeatedly finds a minimum-weight
edge and adds it to the tree if it does not cause a cycle. The process ends
Programming Exercises 1091
when all vertices are in the tree. Design and implement an algorithm for finding
an MST using Kruskal’s algorithm.

Prim’s Minimum Spanning Tree Algorithm
Input: A connected undirected weighted G = (V, E) with non-negative weights
Output: MST (a minimum spanning tree)
def getMinimumSpanningTree(s):
    Let T be a set for the vertices in the spanning tree;
    Initially, add the starting vertex, s,  to T;

    while size of T < n:
        find x in T and y in V – T with the smallest weight
            on the edge (x, y), as shown in Figure 23.6;
        add y to T and set parent[y] = x;
'''


class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.makeSet(v)

    def makeSet(self, v):
        self.parent[v] = v
        self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskalMinSpanningTree(graph):
    vertices = graph.keys()
    disjointSet = DisjointSet(vertices)
    edges = []

    # Create a list of all edges
    for u in vertices:
        for v, weight in graph[u]:
            edges.append((u, v, weight))

    # Sort the edges by weight in non-decreasing order
    edges.sort(key=lambda x: x[2])

    minimumSpanningTree = []

    for u, v, weight in edges:
        if disjointSet.find(u) != disjointSet.find(v):
            disjointSet.union(u, v)
            minimumSpanningTree.append((u, v, weight))

    return minimumSpanningTree

graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('C', 1), ('D', 2)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 2), ('C', 4)]
}

minSpanningTree = kruskalMinSpanningTree(graph)
print(minSpanningTree)

