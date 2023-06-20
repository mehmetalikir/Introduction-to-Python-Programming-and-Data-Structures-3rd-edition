# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Connected rectangles) Listing 22.8, ConnectedCircles.py  allows the user to
create circles and determine whether they are connected. Rewrite the program
for rectangles. The program lets the user create a rectangle by clicking a mouse
in a blank area repainted filled if they are connected or unfilled otherwise,
as shown in Figure 22.20b-c'''

from tkinter import *


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def add(event):
    rectangles.append(Rectangle(event.x, event.y, event.x + width, event.y + height))
    repaint()


def intersect(rect1, rect2):
    return not (rect1.x2 < rect2.x1 or rect1.x1 > rect2.x2 or rect1.y2 < rect2.y1 or rect1.y1 > rect2.y2)


def repaint():
    canvas.delete("rectangle")

    if len(rectangles) == 0:
        return  # Nothing to paint

    sets = getConnectedSets(rectangles)

    for i, rect in enumerate(rectangles):
        for j, connected_set in enumerate(sets):
            if i in connected_set:
                color = COLORS[j % len(COLORS)]  # Use different colors for different sets
                canvas.create_rectangle(rect.x1, rect.y1, rect.x2, rect.y2, fill=color, tags="rectangle")
                break
        else:
            canvas.create_rectangle(rect.x1, rect.y1, rect.x2, rect.y2, tags="rectangle")


def getConnectedSets(rectangles):
    sets = []
    for i, rect1 in enumerate(rectangles):
        connected_set = {i}
        for j, rect2 in enumerate(rectangles):
            if j != i and intersect(rect1, rect2):
                connected_set.add(j)
        sets.append(connected_set)
    return sets


window = Tk()
window.title("ConnectedRectangles")

width = 100
height = 50
canvas_width = 800
canvas_height = 600

canvas = Canvas(window, bg="white", width=canvas_width, height=canvas_height)
canvas.pack()

rectangles = []
canvas.bind("<Button-1>", add)

COLORS = ["red", "green", "blue", "orange", "purple"]  # Colors for the rectangles

window.mainloop()
