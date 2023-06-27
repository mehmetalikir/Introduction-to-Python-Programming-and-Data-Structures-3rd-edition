# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display weighted graphs) Revise GraphView in Listing 22.4, GraphView.py,
to display a weighted graph. Write a program that displays the graph in Figure 23.1
as shown in Figure 23.17. (Instructors may ask students to expand this program
by adding new cities with appropriate edges into the graph).'''

from tkinter import *  # Import tkinter
from Graph import Graph


class GraphView(Canvas):
    def __init__(self, graph, container, width=800, height=450):
        super().__init__(container, width=width, height=height)
        self.graph = graph
        self.drawGraph()

    def drawGraph(self):
        vertices = self.graph.getVertices()
        for i in range(self.graph.getSize()):
            x = vertices[i].getX()
            y = vertices[i].getY()
            name = vertices[i].getName()

            # Display a vertex
            self.create_oval(x - 2, y - 2, x + 2, y + 2,
                             fill="black")
            # Display the name
            self.create_text(x, y - 8, text=str(name))

        # Draw edges for pair of vertices
        for i in range(self.graph.getSize()):
            neighbors = self.graph.getNeighbors(i)
            x1 = self.graph.getVertex(i).getX()
            y1 = self.graph.getVertex(i).getY()
            for e in neighbors:
                x2 = self.graph.getVertex(e.v).getX()
                y2 = self.graph.getVertex(e.v).getY()
                # Draw an edge for (i, v)        
                self.create_line(x1, y1, x2, y2)
                self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(e.weight))


from Displayable import Displayable


class City(Displayable):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    # Override the getX method
    def getX(self):
        return self.x

    # Override the getY method
    def getY(self):
        return self.y

    # Override the getName method
    def getName(self):
        return self.name


vertices = [City("Seattle", 75, 50), City("San Francisco", 50, 210),
            City("Los Angeles", 75, 275), City("Denver", 275, 175),
            City("Kansas City", 400, 245),
            City("Chicago", 450, 100), City("Boston", 700, 80),
            City("New York", 675, 120), City("Atlanta", 575, 295),
            City("Miami", 600, 400), City("Dallas", 408, 325),
            City("Houston", 450, 360)]

from tkinter import *  # Import tkinter
from WeightedGraph import WeightedGraph

# Create edges
edges = [
    [0, 1, 807], [0, 3, 1331], [0, 5, 2097],
    [1, 0, 807], [1, 2, 381], [1, 3, 1267],
    [2, 1, 381], [2, 3, 1015], [2, 4, 1663], [2, 10, 1435],
    [3, 0, 1331], [3, 1, 1267], [3, 2, 1015], [3, 4, 599],
    [3, 5, 1003],
    [4, 2, 1663], [4, 3, 599], [4, 5, 533], [4, 7, 1260],
    [4, 8, 864], [4, 10, 496],
    [5, 0, 2097], [5, 3, 1003], [5, 4, 533],
    [5, 6, 983], [5, 7, 787],
    [6, 5, 983], [6, 7, 214],
    [7, 4, 1260], [7, 5, 787], [7, 6, 214], [7, 8, 888],
    [8, 4, 864], [8, 7, 888], [8, 9, 661],
    [8, 10, 781], [8, 11, 810],
    [9, 8, 661], [9, 11, 1187],
    [10, 2, 1435], [10, 4, 496], [10, 8, 781], [10, 11, 239],
    [11, 8, 810], [11, 9, 1187], [11, 10, 239]
]

# Create a graph
graph = WeightedGraph(vertices, edges)

window = Tk()  # Create a window
window.title("Exercise23_12")  # Set title

view = GraphView(graph, window, 750, 410)
view.pack()

window.mainloop()  # Create an event loop