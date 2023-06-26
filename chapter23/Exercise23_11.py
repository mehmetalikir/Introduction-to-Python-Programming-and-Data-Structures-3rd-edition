# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the shortest paths) Write a program that reads a connected graph from a file.
The graph is stored in a file using the same format specified in Programming
Exercise 23.10. Your program should prompt the user to enter a URL for the file
and the two vertices, and should display the shortest path between the two
vertices. For example, for the graph in Figure 23.16, a shortest path between 0
and 1 can be displayed as 0 2 4 3 1.
Here is a sample run of the program:
Enter a URL : https://liveexample.pearsoncmg.com/test/WeightedGraphSample2.txt
Enter two vertices (integer indexes): 0 1
The number of vertices is 6
Vertex 0: (0, 2, 3) (0, 1, 100)
Vertex 1: (1, 3, 20) (1, 0, 100)
Vertex 2: (2, 4, 2) (2, 3, 40) (2, 0, 3)
Vertex 3: (3, 4, 5) (3, 5, 5) (3, 1, 20) (3, 2, 40)
Vertex 4: (4, 2, 2) (4, 3, 5) (4, 5, 9)
Vertex 5: (5, 3, 5) (5, 4, 9)
A path from 0 to 1: 0 2 4 3 1'''

from collections import deque
from heapq import heappop, heappush


class WeightedEdge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


class WeightedGraph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.adjacencyList = [[] for _ in range(len(vertices))]

        for edge in edges:
            u, v, weight = edge
            self.addEdge(u, v, weight)

    def addEdge(self, u, v, weight):
        edge = WeightedEdge(u, v, weight)
        self.adjacencyList[u].append(edge)
        self.adjacencyList[v].append(edge)

    def getNeighbors(self, vertex):
        return self.adjacencyList[vertex]

    def getShortestPath(self, startVertex, endVertex):
        distances = [float('inf')] * len(self.vertices)
        distances[startVertex] = 0

        previousVertices = [None] * len(self.vertices)

        priorityQueue = [(0, startVertex)]

        while priorityQueue:
            currentDistance, currentVertex = heappop(priorityQueue)

            if currentVertex == endVertex:
                break

            if currentDistance > distances[currentVertex]:
                continue

            for edge in self.adjacencyList[currentVertex]:
                neighbor = edge.u if edge.v == currentVertex else edge.v
                distance = currentDistance + edge.weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previousVertices[neighbor] = currentVertex
                    heappush(priorityQueue, (distance, neighbor))

        shortestPath = []
        currentVertex = endVertex

        while currentVertex is not None:
            shortestPath.append(currentVertex)
            currentVertex = previousVertices[currentVertex]

        shortestPath.reverse()

        return shortestPath


# Function to read the graph from a file
def readGraphFromFile(filePath):
    graph = None
    try:
        with open(filePath, "r") as file:
            numVertices = int(file.readline().strip())
            vertices = [str(i) for i in range(numVertices)]
            edges = []

            for line in file:
                edgeData = line.strip().split(", ")
                u = int(edgeData[0])
                v = int(edgeData[1])
                weight = int(edgeData[2].split(" | ")[0])
                edges.append([u, v, weight])

            graph = WeightedGraph(vertices, edges)
    except IOError:
        print("Error reading the file.")

    return graph


# Prompt the user to enter the file name
fileName = input("Please enter a file name: ")

# Read the graph from the file
graph = readGraphFromFile(fileName)

if graph is not None:
    # Prompt the user to enter two vertices
    startVertex, endVertex = map(int, input("Please enter two vertices (integer indexes): ").split())

    # Find the shortest path using Dijkstra's algorithm
    shortestPath = graph.getShortestPath(startVertex, endVertex)

    # Display the number of vertices
    numVertices = len(graph.vertices)
    print("The number of vertices is", numVertices)

    # Display the adjacency list for each vertex
    for vertex in range(numVertices):
        print("Vertex", vertex, ":", end=" ")
        for edge in graph.getNeighbors(vertex):
            print(f"({edge.u}, {edge.v}, {edge.weight})", end=" ")
        print()

    # Display the shortest path
    print("A path from", startVertex, "to", endVertex, ":", " ".join(map(str, shortestPath)))
else:
    print("Graph could not be read from the file.")
