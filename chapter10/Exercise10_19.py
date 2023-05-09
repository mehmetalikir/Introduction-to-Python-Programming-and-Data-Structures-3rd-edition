# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Draw a rectangle) Write a program that randomly draws a rectangle when the
Draw a Random Rectangle button is clicked, as shown in Figure 10.24b.'''
import random
from tkinter import *  # Import tkinter


class MainGUI:

    def __init__(self):
        window = Tk()  # Create a window
        window.title("Random Rectangle")  # Set a title

        self.canvas = Canvas(window, width=400, height=300, bg="white")
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()

        Button(frame1, text="Draw a Random Rectangle",
               command=self.randomRectangle).pack(side=BOTTOM)

        window.mainloop()  # Create an event loop

    def randomRectangle(self):
        x = random.randint(50, 400)
        y = random.randint(50, 300)
        self.canvas.create_rectangle(x + 10, y + 10, x, y, fill="blue")


MainGUI()  # Create GUI
