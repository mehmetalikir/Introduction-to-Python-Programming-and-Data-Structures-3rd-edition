# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Radix sort animation) Write a program that animates the radix sort algorithm.
Create a list that consists of 20 random numbers from 0 to 1,000. Clicking the
Step button causes the program to place a number in a bucket. The number that has just
been placed is displayed in red. Once all the numbers are placed in the buckets,
clicking the Step button collects all the numbers from the buckets and moves
them back to the array. When the algorithm is finished, clicking the Step button
displays a message to inform the user. Clicking the Reset button creates a new
random list for a new start.'''

from tkinter import *
import tkinter.messagebox
import random

width = 340
height = 150
radius = 2


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Radix Sort Animation")  # Set title

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        Button(frame, text="Step", command=self.step).pack(side=LEFT)
        Button(frame, text="Reset", command=self.reset).pack(side=LEFT)

        self.list = [random.randint(0, 1000) for _ in range(20)]
        self.reset()
        self.key = 0

        self.drawAStep()

        window.mainloop()  # Create an event loop

    def reset(self):
        self.i = 0  # current index
        self.done = False
        random.shuffle(self.list)
        self.drawAStep()

    def step(self):
        if self.i > len(self.list) - 1:
            tkinter.messagebox.showinfo("showinfo", "Radix sort is complete")
            return

        if not self.done:
            # Place the number in the corresponding bucket
            key = getKey(self.list[self.i], self.key)
            self.buckets[key].append(self.list[self.i])

            self.canvas.create_rectangle(self.i * barWidth + 10,
                                         (height - bottomGap) * (1 - self.list[self.i] / (maxCount + 4)),
                                         (self.i + 1) * barWidth + 10, height - bottomGap, fill="red", tag="line")

            self.i += 1  # Increase step

            if self.i == len(self.list):
                self.done = True
                self.collectNumbers()

        else:
            self.resetBuckets()
            self.key += 1
            self.done = False
            self.i = 0

        self.drawAStep()

    def collectNumbers(self):
        k = 0  # k is an index for list
        for i in range(len(self.buckets)):
            for j in range(len(self.buckets[i])):
                self.list[k] = self.buckets[i][j]
                k += 1

    def resetBuckets(self):
        self.buckets = []
        for _ in range(10):
            self.buckets.append([])

    def drawAStep(self):
        bottomGap = 10
        self.canvas.delete("line")
        self.canvas.create_line(10, height - bottomGap, width - 10, height - bottomGap, tag="line")
        barWidth = (width - 20) / len(self.list)

        maxCount = int(max(self.list))
        for i in range(len(self.list)):
            self.canvas.create_rectangle(i * barWidth + 10, (height - bottomGap) * (1 - self.list[i] / (maxCount + 4)),
                                         (i + 1) * barWidth + 10, height - bottomGap, tag="line")

            self.canvas.create_text(i * barWidth + 10 + barWidth / 2,
                                    (height - bottomGap) * (1 - self.list[i] / (maxCount + 4)) - 8,
                                    text=str(self.list[i]), tag="line")

        if self.i >= 0:
            self.canvas.create_rectangle(self.i * barWidth + 10,
                                         (height - bottomGap) * (1 - self.list[self.i] / (maxCount + 4)),
                                         (self.i + 1) * barWidth + 10, height - bottomGap, fill="red", tag="line")


def radixSort(numbers, numberOfDigits):
    """Sort the int array list. numberOfDigits is the number of digits
       in the largest number in the list."""
    buckets = []
    for i in range(10):
        buckets.append([])

    for position in range(numberOfDigits + 1):
        # Clear buckets
        for i in range(len(buckets)):
            buckets[i] = []

        # Distribute the elements from list to buckets
        for i in range(len(numbers)):
            key = getKey(numbers[i], position)
            buckets[key].append(numbers[i])

        # Now move the elements from the buckets back to list
        k = 0  # k is an index for list
        for i in range(len(buckets)):
            for j in range(len(buckets[i])):
                numbers[k] = buckets[i][j]
                k += 1


def getKey(number, position):
    """"Return the digit at the specified position.
        The last digit's position is 0."""
    result = 1
    for i in range(position):
        result *= 10

    return (number // result) % 10


MainGUI()
