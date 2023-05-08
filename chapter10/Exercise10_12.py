# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display a still fan) Write a program that displays a still fan, as shown in Figure
10.21b'''
from tkinter import *  # Import tkinter


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Fan")  # Set a title

        # Constant
        WIDTH = 200
        HEIGHT = 200
        RADIUS = 80

        canvas = Canvas(window, bg="white", width=WIDTH, height=HEIGHT)
        canvas.pack()

        angle = 0
        while angle <= 270:
            canvas.create_arc(WIDTH / 2 - RADIUS, HEIGHT / 2 - RADIUS, WIDTH / 2 + RADIUS, HEIGHT / 2 + RADIUS,
                              start=angle, extent=30, fill="red", tags="fan")
            angle += 90

        window.mainloop()  # Create an event loop


MainGUI()  # Create GUI
