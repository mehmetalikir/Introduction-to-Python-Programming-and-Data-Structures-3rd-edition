# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display balls with random colors) Write a program that displays ten balls with
random colors and placed at random locations, at shown in Figure 10.22c.'''
import random
from tkinter import *  # Import tkinter

WIDTH = 200
HEIGHT = 150


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Random Balls")  # Set title

        self.canvas = Canvas(window, bg="white", width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()

        Button(frame1, text="Display", command=self.displayFigure).pack(side=BOTTOM)

        window.mainloop()  # Create an event loop

    def displayFigure(self):
        x = random.randrange(0, WIDTH)
        y = random.randrange(0, HEIGHT)
        self.canvas.create_oval(x, x, y, y, fill=self.randomColor())

    def randomColor(self):
        colors = ["red", "blue", "yellow", "green"]
        i = random.randint(0, len(colors))
        return colors[i]


MainGUI()  # Create GUI
