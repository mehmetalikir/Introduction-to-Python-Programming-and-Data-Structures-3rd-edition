# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display a running fan) Write a program that displays a fan running, as shown in
Figure 11.17a'''

from tkinter import *  # Import tkinter

width = 200
height = 200
radius = 80


class ARunningFan:
    def __init__(self):
        self.window = Tk()  # Create a window
        self.window.title("Fan")  # Set a title

        self.canvas = Canvas(self.window, bg="white", width=width, height=height)
        self.canvas.pack()

        self.window.protocol("WM_DELETE_WINDOW", self.quit)  # Handle window closed event

        self.startingAngle = 0
        self.isContinue = True
        while self.isContinue:  # Exit when window is closed
            self.startingAngle += 5
            self.displayFan(self.startingAngle)
            self.canvas.after(100)  # Sleep for 100 milliseconds
            self.canvas.update()

        self.window.mainloop()  # Create an event loop

    def displayFan(self, startingAngle):
        self.canvas.delete("fan")

        self.canvas.create_arc(width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius,
                               start=self.startingAngle + 0, extent=30, fill="red", tags="fan")

        self.canvas.create_arc(width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius,
                               start=self.startingAngle + 90, extent=30, fill="red", tags="fan")

        self.canvas.create_arc(width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius,
                               start=self.startingAngle + 180, extent=30, fill="red", tags="fan")

        self.canvas.create_arc(width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius,
                               start=self.startingAngle + 270, extent=30, fill="red", tags="fan")

    def quit(self):
        self.isContinue = False
        self.window.destroy()


ARunningFan()

