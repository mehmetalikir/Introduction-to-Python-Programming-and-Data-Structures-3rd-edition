# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Move a circle using keys) Write a program that moves a circle up, down, left, or
right, using the arrow keys, as shown in Figure 11.18c-d.'''

from tkinter import *  # Import tkinter


class MoveACircle:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Moving Circle")  # Set a title
        self.canvas = Canvas(window, bg="white", width=250, height=250)
        self.canvas.pack()

        self.canvas.create_oval(25, 5, 75, 55, tags="circle")

        # Bind with <Key> event
        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()

        window.mainloop()  # Create an event loop

    def processKeyEvent(self, event):
        if event.keysym == "Left":
            self.canvas.move("circle", -20, 0)  # Move circle
            self.canvas.update()  # Update canvas
        if event.keysym == "Right":
            self.canvas.move("circle", 20, 0)  # Move circle
            self.canvas.update()  # Update canvas
        if event.keysym == "Up":
            self.canvas.move("circle", 0, -20)  # Move circle
            self.canvas.update()  # Update canvas
        if event.keysym == "Down":
            self.canvas.move("circle", 0, 20)  # Move circle
            self.canvas.update()  # Update canvas


MoveACircle()  # Create GUI
