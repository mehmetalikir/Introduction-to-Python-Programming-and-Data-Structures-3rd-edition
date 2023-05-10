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
from random import randint
from tkinter import *  # Import tkinter


class MainGUI:

    def __init__(self):
        window = Tk()  # Create a window
        window.title("24-Point Game")  # Set a title

        img = PhotoImage(file=f"image/cards/{randint(1, 52)}.png")
        Label(window, image=img).grid(row=1, column=1)
        img1 = PhotoImage(file=f"image/cards/{randint(1, 52)}.png")
        Label(window, image=img1).grid(row=1, column=2)
        img2 = PhotoImage(file=f"image/cards/{randint(1, 52)}.png")
        Label(window, image=img2).grid(row=1, column=3)
        img3 = PhotoImage(file=f"image/cards/{randint(1, 52)}.png")
        Label(window, image=img3).grid(row=1, column=4)

        Label(window, text="Enter an expression").grid(row=2, column=1)

        self.expression = StringVar()
        Entry(window, textvariable=self.expression).grid(row=2, column=2)

        Button(window, text="Verify", command=self.computeExpression).grid(row=2, column=4, sticky=E)

        window.mainloop()  # Create an event loop

    def refresh(self):
        pass

    def computeExpression(self):
        pass



MainGUI()  # Call the main function
