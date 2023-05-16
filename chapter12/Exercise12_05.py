# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

''''''

from random import *  # Import random
from tkinter import *  # Import tkinter


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("TicTacToe")  # Set a title

        # Assign values
        imageX = PhotoImage(file="image/x.gif")
        imageO = PhotoImage(file="image/o.gif")

        for i in range(3):
            frame = Frame(window)
            frame.pack()
            for j in range(3):
                label = Label(frame, image=imageX if randrange(0, 2) == 0 else imageO)
                label.pack(side=LEFT)

        window.mainloop()  # Create an event loop


MainGUI()  # Create GUI
