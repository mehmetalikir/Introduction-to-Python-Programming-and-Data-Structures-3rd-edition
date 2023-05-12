# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Draw dots using mouse click) Write a program that draws dot on the location of
the mouse pointer location when the mouse is clicked(see Figure 11.16a-b).'''

from tkinter import *  # Import tkinter

width = 220
height = 100


class DrawDots:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Draw Dots")  # Set a title

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        # Bind canvas with mouse events
        self.canvas.bind("<Button-1>", self.displayPosition)

        window.mainloop()  # Create an event loop

    def displayPosition(self, event):
        self.canvas.create_oval(event.x, event.y, event.x - 5, event.y - 5, fill="red")


DrawDots()
