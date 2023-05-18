# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: the 24-point card game) Enhance Exercise 10.21 to enable the computer
to display the expression for a 24-point game solution if one exists, as
shown in Figure 12.27. Otherwise, report that the solution does not exist.'''

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
        shuffle(self.imageList)  # Shuffle list
        for i in range(4):
            self.labelList[i]["image"] = self.imageList[i]

    def verify(self):
        # Get the input from the entry
        self.entryValue = eval(self.expression.get())



MainGUI()  # Create GUI
