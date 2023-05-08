# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: display a checkerboard) Write a program that displays a checkerboard in
which each white and black cell is a canvas with a background of black or white,
as shown in Figure 10.19a.'''
from random import randint
from tkinter import *  # Import tkinter


class Checkerboard:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("A Checkerboard")  # Set a title

        imageWhite = PhotoImage(file="image/white.gif")
        imageBrown = PhotoImage(file="image/brown.gif")

        for i in range(8):
            frame = Frame(window)
            frame.pack()
            for j in range(8):
                label = Label(frame, image=imageWhite if j % 2 == 0 else imageBrown)
                label.pack(side=LEFT if i % 2 == 0 else RIGHT)  # Mehmeteous assignment

        window.mainloop()  # Create an event loop


Checkerboard()  # Create GUI
