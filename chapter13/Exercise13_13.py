# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: display a graph) A graph consists of vertices and edges that connect
vertices. Write a program that reads a graph from a file and displays it on a
panel. The first line in the file contains a number that indicates the number of
vertices (n). The vertices are labeled as 0, 1, ..., n-1. Each subsequent line, with
the format u x y v1, v2, ..., describes that the vertex u is located at position
(x, y) with the edges (u, v1), (u, v2), and so on. Figure 13.12a gives an example
of the file for a graph. Your program prompts the user to enter the name of the
file, reads data from the file, and displays the graph on a panel, as shown in
Figure 13.13b.'''

from tkinter import *  # Import tkinter


def displayGraph(canvas, vertices, edges):
    radius = 3
    for vertex, x, y in vertices:
        canvas.create_text(x - 2 * radius, y - 2 * radius, text=str(vertex), tags="graph")
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="black", tags="graph")

    for v1, v2 in edges:
        canvas.create_line(vertices[v1][1], vertices[v1][2], vertices[v2][1], vertices[v2][2], tags="graph")


def main():
    # Prompt the user to enter a filename
    global input
    data = str(input("Please enter file name: ").strip())

    numberOfVertices = int(data.readline().decode())  # Read the first line from the file
    print(numberOfVertices)

    vertices = []
    edges = []
    for i in range(numberOfVertices):
        items = data.readline().strip().split()  # Read the info for one vertex
        vertices.append([float(items[0]), float(items[1]), float(items[2])])
        for j in range(3, len(items)):
            edges.append([float(items[0]), float(items[j])])

    print(vertices)
    print(edges)

    data.close()  # Close the input file

    window = Tk()  # Create a window
    window.title("Display a Graph")  # Set title

    frame1 = Frame(window)  # Hold four labels for displaying cards
    frame1.pack()
    canvas = Canvas(frame1, width=300, height=200)
    canvas.pack()

    displayGraph(canvas, vertices, edges)

    window.mainloop()  # Create an event loop


main()
