# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Racing car) Write a program that simulates car racing, as shown in Figure
11.17b–d. The car moves from left to right. When it reaches the right end, it restarts
from the left and continues the same process. Let the user increase and decrease
the car’s speed by pressing the Up and Down arrow keys.'''

from tkinter import *  # Import tkinter


class RacingCar:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Racing Car")  # Set a title
        self.width = 250  # Width of the self.canvas
        self.canvas = Canvas(window, bg="white", width=200, height=200)
        self.canvas.pack()

        # Bind with <Key> event
        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()

        self.sleepTime = 100  # Set a sleep time
        self.x, self.y = 0, 110  # Starting x position

        # TO-DO -> Draw car object
        self.canvas.create_polygon(self.x + 10.0, self.y - 20.0, self.x + 20.0, self.y - 30.0, self.x + 30.0,
                                   self.y - 30.0, self.x + 40.0, self.y - 20.0, tags="car")

        self.dx = 3
        self.isStopped = False
        self.animate()

        window.mainloop()  # Create an event loop

    def processKeyEvent(self, event):
        if event.keysym == "Up":  # Speed up the animation
            self.sleepTime -= 10
        if event.keysym == "Down":
            self.sleepTime += 10  # Slow down the animation

    def animate(self):  # Move the message
        while not self.isStopped:
            self.canvas.move("car", self.dx, 0)  # Move text
            self.canvas.after(self.sleepTime)  # Sleep
            self.canvas.update()  # Update self.canvas
            if self.x < self.width:
                self.x += self.dx  # Set new position
            else:
                self.x = 0  # Reset car position to the beginning
                self.canvas.delete("car")
                # Redraw text at the beginning
                self.canvas.create_polygon(self.x + 10.0, self.y - 20.0, self.x + 20.0, self.y - 30.0, self.x + 30.0,
                                           self.y - 30.0, self.x + 40.0, self.y - 20.0, tags="car")


RacingCar()  # Create GUI
