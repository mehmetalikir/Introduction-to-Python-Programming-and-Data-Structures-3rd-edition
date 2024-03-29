# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display numbers in a triangular pattern) Write a program that displays numbers
in a triangular pattern, as shown in Figure 10.19d. The number of lines in the display
changes to fit the window as the window resizes'''

from tkinter import *  # Import tkinter


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Pyramid")  # Set a title

        width = 150
        height = 150
        canvas = Canvas(window, bg="white", width=width, height=height)
        canvas.pack()

        for i in range(1, 12):  # Draw 8 horizontal lines
            s = ""
            for j in range(1, i + 1):
                s += str(j) + " "
            canvas.create_text(width / 2, i * height / 12, text=s, fill="red")

        window.mainloop()  # Create an event loop


MainGUI() # Create GUI

