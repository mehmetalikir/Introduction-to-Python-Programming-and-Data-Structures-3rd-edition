# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display a GO sign) Write a program that displays a GO sign, as shown in Figure
10.30a. The hexagon is in dark green and the text is in white'''

import math
from tkinter import *  # Import tkinter


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Go Sign")  # Set title

        width = 200
        height = 150
        canvas = Canvas(window, bg="white", width=width, height=height)
        canvas.pack()

        xCenter = width / 2
        yCenter = height / 2
        radius = min(width, height) * 0.4

        # Create a Polygon object
        polygon = []

        # Add points to the polygon
        for i in range(6):
            polygon.append([xCenter + radius *
                            math.cos(i * 2 * math.pi / 6 + 2 * math.pi / 12), yCenter - radius *
                            math.sin(i * 2 * math.pi / 6 + 2 * math.pi / 12)])

        # Draw the polygon
        canvas.create_polygon(polygon, fill="darkgreen", outline='black')
        canvas.create_text(xCenter, yCenter, text="GO", font="Sans 25 bold", fill="white")

        window.mainloop()  # Create an event loop


MainGUI()
