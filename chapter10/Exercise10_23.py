# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Four consecutive equal numbers) Write a GUI program for Exercise
8.19, as shown in Figure 10.27. Let the user enter the numbers in the text fields in
a grid of six rows and seven columns. The user can click the Solve button to highlight
a sequence of four equal numbers, if it exists.'''

from tkinter import *  # Import tkinter

# Constant
N = 2
C = 7


class MainGUI:

    def __init__(self):
        window = Tk()  # Create a window
        window.title("Consecutive four")  # Set title

        frame = Frame(window)  # Hold entries
        frame.pack()

        self.cells = []  # A list of variables tied to entries
        for i in range(C):
            self.cells.append([])
            for j in range(C):
                self.cells[i].append(StringVar())

        self.entries = []
        for i in range(C):
            self.entries.append([])
            for j in range(C):
                self.entries[i].append(Entry(frame, width=2, justify=RIGHT,
                                             textvariable=self.cells[i][j]))
                self.entries[i][j].grid(row=i, column=j)

        frame1 = Frame(window)  # Hold buttons
        frame1.pack()
        Button(frame1, text="Solve", command=self.solve).pack(side=LEFT)

        window.mainloop()  # Create an event loop

    def solve(self):
        a = self.entries
        # Find consecutive fours in the rows, columns, and diagonal
        for i in range(C):
            for j in range(C):
                if self.isConsecutiveFour(a, C):
                    self.entries[i][j]["bg"] = "yellow"

    # Display result
    def isConsecutiveFour(self, a, n):
        if self.isSameOnARow(a) or \
                self.isSameOnAColumn(a, n) or \
                self.isSubDiagonal(a, n) or \
                self.isMajorDiagonal(a, n):
            return True
        return False

    # Check rows
    def isSameOnARow(self, a):
        for i in range(4):
            count = 0
            for j in range(4):
                if a[i][0] == a[j]:  # Check whether row has not same values
                    count += 1
            if count == 4:
                return True
            return False

    # Check columns
    def isSameOnAColumn(self, a, n):
        # Assign value
        count = 0
        for i in range(len(a) - 1):
            for j in range(1, len(a) - 1):
                if a[0][j] == a[i + 1][j]:  # Check whether column has not same values
                    count += 1
                    if count == N:
                        return True
        return False

    # Check major diagonal
    def isMajorDiagonal(self, a, n):
        # Assign value
        count = 0
        for i in range(1, len(a) - 1):
            if a[0][0] == a[i][i]:  # Check whether major diagonal has not same values
                count += 1

        if count == N:
            return True
        return False

    # Check sub-diagonal
    def isSubDiagonal(self, a, n):
        # Assign value
        count = 0
        for i in range(1, len(a) - 1):
            if a[0][n - 1] == a[i][n - 2]:  # Check whether sub-diagonal has not same values
                count += 1

        if count == N:
            return True
        return False


MainGUI()  # Call the main function

#
# # Assign value
#
# a = ["1", "1", "1", "1",
#      "1", "1", "1", "1",
#      "1", "1", "1", "1",
#      "1", "1", "1", "1"]
#
#
# for i in range(4):
#     count = 0
#     for j in range(4):
#         if a[i][0] == a[j]:  # Check whether row has not same values
#             count += 1
#             if count == 4:
#                 print("OK")
