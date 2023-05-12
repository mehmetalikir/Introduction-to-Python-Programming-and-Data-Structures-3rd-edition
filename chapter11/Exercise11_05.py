# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Move line using the arrow keys) Write a program that moves a line segment using
the arrow keys. Initially, the line positioned horizontally at the center of the frame
 and moves toward right, up, left or down when the right arrow key, Up arrow key,
 Left arrow key, or Down key is pressed, as shown in Figure 11.16c.'''
from tkinter import *  # Import tkinter


class MouseKeyEventDemo:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Arrow Keys")  # Set a title
        self.canvas = Canvas(window, bg="white", width=250, height=250)
        self.canvas.pack()

        self.canvas.create_line(10, 125, 100, 125, tags="line")

        # Bind with <Key> event
        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()

        window.mainloop()  # Create an event loop

    def processKeyEvent(self, event):
        if event.keysym == "Left":
            self.canvas.move("line", -20, 0)  # Move line
            self.canvas.update()  # Update canvas
        if event.keysym == "Right":
            self.canvas.move("line", 20, 0)  # Move line
            self.canvas.update()  # Update canvas
        if event.keysym == "Up":
            self.canvas.move("line", 0, -20)  # Move line
            self.canvas.update()  # Update canvas
        if event.keysym == "Down":
            self.canvas.move("line", 0, 20)  # Move line
            self.canvas.update()  # Update canvas


MouseKeyEventDemo()  # Create GUI
