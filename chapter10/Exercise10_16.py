# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display a polygonal) Write a program that displays a random coordinated
polygonal, as shown Figure 10.23a.'''
from tkinter import *  # Import tkinter
import random


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Random Polygon")  # Set title

        canvas = Canvas(window, bg="white", width=200, height=150)
        canvas.pack()

        # Generate random coordinates
        points = []
        for i in range(0, 12):
            if i % 2 == 0:
                points.append(self.getX())
            else:
                points.append(self.getY())

        # Create polygon with random coordinates
        canvas.create_polygon(points, outline='yellow', fill='navy', width=2)

        window.mainloop()  # Create an event loop

    def getX(self):
        return random.randint(10, 190)

    def getY(self):
        return random.randint(10, 140)


MainGUI()  # Create GUI
