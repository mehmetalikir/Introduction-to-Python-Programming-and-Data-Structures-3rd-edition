# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Plot the sine function) Exercise 5.52 draws a sine function using Turtle.
Rewrite the program to draw a sine function using Tkinter, as shown in Figure 10.28a.
Hint:
The Unicode for p is \u03c0. To display –2p use turtle.write("-2\u03c0"). For
a trigonometric function like sin(x), x is in radians. Use the following loop to add the
points to a polygon p:

p = []
for x in range(-175, 176):
    p.append([x, -50 * math.sin((x / 100.0) * 2 *
                                math.pi)])

–2p is displayed at (-100, -15), the center of the axis is at (0, 0), and 2p is displayed at
(100, -15).
'''
import math
from tkinter import *  # Import tkinter


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Sine Function")  # Set title

        width = 400
        height = 150
        canvas = Canvas(window, width=width, height=height)
        canvas.pack()

        # Draw sine function
        p = []
        for x in range(-175, 176):
            p.append([x + width / 2, -50 * math.sin((x / 100.0) * 2 * math.pi) + height / 2])

        for i in range(len(p) - 1):
            canvas.create_line(p[i], p[i + 1])

        # Draw X-axis
        canvas.create_line(10, height / 2, width - 10, height / 2)
        canvas.create_text(width / 2 + 100, height / 2 + 10, text="2\u03c0")
        canvas.create_text(width / 2 - 100, height / 2 + 10, text="-2\u03c0")
        canvas.create_line(width - 10 - 10, height / 2 + 10, width - 10, height / 2)
        canvas.create_line(width - 10 - 10, height / 2 - 10, width - 10, height / 2)

        # Draw Y-axis
        canvas.create_line(width / 2, 10, width / 2, height - 10)
        canvas.create_line(width / 2, 10, width / 2 - 10, 10 + 10)
        canvas.create_line(width / 2, 10, width / 2 + 10, 10 + 10)

        window.mainloop()  # Create an event loop


MainGUI()
