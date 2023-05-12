# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: pendulum) Write a program that animates a pendulum swinging, as
shown in Figure 11.21. Press the Up arrow key to increase the speed and the Down
arrow key to decrease it. Press the S key to stop the animation and the R key to
resume it.'''

import math
from tkinter import *  # Import tkinter

width = 200
height = 200
pendulumRadius = 150
ballRadius = 10
leftAngle = 120
rightAngle = 60


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Pendulum")  # Set a title

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        self.angle = leftAngle  # Start from leftAngle
        self.angleDelta = 1  # Swing interval
        delay = 10

        while True:
            self.canvas.delete("pendulum")
            self.displayPendulum()
            self.canvas.after(delay)  # Sleep for 100 milliseconds
            self.canvas.update()  # Update canvas

        self.displayPendulum()

        window.mainloop()  # Create an event loop

    def displayPendulum(self):
        x1 = width / 2
        y1 = 20

        if self.angle < rightAngle:
            self.angleDelta = 1  # Swing to the left
        elif self.angle > leftAngle:
            self.angleDelta = -1  # Swing to the right

        self.angle += self.angleDelta
        x = x1 + pendulumRadius * math.cos(math.radians(self.angle))
        y = y1 + pendulumRadius * math.sin(math.radians(self.angle))

        self.canvas.create_line(x1, y1, x, y, tags="pendulum")
        self.canvas.create_oval(x1 - 2, y1 - 2, x1 + 2, y1 + 2, fill="black", tags="pendulum")
        self.canvas.create_oval(x - ballRadius, y - ballRadius, x + ballRadius, y + ballRadius,
                                fill="black", tags="pendulum")


MainGUI()
