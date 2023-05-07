# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Move the square) Write a program that moves a square in a panel. You should define a
panel class for displaying the square and provide the methods for moving the square
left, right, up, and down, as shown in Figure 10.16a. Check the boundaries to prevent
the square from moving out of sight completely.'''

from tkinter import *  # Import tkinter


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Move the square")  # Set title

        # Place self.canvas in the window
        self.canvas = Canvas(window, width=400, height=200,
                             bg="white")
        self.canvas.pack()

        # Create the square
        a = 50
        self.square = self.canvas.create_rectangle(a, a, a, a, fill="blue")

        # Place buttons in frame
        frame = Frame(window)
        frame.pack()

        btLeft = Button(frame, text="Left",
                        command=self.moveLeft)
        btLeft.pack(side=LEFT)

        btRight = Button(frame, text="Right",
                         command=self.moveRight)
        btRight.pack(side=RIGHT)

        btUp = Button(frame, text="Up",
                      command=self.moveUp)
        btUp.pack(side=TOP)

        btDown = Button(frame, text="Down",
                        command=self.moveDown)
        btDown.pack(side=BOTTOM)

        window.mainloop()  # Create an event loop

    def moveLeft(self):
        self.canvas.move(self.square, 0, 100)

    def moveRight(self):
        self.canvas.move(self.square, 0, 100)

    def moveUp(self):
        self.canvas.move(self.square, 0, 100)

    def moveDown(self):
        self.canvas.move(self.square, 0, 100)


MainGUI()  # Call the main function
