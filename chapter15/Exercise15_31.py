# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: Recursive tree) Write a program to display a recursive tree, as shown in
Figure 15.17.'''

import math
from tkinter import *

angleFactor = math.pi / 5
sizeFactor = 0.58


# Function to draw a branch of the recursive tree
def paintBranch(canvas, depth, x1, y1, length, angle):
    if depth >= 0:
        x2 = x1 + math.cos(angle) * length
        y2 = y1 + math.sin(angle) * length

        # Draw the line
        canvas.create_line(x1, y1, x2, y2, width=2)

        # Draw the left branch
        paintBranch(canvas, depth - 1, x2, y2, length * sizeFactor, angle + angleFactor)
        # Draw the right branch
        paintBranch(canvas, depth - 1, x2, y2, length * sizeFactor, angle - angleFactor)


def main():
    # Create the main window
    window = Tk()
    window.title("Recursive Tree")

    # Create a canvas to draw the tree
    canvas = Canvas(window, width=400, height=400)
    canvas.pack()

    depth = float(input("Please enter a depth: "))
    paintBranch(canvas, depth, 200, 350, 100, -math.pi / 2)

    # Start the Tkinter event loop
    window.mainloop()


main()
