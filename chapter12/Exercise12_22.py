# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(On-Off switches) Write a program that displays on(1) or off(0) for each of nine
switches, as shown in Figure 12.32a–b. When a cell is clicked, the switch is off
and vice versa. Write a custom cell class that extends Label. In the initializer
of the class, bind the event <Button-1> with the method for flipping the switch.
When the program starts, all cells initially display 1.'''

from tkinter import *  # Import tkinter

class Cell(Label):
    def __init__(self, container, text):
        Label.__init__(self, container,
                       text=text, font="Helvetica 30 bold", fg="darkgreen")
        self.bind("<Button-1>", self.onoff)

    def onoff(self, event):
        if self["text"] == "1":
            self["text"] = "0"
            self["fg"] = "red"
        else:
            self["text"] = "1"
            self["fg"] = "darkgreen"

class MainClass:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("On-Off switches")  # Set title

        frame = Frame(window)
        frame.pack()

        for i in range(3):
            for j in range(3):
                Cell(frame, text="1").grid(row=i, column=j)

        window.mainloop()  # Create an event loop

MainClass()