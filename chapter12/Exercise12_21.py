# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: display an n-sided regular polygon) In Exercise 12.20 you created the
RegularPolygonPanel subclass for displaying an n-sided regular polygon.
Write a program that displays a regular polygon and uses two buttons named
and to increase or decrease the size of the polygon, as shown in Figure
12.31a–b. Also enable the user to increase or decrease the size by clicking the
right or left mouse button and by pressing the UP and DOWN arrow keys'''

import math
from tkinter import *  # Import tkinter


class RegularPolygonCanvas(Canvas):
    def __init__(self, parent, numberOfSides=3, width=150, height=150):
        super().__init__(parent, width=width, height=height)
        self.setNumberOfSides(numberOfSides)

    def getNumberOfSides(self):
        return self.__numberOfSides

    def setNumberOfSides(self, numberOfSides):
        self.__numberOfSides = numberOfSides
        self.drawPolygon()

    def drawPolygon(self):
        self.delete("polygon")

        width = int(self["width"])
        height = int(self["height"])
        xCenter = width / 2
        yCenter = height / 2
        radius = min(width, height) * 0.4

        angle = 2 * math.pi / self.__numberOfSides

        # Create a Polygon object
        polygon = []

        # Add points to the polygon
        for i in range(self.__numberOfSides):
            polygon.append([xCenter + radius * math.cos(i * angle),
                            yCenter - radius * math.sin(i * angle)])

            # Draw the polygon
        self.create_polygon(polygon, fill="red", tags="polygon")


class MainClass:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("n-sided Polygons")  # Set title

        self.canvas = RegularPolygonCanvas(window, 5)
        self.canvas.pack(side=LEFT)

        frame = Frame(window)
        frame.pack()
        Button(frame, text="+1", command=self.add).pack(side=LEFT)
        Button(frame, text="-1", command=self.add).pack(side=LEFT)

        # Bind with <Key> event
        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()

        window.mainloop()  # Create an event loop

    def processKeyEvent(self, event):
        if event.keysym == "Up":
            self.canvas.update()  # Update canvas
        if event.keysym == "Down":
            self.canvas.update()  # Update canvas

    def add(self):
        pass

    def remove(self):
        pass


MainClass()
