# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: display a tic-tac-toe board) Revise Exercise 10.6 to display a new tic-tac-toe
board with a click of the Refresh button, as shown in Figure 10.31.'''


from tkinter import *  # Import tkinter
from random import randint


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("TicTacToe")  # Set a title

        self.imageX = PhotoImage(file="image/x.gif")
        self.imageO = PhotoImage(file="image/o.gif")

        frame = Frame(window)
        frame.pack()

        self.matrix = []
        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                self.matrix[i].append(Label(frame, image=self.imageX if randint(0, 1) == 0 else self.imageO))
                self.matrix[i][j].grid(row=i, column=j)

        frame1 = Frame(window)
        frame1.pack()
        Button(frame1, text="Refresh", command=self.refresh).pack()

        window.mainloop()  # Create an event loop

    def refresh(self):
        for i in range(3):
            for j in range(3):
                self.matrix[i][j]["image"] = self.imageX if randint(0, 1) == 0 else self.imageO


MainGUI()
