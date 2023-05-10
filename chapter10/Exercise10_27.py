# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Plot the square function) Exercise 5.54 draws a square function. Rewrite the
program to draw the square function using Tkinter, as shown in Figure 10.29b.'''
from tkinter import *  # Import tkinter


class MainGUI:

    def __init__(self):
        window = Tk()  # Create a window
        window.title("Square Function")  # Set title

        width = 400
        height = 150
        canvas = Canvas(window, width=width, height=height)
        canvas.pack()

        # Draw square function
        p = []
        for x in range(-100, 100):
            p.append([x + width / 2, -0.0125 * x * x + height / 2]) # Danieleus Assigment

        for i in range(len(p) - 1):
            canvas.create_line(p[i], p[i + 1])

        # Draw X-axis
        canvas.create_text(width - 10 - 10, height / 2 + 10, text="x")
        canvas.create_line(10, height / 2, width - 10, height / 2)
        canvas.create_line(width - 10 - 10, height / 2 + 10, width - 10, height / 2)
        canvas.create_line(width - 10 - 10, height / 2 - 10, width - 10, height / 2)

        # Draw Y-axis
        canvas.create_text(width / 2, height / 2 - 50, text="y")
        canvas.create_line(width / 2, 10, width / 2, height - 10)
        canvas.create_line(width / 2, 10, width / 2 - 10, 10 + 10)
        canvas.create_line(width / 2, 10, width / 2 + 10, 10 + 10)

        window.mainloop()  # Create an event loop


MainGUI()  # Call the main function
