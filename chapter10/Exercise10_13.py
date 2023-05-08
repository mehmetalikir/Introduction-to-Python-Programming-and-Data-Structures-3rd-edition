# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Buttons and radio buttons) Write a program that uses radio buttons to select
background colors for text, as shown in Figure 10.21c. The available colors are
red, yellow, white, gray, and green. The program uses the buttons <= and => to
move the left or right'''

from tkinter import *  # Import tkinter


class MainGUI:

    def __init__(self):
        window = Tk()  # Create a window
        window.title("Radio buttons and buttons")

        # Add radio buttons to frame
        frame = Frame(window)
        frame.pack()

        # Create IntVars bound with colors
        self.v1 = IntVar()
        rbRed = Radiobutton(frame, text="Red", variable=self.v1, value=1, command=self.processRadioButton)
        rbYellow = Radiobutton(frame, text="Yellow", variable=self.v1, value=2, command=self.processRadioButton)
        rbWhite = Radiobutton(frame, text="White", variable=self.v1, value=3, command=self.processRadioButton)
        rbGray = Radiobutton(frame, text="Gray", variable=self.v1, value=4, command=self.processRadioButton)
        rbGreen = Radiobutton(frame, text="Green", variable=self.v1, value=5, command=self.processRadioButton)

        # Assign values to grid
        rbRed.grid(row=1, column=1)
        rbYellow.grid(row=1, column=2)
        rbWhite.grid(row=1, column=3)
        rbGray.grid(row=1, column=4)
        rbGreen.grid(row=1, column=5)

        # Place self.canvas in the window
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        # Place buttons in the window
        btLeft = Button(window, text="<=", command=self.displayString)
        btLeft.pack()
        btRight = Button(window, text="=>", command=self.displayString)
        btRight.pack()
        window.mainloop()  # Create an event loop

    def processRadioButton(self):
        self.canvas.create_rectangle(10, 10, 190, 90, fill=self.getColor())

    # Display a string
    def displayString(self):
        self.canvas.create_text(100, 50, text="welcome")


    # Get color
    def getColor(self):
        if self.v1.get() == 1:
            return "red"
        elif self.v1.get() == 2:
            return "yellow"
        elif self.v1.get() == 3:
            return "white"
        elif self.v1.get() == 4:
            return "gray"
        else:
            return "green"


MainGUI()  # Create GUI
