# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display histograms) Write a program that generates 1,000 lowercase letters randomly,
counts the occurrence of each letter, and displays a histogram for the
occurrences, as shown in Figure 10.24c.'''

from tkinter import *  # Import tkinter
from RandomCharacter import *


def getCounts():
    counts = 26 * [0]
    for i in range(1000):
        ch = getRandomLowerCaseLetter()
        counts[ord(ch) - ord('a')] += 1
    return counts


width = 300
height = 200
radius = 2


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Count of Each Letter")  # Set title

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()
        Button(window, text="Display Histogram", command=self.displayHistogram).pack()

        window.mainloop()  # Create an event loop

    def displayHistogram(self):
        self.canvas.delete("histogram")
        counts = getCounts()
        bottomGap = 10
        self.canvas.create_line(10, height - bottomGap, width - 10, height - bottomGap)
        barWidth = (width - 20) / len(counts)
        maxCount = int(max(counts))
        for i in range(0, len(counts)):
            self.canvas.create_rectangle(i * barWidth + 10, height - (height - 10) * counts[i] / maxCount,
                                         (i + 1) * barWidth + 10, height - bottomGap, tags="histogram")

            self.canvas.create_text(i * barWidth + 10 + 10 / 2, height - bottomGap / 2,
                                    text=chr(i + ord('a')), tags="histogram")


MainGUI()
