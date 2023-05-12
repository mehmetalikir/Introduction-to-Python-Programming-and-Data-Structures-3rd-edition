# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: inside a rectangle?) Write a program that draws a fixed rectangle centered
at (100, 60) with width 100 and height 40. Whenever the mouse is moved,
display the message indicating whether the mouse pointer is inside the rectangle,
as shown in Figure 11.20. To detect whether the pointer is inside a rectangle, use the
Rectangle2D class defined in Exercise 9.13.'''
import math
from tkinter import *  # Import tkinter

width = 240
height = 120


# hipotenus = 0


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Inside the rectangle?")  # Set a title

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        self.canvas.create_rectangle(10, 10, 100, 60, tags="rectangle")

        self.canvas.bind("<B1-Motion>", self.isInside)

        window.mainloop()  # Create an event loop

    def isInside(self, event):
        self.canvas.delete("text")
        if isInsideRectangle(100, 60, event.x, event.y):
            self.canvas.create_text(event.x, event.y,
                                    text="Mouse pointer is in the rectangle", tags="text")
        else:
            self.canvas.create_text(event.x, event.y,
                                    text="Mouse pointer is not in the rectangle", tags="text")


def isInsideRectangle(r1X, r1Y, r2X, r2Y):
    # Determine whether the mouse pointer is inside the rectangle
    if ((math.pow(math.pow(r2Y - r1Y, 2), .05) + r2Y / 2 <= r1Y / 2) and
            (math.pow(math.pow(r2X - r1X, 2), .05) + r2X / 2 <= r1X / 2) and
            (r1Y / 2 + r2Y / 2 <= r1Y) and
            (r1X / 2 + r2X / 2 <= r1X)):
        return True


MainGUI()
