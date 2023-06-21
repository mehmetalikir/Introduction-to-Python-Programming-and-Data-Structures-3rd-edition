# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display a graph) Write a program that reads a graph from a file and displays it.
The first line in the file contains a number that indicates the number of vertices
(n). The vertices are labeled 0, 1, ..., n-1. Each subsequent line, with the
format u x y v1 v2 ..., describes the position of u at (x, y) and edges
(u, v1)(u, v2), and so on. Figure 22.22a gives an example of the file for their
corresponding graph. Your program prompts the user to  enter the name of the
file, reads data from a file, and displays the graph using GraphView, as shown
in Figure 22.22b.

File:
7
0 30 30 1 2
1 90 30 0 3 6
2 30 90 0 3 4
3 90 90 1 2 4 5
4 30 150 2 3 5
5 90 150 3 4 6
6 130 90 1 5'''

from math import sqrt
from tkinter import *


class GraphView:
    def __init__(self, graphFile):
        self.window = Tk()
        self.window.title("Graph View")

        self.canvas = Canvas(self.window, width=300, height=300)
        self.canvas.pack()

        self.vertices = {}
        self.edges = []

        self.readGraphFromFile(graphFile)
        self.drawGraph()

        self.window.mainloop()

    def readGraphFromFile(self, graphFile):
        with open(graphFile, 'r') as file:
            numVertices = int(file.readline().strip())
            for _ in range(numVertices):
                line = file.readline().strip().split()
                vertex = int(line[0])
                x, y = int(line[1]), int(line[2])
                adjacentVertices = [int(v) for v in line[3:]]
                self.vertices[vertex] = (x, y)
                self.edges.extend([(vertex, v) for v in adjacentVertices])

    def drawGraph(self):
        for vertex, coordinates in self.vertices.items():
            x, y = coordinates
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white", width=2)
            self.canvas.create_text(x, y, text=str(vertex))

        for edge in self.edges:
            startVertex, endVertex = edge
            x1, y1 = self.vertices[startVertex]
            x2, y2 = self.vertices[endVertex]
            self.canvas.create_line(x1, y1, x2, y2)

    def getDistance(self, x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    graphFile = input("Please enter the name of the graph file: ")
    GraphView(graphFile)


main()
