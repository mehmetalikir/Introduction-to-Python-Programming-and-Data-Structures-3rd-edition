# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: two rectangles intersect?) Using the Rectangle2D class you defined in
Exercise 9.13, write a program that enables the user to point the mouse inside a
rectangle and drag it. As the rectangle is being dragged, the label displays whether
two rectangles overlap, as shown in Figure 12.19.'''

from tkinter import *  # Import tkinter


class Rectangle2D:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def getArea(self):
        return self.width * self.height

    def containsPoint(self, x, y):
        return abs(x - self.x) <= self.width / 2 and abs(y - self.y) <= self.height / 2

    def contains(self, r):
        return self.containsPoint(r.x - r.width / 2, r.y + r.height / 2) and \
               self.containsPoint(r.x - r.width / 2, r.y - r.height / 2) and \
               self.containsPoint(r.x + r.width / 2, r.y + r.height / 2) and \
               self.containsPoint(r.x + r.width / 2, r.y - r.height / 2)

    def overlaps(self, r):
        return abs(self.x - r.x) <= (self.width + r.width) / 2 and \
               abs(self.y - r.y) <= (self.height + r.height) / 2


def displayRectangle(r, text):
    canvas.delete(text)
    canvas.create_rectangle(r.x, r.y, r.width, r.height, tags=text)
    canvas.create_text(r.x, r.y, text=text, tags=text)


def mouseMoved(event):
    if r1.containsPoint(event.x, event.y):
        r1.setWidth(event.x)
        r1.setHeight(event.y)
        displayRectangle(r1, "r1")
        if r1.overlaps(r2):
            label["text"] = "Two rectangles intersect"
        else:
            label["text"] = "Two rectangles don't intersect"
    elif r2.containsPoint(event.x, event.y):
        r2.setWidth(event.x)
        r2.setHeight(event.y)
        displayRectangle(r2, "r2")
        if r1.overlaps(r2):
            label["text"] = "Two rectangles intersect"
        else:
            label["text"] = "Two rectangles don't intersect"


window = Tk()  # Create a window
window.title("Two Rectangle")  # Set title

width = 300
height = 100
label = Label(window, text="Two rectangle intersect")
label.pack()
canvas = Canvas(window, width=width, height=height)
canvas.pack()

canvas.bind("<B1-Motion>", mouseMoved)
r1 = Rectangle2D(50, 50, 100, 60)
r2 = Rectangle2D(50, 50, 60, 100)
displayRectangle(r1, "r1")
displayRectangle(r2, "r2")

window.mainloop()  # Create an event loop
