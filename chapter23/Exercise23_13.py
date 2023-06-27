# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display the shortest paths) Revise GraphView in Listing 22.4 to display a
weighted graph and a shortest path between the two specified cities, as shown
in Figure 23.18. You need to add a data field path in GraphView. If a path
is not None or empty, the edges in the path are displayed in red. If a city not
in the map is entered, the program displays a text to alert the user.'''

from tkinter import *  # Import tkinter
from Graph import Graph


class GraphView(Canvas):
    def __init__(self, graph, container, width=800, height=450, p=None):
        super().__init__(container, width=width, height=height)
        self.graph = graph
        self.path = p
        self.drawGraph()

    def setPath(self, p):
        self.path = p
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

        if self.path != None:
            print(self.path)
            for i in range(len(self.path) - 1):
                x1 = self.graph.getVertex(self.path[i]).getX()
                y1 = self.graph.getVertex(self.path[i]).getY()
                x2 = self.graph.getVertex(self.path[i + 1]).getX()
                y2 = self.graph.getVertex(self.path[i + 1]).getY()

                self.create_line(x1, y1, x2, y2, fill="red")


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


class GUI:
    def __init__(self):
        # Create a graph
        self.graph = WeightedGraph(vertices, edges)

        window = Tk()  # Create a window
        window.title("Exercise23_13")  # Set title

        self.view = GraphView(self.graph, window, 750, 410, None)
        self.view.pack()

        frame = Frame(window)
        frame.pack()
        Label(frame, text="Starting City").pack(side=LEFT)

        self.v1 = StringVar()
        Entry(frame, width=15, textvariable=self.v1, justify=RIGHT).pack(side=LEFT)
        Label(frame, text="Ending City").pack(side=LEFT)

        self.v2 = StringVar()
        Entry(frame, width=15, textvariable=self.v2, justify=RIGHT).pack(side=LEFT)
        Button(frame, text="Get Shortest Path", command=self.find).pack(side=LEFT)
        window.mainloop()  # Create an event loop

    def find(self):
        # print(self.v1.get(), self.v2.get())
        sourceVertex = self.v1.get()
        endVertex = self.v2.get()
        tree = self.graph.getShortestPath(self.getIndex(sourceVertex))
        path = tree.getPath(self.getIndex(endVertex))
        for i in range(len(path)):
            path[i] = self.getIndex(path[i].getName())
        print(path)
        self.view.setPath(path)

    def getIndex(self, s):
        for i in range(len(vertices)):
            if vertices[i].getName() == s:
                return i
        return -1


GUI()