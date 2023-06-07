# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: H-tree fractal) An H-tree is a fractal defined as follows:
    1. Begin with a letter H. The three lines of the H are of the same length, as shown
    in Figure 15.1a.
    2. The letter H (in its sans-serif form, H) has four endpoints. Draw an H centered
    at each of the four endpoints to an H-tree of order 1, as shown in Figure 15.1b.
    These Hs are half the size of the H that contains the four endpoints.
    3. Repeat Step 2 to create an H-tree of order 2, 3, ..., and so on, as shown in
    Figure 15.1c–d.
Write a Python program that draws an H-tree, as shown in Figure 15.1.'''

from tkinter import *

# Function to draw an H-tree fractal
def drawHTree(canvas, x, y, size, depth):
    if depth == 0:
        return

    # Calculate the coordinates of the four endpoints of the H
    x0 = x - size / 2
    x1 = x + size / 2
    y0 = y - size / 2
    y1 = y + size / 2

    # Draw the horizontal lines of the H
    canvas.create_line(x0, y, x1, y, width=2)
    canvas.create_line(x0, y0, x0, y1, width=2)
    canvas.create_line(x1, y0, x1, y1, width=2)

    # Recursively draw H-trees of smaller size and depth
    newSize = size / 2
    newDepth = depth - 1

    drawHTree(canvas, x0, y0, newSize, newDepth)  # Upper left
    drawHTree(canvas, x0, y1, newSize, newDepth)  # Lower left
    drawHTree(canvas, x1, y0, newSize, newDepth)  # Upper right
    drawHTree(canvas, x1, y1, newSize, newDepth)  # Lower right

# Create the main window
window = Tk()
window.title("H-Tree Fractal")

# Create a canvas to draw the H-tree
canvas = Canvas(window, width=500, height=500)
canvas.pack()

# Draw the H-tree at the center of the canvas
centerX = canvas.winfo_width() / 2
centerY = canvas.winfo_height() / 2
initialSize = 200
initialDepth = 3
drawHTree(canvas, centerX, centerY, initialSize, initialDepth)

# Start the Tkinter event loop
window.mainloop()



