# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Merge animation) Write a program that animates the merge of two sorted lists.
Create two lists, list1 and list2, each of which consists of 8 random numbers
from 1 to 999. The array elements are displayed, as shown in Figure 17.5.
Clicking the Next button causes the program to move an element from list1 or
list2 to temp. Clicking the Reset button creates two new random lists for
a new start.'''

import random
import tkinter.messagebox
from tkinter import *

width = 340
height = 150


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Merge Animation")  # Set title

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        Button(frame, text="Next", command=self.step).pack(side=LEFT)
        Button(frame, text="Reset", command=self.reset).pack(side=LEFT)

        self.list1 = [random.randint(1, 999) for _ in range(8)]
        self.list2 = [random.randint(1, 999) for _ in range(8)]
        self.temp = []
        self.i = 0

        self.drawAStep()

        window.mainloop()  # Create an event loop

    def reset(self):
        self.list1 = [random.randint(1, 999) for _ in range(8)]
        self.list2 = [random.randint(1, 999) for _ in range(8)]
        self.temp = []
        self.i = 0
        self.drawAStep()

    def step(self):
        if self.i < 8:
            if len(self.list1) > 0 and len(self.list2) > 0:
                if self.list1[0] < self.list2[0]:
                    self.temp.append(self.list1.pop(0))
                else:
                    self.temp.append(self.list2.pop(0))
            elif len(self.list1) > 0:
                self.temp.extend(self.list1)
                self.list1.clear()
            elif len(self.list2) > 0:
                self.temp.extend(self.list2)
                self.list2.clear()
            self.i += 1
            self.drawAStep()
        else:
            tkinter.messagebox.showinfo("Merge Complete", "The two lists have been merged.")

    def drawAStep(self):
        self.canvas.delete("line")
        self.canvas.create_text(width // 2, height // 2, text="list1: " + str(self.list1), tag="line")
        self.canvas.create_text(width // 2, height // 2 + 20, text="list2: " + str(self.list2), tag="line")
        self.canvas.create_text(width // 2, height // 2 + 40, text="temp: " + str(self.temp), tag="line")


MainGUI()
