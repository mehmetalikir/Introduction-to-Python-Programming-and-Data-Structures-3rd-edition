# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: display a tic-tac-toe board ) Write a program that displays nine labels.
Each label may display an image icon for an X or an image icon for an O, as
shown in Figure 10.19b. What to display is randomly decided. Use the
random.randrange(0, 2) function to generate an integer 0 or 1, which corresponds
to displaying a cross image (X) icon or a not image (O) icon. The cross and
not images are in the files x.gif and o.gif.'''

from tkinter import *  # Import tkinter
from random import *  # Import random


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
