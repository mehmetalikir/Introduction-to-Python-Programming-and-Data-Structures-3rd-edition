# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find a shortest path) Write a program that reads a connected graph from a file.
The graph is stored in a file using the same format specified in Programing Exercise
22.1. Your program should prompt the user to enter the name of the file,
then two vertices, and should display the shortest path between the two vertices.
For example, for the graph in Figure 22.19a, a shortest path between 0 and 5 may
be displayed as 0 1 3 5'''

import urllib.request

from Graph import Graph
import os.path
import sys

filename = input("Please enter a file: ").strip()
if not os.path.isfile(filename):
    print(filename, "does not exit")
    sys.exit()

s = input("Please enter two vertices (integer indexes): ")
v = [int(x) for x in s.split()]
v1, v2 = v[0], v[1]

inputFile = open(filename, "r")
# Read the number of vertices
lines = inputFile.readlines()
inputFile.close()

numberOfVertices = int(lines[0])

print("The number of vertices is", numberOfVertices)

vertices = []
edges = []

for line in lines[1:]:
    tokens = [int(x) for x in line.split()]

    startingVertex = tokens[0]
    vertices.append(startingVertex)
    for adjacentVertex in tokens[1:]:
        edges.append([startingVertex, adjacentVertex])

graph = Graph(vertices, edges)
graph.printEdges()
tree = graph.bfs(v1)
path = tree.getPath(v2)

print("The path is", end=' ')
for v in path:
    print(v, end=' ')