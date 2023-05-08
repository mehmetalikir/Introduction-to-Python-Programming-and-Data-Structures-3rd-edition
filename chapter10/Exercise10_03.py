# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Select geometric figures) Write a program that draws a rectangle or an oval, as
shown in Figure 10.17. The user selects a figure from a radio button and specifies
whether it is filled by selecting a check button.'''

from tkinter import *  # Import tkinter


class GeometricFigures:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Select Geometric Figures")  # Set a title

        # Place self.canvas in the window
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        # Place buttons in frame
        frame = Frame(window)
        frame.pack()

        # Add two radio button and a check button to frame
        self.v1 = IntVar()  # Create an IntVar bound with rbRectangle and rbOval
        rbRectangle = Radiobutton(frame, text="Rectangle",
                                  variable=self.v1, value=1, command=self.processRadioButton)  # Call processRadioButton
        rbOval = Radiobutton(frame, text="Oval",
                             variable=self.v1, value=2, command=self.processRadioButton)
        self.v2 = IntVar()  # Create an IntVar bound with cbtFilled
        chtFilled = Checkbutton(frame, text="Filled",
                                variable=self.v2, command=self.processCheckButton)  # Call processCheckButton

        # Assign values to grid
        rbRectangle.grid(row=1, column=1)
        rbOval.grid(row=1, column=2)
        chtFilled.grid(row=1, column=3)

        mainloop()  # Create an event loop

    # Display a rectangle or an oval
    def processRadioButton(self):
        if self.v1.get() == 1:
            self.canvas.create_rectangle(10, 10, 190, 90, fill=self.processCheckButton())
        else:
            self.canvas.create_oval(10, 10, 190, 90, fill=self.processCheckButton())

    # Return filled color
    def processCheckButton(self):
        if self.v2.get() == 1:
            return "violet"
        else:
            return ""


GeometricFigures()  # Create GUI
