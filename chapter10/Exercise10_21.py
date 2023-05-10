# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: the 24-point card game) The 24-point card game involves picking any four
cards from 52 cards, as shown in Figure 10.25. Note that the jokers are excluded. Each
card represents a number. An ace, king, queen, and jack represent 1, 13, 12, and 11,
respectively. Enter an expression that uses the four numbers from the four selected
cards. Each card number can be used only once in each expression, and each card
must be used. You can use the operators ( +,-, *, and /) and parentheses in the
expression. The expression must evaluate to 24. After entering the expression, click
the Verify button to check whether the numbers in the expression are currently selected
and whether the result of the expression is correct. Display the verification in a dialog
box. You can click the Refresh button to get another set of four cards. Assume that
images are stored in files named 1.gif, 2.gif, ..., 52.gif, in the order of spades, hearts,
diamonds, and clubs. So, the first 13 images are for spades 1, 2, 3, ..., and 13.'''
import tkinter.messagebox
from random import shuffle
from tkinter import *  # Import tkinter


class MainGUI:

    def __init__(self):
        window = Tk()  # Create a window
        window.title("24-Point Game")  # Set a title
        frame = Frame(window)  # Hold four labels for cards
        frame.pack()

        self.imageList = []  # Store images for cards
        for i in range(1, 53):
            self.imageList.append(PhotoImage(file="image/cards/"
                                                  + str(i) + ".png"))

        self.labelList = []  # A list of four labels

        for i in range(4):
            self.labelList.append(Label(frame,
                                        image=self.imageList[i]))
            self.labelList[i].pack(side=LEFT)

        Button(window, text="Refresh", command=self.refresh).pack()

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text="Please enter an expression").pack(side=LEFT)
        self.expression = StringVar()
        Entry(frame1, textvariable=self.expression).pack(side=LEFT)
        Button(frame1, text="Verify", command=self.verify).pack(side=RIGHT)  # Verify

        window.mainloop()  # Create an event loop

    # Choose four random cards
    def refresh(self):
        # Assign value
        self.calculateCardValues = 0

        shuffle(self.imageList)  # Shuffle list
        for i in range(4):
            self.labelList[i]["image"] = self.imageList[i]

            self.calculateCardValues = 0

    def verify(self):
        # Assign value
        calculateEntryValues = 0

        # Get the input from the entry
        entryValue = str(self.expression.get())

        if calculateEntryValues == self.calculateCardValues:
            tkinter.messagebox.showinfo("Correct", "You'Ve Got It")
        else:
            tkinter.messagebox.showerror("Incorrect", "Please ty it again")


MainGUI()  # Create GUI
