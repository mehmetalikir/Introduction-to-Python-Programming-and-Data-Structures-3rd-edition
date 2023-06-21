# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Revise Listing 22.12, NineTail.py) The program in Listing 22.12 lets the user
enter an input for the nine tail program form the console and displays the result
on the console, Write a GUI program that lets user set an initial state of the
nine coins(see Figure 22.21a) and click the Solve button to display the solution,
as shown in Figure 22.21b. Initially, the user can click the mouse button to flip a
coin'''

from tkinter import *
from NineTail import NineTail


class NineCoinsGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Nine Coins")

        self.buttons = []
        self.solution_label = None

        self.nine_tail = NineTail()

        self.create_grid()
        self.create_solve_button()
        self.create_solution_label()

        self.window.mainloop()

    def create_grid(self):
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = Button(self.window, width=5, height=2, command=lambda i=i, j=j: self.flip_coin(i, j))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def create_solve_button(self):
        solve_button = Button(self.window, text="Solve", command=self.solve)
        solve_button.grid(row=3, column=1)

    def create_solution_label(self):
        self.solution_label = Label(self.window, text="")
        self.solution_label.grid(row=4, column=0, columnspan=3)

    def flip_coin(self, i, j):
        self.nine_tail.flip_coin(i, j)
        self.update_grid()

    def update_grid(self):
        for i in range(3):
            for j in range(3):
                if self.nine_tail.get_coin(i, j):
                    self.buttons[i][j].config(text="H")
                else:
                    self.buttons[i][j].config(text="T")

    def solve(self):
        result = self.nine_tail.solve()
        if result is None:
            self.solution_label.config(text="No solution found.")
        else:
            self.solution_label.config(text="Solution: " + result)


NineCoinsGUI()
