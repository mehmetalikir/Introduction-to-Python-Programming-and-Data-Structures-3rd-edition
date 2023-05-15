# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display circles) Write a program that displays a new larger circle with a left
mouse click and removes the largest circle with a right mouse click, as shown in
Figure 11.22.'''

from tkinter import *  # Import tkinter


class Circle:
    def __init__(self):
        self.i = 3
        self.x0 = 190 - self.i * 5
        self.y0 = 110 - self.i * 5
        self.x1 = 220 + self.i * 5
        self.y1 = 140 + self.i * 5
        self.outline = "#000"
        self.width = 1.5


class DisplayCircles:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Display Circles")  # Set a title

        frame = Frame(window)
        frame.pack()

        # Place self.canvas in the window
        self.canvas = Canvas(frame, width=400, height=400, bg="white")
        self.canvas.pack()

        self.circleList = []  # Create a list for circles

        # Bind Button-1 displays a new larger circle with a left mouse click

        # self.canvas.bind("<Button-1>", self.addCircle())
        self.animate()

        # # Bind Button-3 removes the largest circle with a right mouse click
        # self.canvas.bind("<Button-3>", self.removeCircle)

        window.mainloop()  # Create an event loop

    # Display circles
    def displayCricles(self, circle):
        self.canvas.create_oval(circle.x0, circle.y0, circle.x1, circle.y1,
                                outline=circle.outline, width=circle.width)

    def animate(self):  # Move the message

        for circle in self.circleList:
            self.displayCricles(circle)

        self.canvas.update()  # Update self.canvas

    def addCircle(self, circle):  # Add a new circle

        self.circleList.append(Circle())

    def removeCircle(self):  # Remove the last circle

        self.circleList.pop()


DisplayCircles()  # Create GUI
