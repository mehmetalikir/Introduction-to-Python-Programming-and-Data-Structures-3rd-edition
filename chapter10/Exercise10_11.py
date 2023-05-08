# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display a clock) Write a program that displays a clock to show the current time,
as shown in Figure 10.21a. To obtain the current time, use the datetime class in
Section 9.4, "Using Classes from the Python Library: the datetime Class."'''

from tkinter import *  # Import tkinter
from datetime import datetime


class Clock:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Clock")  # Set a title

        WIDTH = 200
        HEIGHT = 200
        RADIUS = 80

        canvas = Canvas(window, bg="white", width=WIDTH, height=HEIGHT)
        canvas.pack()

        canvas.create_arc(WIDTH / 2 - RADIUS, HEIGHT / 2 - RADIUS, WIDTH / 2 + RADIUS, HEIGHT / 2 + RADIUS,
                          start=-1, extent=359, outline="black", tags="clock")
        canvas.create_text(WIDTH, HEIGHT/2, text="3")
        canvas.create_text(WIDTH/2, HEIGHT, text="6")


        frame = Frame(window)
        frame.pack()
        time = datetime.now().strftime("%T")
        Label(frame, text=time).grid(row=1,column=1)
        window.mainloop()  # Create an event loop


Clock()  # Create GUI
