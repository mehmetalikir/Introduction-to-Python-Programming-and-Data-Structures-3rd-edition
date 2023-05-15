# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display five filled circles) Write a program that displays five filled circles, as
shown in Figure 11.24a. Enable the user to drag the blue ring using the mouse, as
shown in Figure 11.24b.'''

from tkinter import *  # Import tkinter


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    # Is point (x, y) inside this circle?
    def isInside(self, x, y):
        return distance(self.x, self.y, x, y) <= self.radius


width = 400
height = 250
x = 100
y = 100
hGap = 120
vGap = 50
radius = 50


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Dragging The Blue Circle")  # Set title

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()

        self.c1 = Circle(x, y, radius)
        self.c2 = Circle(x + hGap, y, radius)
        self.c3 = Circle(x + 2 * hGap, y, radius)
        self.c4 = Circle(x + radius, y + vGap, radius)
        self.c5 = Circle(x + 190, y + vGap, radius)

        self.paint(self.c1, "blue", "c1")
        self.paint(self.c2, "black")
        self.paint(self.c3, "red")
        self.paint(self.c4, "yellow")
        self.paint(self.c5, "green")

        self.canvas.bind("<B1-Motion>", self.mouseMoved)

        window.mainloop()  # Create an event loop

    def mouseMoved(self, event):
        if self.c1.isInside(event.x, event.y):
            self.c1.x = event.x
            self.c1.y = event.y

        self.canvas.delete("c1")
        self.paint(self.c1, "blue", "c1")

    def paint(self, c, color, tags="stable"):
        self.canvas.create_oval(c.x - c.radius, c.y - c.radius, c.x + c.radius, c.y + c.radius, fill=color,
                                activefill="gold", tags=tags)


def distance(x1, y1, x2, y2):
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5


MainGUI()
