# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Swap background and foreground color) Write a program to swap between
background and foreground color of a canvas with text "Programming is fun"
using a left mouse click, as shown in Figure 11.15'''
import random
from tkinter import *  # Import tkinter

width = 220
height = 100


class SwapColor:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Set Colors")  # Set a title

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        # Bind canvas with mouse events
        self.canvas.bind("<Button-1>", self.displayPosition)

        window.mainloop()  # Create an event loop

    def displayPosition(self, event):
        if event:
            self.canvas.configure(bg=self.getRandomColor())
            self.canvas.create_text(110, 40, text="Programing is Fun", fill=self.getRandomColor(), font="Times 11 bold")

    def getRandomColor(self):
        color = "#"
        for r in range(6):
            color += self.toHexChar(random.randint(0, 15))
        return color

    def toHexChar(self, hexValue):
        if 0 <= hexValue <= 9:
            return chr(hexValue + ord('0'))
        else:
            return chr(hexValue - 10 + ord('A'))


SwapColor()
