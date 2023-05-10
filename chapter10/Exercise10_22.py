# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Sudoku solutions) The complete solution for the Sudoku problem is
given in Supplement III.A. Write a GUI program that enables the user to enter a
Sudoku puzzle and click the Solve button to display a solution, as shown in
Figure 10.26.'''

from tkinter import *  # Import tkinter
from Sudoku import isValidGrid  # Import isValid
from Sudoku import search  # Import search
import tkinter.messagebox  # Import tkinter.messagebox


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Sudoku")  # Set title

        frame = Frame(window)  # Hold entries
        frame.pack()

        self.cells = []  # A list of variables tied to entries
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(StringVar())

        self.entries = []
        for i in range(9):
            self.entries.append([])
            for j in range(9):
                self.entries[i].append(Entry(frame, width=2, justify=RIGHT,
                                             textvariable=self.cells[i][j]))
                self.entries[i][j].grid(row=i, column=j)

        frame1 = Frame(window)  # Hold buttons
        frame1.pack()
        Button(frame1, text="Solve", command=self.solve).pack(side=LEFT)
        Button(frame1, text="Clear", command=self.clear).pack(side=LEFT)

        window.mainloop()  # Create an event loop

    def solve(self):
        for i in range(9):
            for j in range(9):
                if len(self.cells[i][j].get().strip()) != 0:
                    self.entries[i][j]["bg"] = "gray"

        # Get the numbers from the entries
        values = []
        for i in range(9):
            values.append([])
            for j in range(9):
                if len(self.cells[i][j].get().strip()) == 0:
                    values[i].append(0)
                else:
                    values[i].append(int(self.cells[i][j].get()))

        if not isValidGrid(values):
            tkinter.messagebox.showinfo("Sudoku", "Invalid input")
        elif search(values):
            print("found")
            # Put values back to the cells
            for i in range(9):
                for j in range(9):
                    print(values[i][j])
                    self.cells[i][j].set(str(values[i][j]))
        else:
            tkinter.messagebox.showinfo("Sudoku", "No solution")

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].set("")
                self.entries[i][j]["bg"] = "white"


MainGUI()

