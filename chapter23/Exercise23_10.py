# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Create a file for a graph) Modify Listing 23.3, TestWeightedGraph.py,
to create a file for representing graph1. The first line in the file contains a number
that indicates the number of vertices(n). The vertices are labeled as 0,1, ..., n-1. Each
subsequent line describes the edges in the form of u1, v1, w1 | u2, v2, w2
| .... Each triplet in this form describes an edge and its weight. Note that we assume
the graph is undirected. If the graph has an edge(u, v) it also has an edge(v,u).
Only one edge is represented in the file. When you construct a graph, both edges
need to be added. Create the file form the array defined in lines 724 in Listing
23.3. The number of vertices for the graph is 12, which will be sorted in the first
line of the line. An edge (u, v) is stored if u < v. The contents of the file should
be as follows:
12
0, 1, 807 | 0, 3, 1331 | 0, 5, 2097
1, 2, 381 | 1, 3, 1267
2, 3, 1015 | 2, 4, 1663 | 2, 10, 1435
3, 4, 599 | 3, 5, 1003
4, 5, 533 | 4, 7, 1260 | 4, 8, 864 | 4, 10, 496
5, 6, 983 | 5, 7, 787
6, 7, 214
7, 8, 888
8, 9, 661 | 8, 10, 781 | 8, 11, 810
9, 11, 1187
10, 11, 239'''

from WeightedGraph import WeightedGraph, WeightedEdge

# Create vertices
vertices = ["Seattle", "San Francisco", "Los Angeles",
            "Denver", "Kansas City", "Chicago", "Boston", "New York",
            "Atlanta", "Miami", "Dallas", "Houston"]

# Create edges
edges = [
    [0, 1, 807], [0, 3, 1331], [0, 5, 2097],
    [1, 2, 381], [1, 3, 1267],
    [2, 3, 1015], [2, 4, 1663], [2, 10, 1435],
    [3, 4, 599], [3, 5, 1003],
    [4, 5, 533], [4, 7, 1260], [4, 8, 864], [4, 10, 496],
    [5, 6, 983], [5, 7, 787],
    [6, 7, 214],
    [7, 8, 888],
    [8, 9, 661], [8, 10, 781], [8, 11, 810],
    [9, 11, 1187],
    [10, 11, 239]
]

# Create a graph
graph1 = WeightedGraph(vertices, edges)

# Create a file for graph1
with open("graph1.txt", "w") as file:
    # Write the number of vertices
    file.write(str(graph1.getSize()) + "\n")

    # Write the edges
    for vertex in range(graph1.getSize()):
        for edge in graph1.getNeighbors(vertex):
            if vertex < edge.v:  # Store edge only once if u < v
                file.write(f"{vertex}, {edge.v}, {edge.weight} | ")

    # Move the file cursor back by 3 characters to remove the last " | "
    file.seek(file.tell() - 3)
    file.truncate()

print("graph1.txt file has been created.")
