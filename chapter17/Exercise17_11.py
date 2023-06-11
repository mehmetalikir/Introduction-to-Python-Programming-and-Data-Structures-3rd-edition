# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Quick sort partition animation) Write a program that animates the partition for
a quick sort. The program creates a list that consists of 20 random numbers from
1 to 999. The list is displayed, as shown in Figure 17.7. Clicking the Step button
causes the program to move low to the right or high to the left, or swap the
elements at low and high. Clicking the Reset button creates a new list of random
numbers for a new start. When the algorithm is finished, clicking the Step button
displays a message to inform the user.'''

from tkinter import *
import tkinter.messagebox
import random

width = 340
height = 150
barWidth = 15
bottomGap = 10


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Quick Sort Partition Animation")  # Set title

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        Button(frame, text="Step", command=self.step).pack(side=LEFT)
        Button(frame, text="Reset", command=self.reset).pack(side=LEFT)

        self.list = [random.randint(1, 999) for _ in range(20)]
        self.reset()
        self.pivot = 0
        self.low = 1
        self.high = len(self.list) - 1

        self.drawAStep()

        window.mainloop()  # Create an event loop

    def reset(self):
        self.pivot = 0
        self.low = 1
        self.high = len(self.list) - 1
        random.shuffle(self.list)
        self.drawAStep()

    def step(self):
        if self.low > self.high:
            tkinter.messagebox.showinfo("Partition Complete", "The partition step is complete.")
            return

        if self.list[self.low] <= self.list[self.pivot]:
            self.low += 1
        elif self.list[self.high] > self.list[self.pivot]:
            self.high -= 1
        else:
            self.swap(self.low, self.high)

        self.drawAStep()

    def swap(self, i, j):
        self.list[i], self.list[j] = self.list[j], self.list[i]

    def drawAStep(self):
        self.canvas.delete("line")
        self.canvas.create_text(width // 2, height // 2, text="List: " + str(self.list), tag="line")

        for i, num in enumerate(self.list):
            x0 = i * barWidth + 10
            y0 = height - bottomGap
            x1 = x0 + barWidth
            y1 = y0 - num
            fill = "white"
            if i == self.pivot:
                fill = "red"
            elif i == self.low:
                fill = "yellow"
            elif i == self.high:
                fill = "green"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, tag="line")

        self.canvas.update()

    def partition(self, low, high):
        pivot = self.list[low]  # Choose the first element as the pivot
        j = low + 1

        while j <= high:
            if self.list[j] <= pivot:
                self.low += 1
                self.swap(j, self.low)
            j += 1

        self.swap(low, self.low)
        return self.low


MainGUI()

