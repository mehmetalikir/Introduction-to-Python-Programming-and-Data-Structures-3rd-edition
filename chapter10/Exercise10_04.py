# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display circles) Write a program that displays 20 circles, as shown in Figure 10.18.'''

from tkinter import *  # Import tkinter


class DisplayCircles:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Display Circles")  # Set a title

        frame = Frame(window)
        frame.pack()

        # Place self.canvas in the window
        self.canvas = Canvas(frame, width=800, height=800, bg="white")
        self.canvas.pack()

        for i in range(20):
            self.displayCricles(i)

        window.mainloop()  # Create an event loop

    # Display circles
    def displayCricles(self, i):
        self.canvas.create_oval(190 - i * 5, 110 - i * 5, 220 + i * 5, 140 + i * 5,
                                outline="#000", width=1.5)


DisplayCircles()  # Create GUI
