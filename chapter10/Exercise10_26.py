# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Draw a polygon) Write a program that prompts the user to enter the
coordinates of six points and fills the polygon that connects the points, as
shown in Figure 10.29a. Note that you can draw a polygon using
canvas.create_polygon(points), where points are a two-dimensional list that
stores the x- and y-coordinates of the points'''
from tkinter import *  # Import tkinter


class MainGUI:
    def __init__(self):
        coordinates = input("Enter coordinates for six points separated by spaces: ")
        c = coordinates.split()
        points = [[float(c[i]), float(c[i + 1])] for i in range(0, len(c), 2)] # Separate x and y cords

        window = Tk()  # Create a window
        window.title("Polygon")  # Set title

        width = 400
        height = 250
        canvas = Canvas(window, width=width, height=height)
        canvas.pack()

        canvas.create_polygon(points)

        window.mainloop()  # Create an event loop


MainGUI()
