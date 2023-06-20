# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Move a circle) Modify Listing 22.8, ConnectedCircles.py, to enable the user to drag
and move a circle'''

from tkinter import *


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def add(event):
    circles.append(Vertex(event.x, event.y))
    repaint()


def distance(vertex1, vertex2):
    return ((vertex1.x - vertex2.x) ** 2 + (vertex1.y - vertex2.y) ** 2) ** 0.5


def repaint():
    canvas.delete("point")

    if len(circles) == 0:
        return  # Nothing to paint

    # Build the edges
    edges = []
    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):
            if distance(circles[i], circles[j]) <= 2 * radius:
                edges.append([i, j])
                edges.append([j, i])

    sets = getConnectedSets(circles, edges)

    for i, vertex in enumerate(circles):
        for j, connected_set in enumerate(sets):
            if i in connected_set:
                color = COLORS[j % len(COLORS)]  # Use different colors for different sets
                canvas.create_oval(vertex.x - radius, vertex.y - radius, vertex.x + radius, vertex.y + radius,
                                   fill=color, tags="point")
                break
        else:
            canvas.create_oval(vertex.x - radius, vertex.y - radius, vertex.x + radius, vertex.y + radius,
                               tags="point",  fill="yellow")


def getConnectedSets(vertices, edges):
    graph = {}
    for vertex in vertices:
        graph[vertex] = set()

    for edge in edges:
        v1, v2 = edge
        graph[vertices[v1]].add(vertices[v2])
        graph[vertices[v2]].add(vertices[v1])

    sets = []
    visited = set()

    for vertex in vertices:
        if vertex not in visited:
            connected_set = set()
            dfs(graph, vertex, visited, connected_set)
            sets.append(connected_set)

    return sets


def dfs(graph, start, visited, connected_set):
    visited.add(start)
    connected_set.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, connected_set)


def move(event):
    x, y = event.x, event.y

    # Find the closest circle to the mouse position
    closest_circle = None
    min_distance = float('inf')

    for i, vertex in enumerate(circles):
        d = distance(Vertex(x, y), vertex)
        if d < min_distance:
            min_distance = d
            closest_circle = vertex

    if closest_circle is not None:
        closest_circle.x = x
        closest_circle.y = y
        repaint()


window = Tk()
window.title("ConnectedCircles")

width = 250
height = 200
radius = 15
canvas = Canvas(window, bg="white", width=width, height=height)
canvas.pack()

circles = []
canvas.bind("<Button-1>", add)
canvas.bind("<B1-Motion>", move)  # Bind mouse motion to the move function

COLORS = ["red", "blue", "green", "orange", "purple"]  # List of colors for different sets

window.mainloop()
