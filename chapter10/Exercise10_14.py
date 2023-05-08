# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Traffic lights) Write a program that simulates a traffic light. The program lets
the user select one of three lights: red, yellow, or green. When a radio button is
selected, the light is turned on, and only one light can be on at a time(see Figure
1022.a-b) No light is on when the program stars'''
from tkinter import *  # Import tkinter

WIDTH = 200
HEIGHT = 150


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Traffic Lights")  # Set title

        self.h = HEIGHT * 0.85
        self.w = self.h / 3
        self.radius = self.w * 0.9 / 2

        self.canvas = Canvas(window, bg="white", width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.displayBasic()

        frame1 = Frame(window)
        frame1.pack()

        self.v = IntVar()
        Radiobutton(frame1, text="Red",
                    variable=self.v, value=1, command=self.displayFigure).pack(side=LEFT)
        Radiobutton(frame1, text="Yellow",
                    variable=self.v, value=2, command=self.displayFigure).pack(side=LEFT)
        Radiobutton(frame1, text="Green",
                    variable=self.v, value=3, command=self.displayFigure).pack(side=LEFT)

        window.mainloop()  # Create an event loop

    def displayFigure(self):
        self.canvas.delete("light")
        self.displayBasic()

        if self.v.get() == 1:
            self.canvas.create_oval(WIDTH / 2 - self.radius, HEIGHT / 2 - self.radius - self.w, WIDTH / 2 + self.radius,
                                    HEIGHT / 2 + self.radius - self.w,
                                    fill="red", tags="light")
        elif self.v.get() == 2:
            self.canvas.create_oval(WIDTH / 2 - self.radius, HEIGHT / 2 - self.radius, WIDTH / 2 + self.radius,
                                    HEIGHT / 2 + self.radius,
                                    fill="yellow", tags="light")
        else:
            self.canvas.create_oval(WIDTH / 2 - self.radius, HEIGHT / 2 - self.radius + self.w, WIDTH / 2 + self.radius,
                                    HEIGHT / 2 + self.radius + self.w,
                                    fill="green", tags="light")

    def displayBasic(self):
        self.canvas.create_rectangle(WIDTH / 2 - self.w / 2, HEIGHT / 2 - self.h / 2,
                                     WIDTH / 2 + self.w / 2, HEIGHT / 2 + self.h / 2, tags="light")
        self.canvas.create_oval(WIDTH / 2 - self.radius, HEIGHT / 2 - self.radius, WIDTH / 2 + self.radius,
                                HEIGHT / 2 + self.radius,
                                tags="light")
        self.canvas.create_oval(WIDTH / 2 - self.radius, HEIGHT / 2 - self.radius - self.w, WIDTH / 2 + self.radius,
                                HEIGHT / 2 + self.radius - self.w,
                                tags="light")
        self.canvas.create_oval(WIDTH / 2 - self.radius, HEIGHT / 2 - self.radius + self.w, WIDTH / 2 + self.radius,
                                HEIGHT / 2 + self.radius + self.w,
                                tags="light")


MainGUI() # Create GUI
