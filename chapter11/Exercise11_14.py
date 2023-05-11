# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''() Write a program that'''

from tkinter import *  # Import tkinter


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("")  # Set title

        # Place self.canvas in the window
        self.canvas = Canvas(window, width=400, height=200,
                             bg="white")
        self.canvas.pack()

        # Create object
        self.object = self.canvas.create_object

        # Place buttons in frame
        frame = Frame(window)
        frame.pack()

        Button(frame, text="", command=self.function).pack(side=LEFT)

        window.mainloop()  # Create an event loop

    def function(self):
        self.canvas.does()


MainGUI()  # Call the main function
