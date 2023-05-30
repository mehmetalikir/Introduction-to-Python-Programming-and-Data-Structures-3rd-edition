# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: Count the occurrences of each letter) Revise the preceding exercise to
display a histogram for the result, as shown in Figure 14.6. You need to display a
message in a message box if the URL does not exist.'''

import tkinter.messagebox  # Import tkinter.messagebox
import urllib.request
from tkinter import *  # Import tkinter


def showResult():
    analyzeFile(url.get())


def analyzeFile(url):
    try:
        input = urllib.request.urlopen(url)
        s = str(input.read().decode())  # Read the content as string from the URL

        counts = countLetters(s.lower())

        # Display results in a histogram
        histogram(counts)

        input.close()  # Close file
    except ValueError:
        tkinter.messagebox.showwarning("Analyze URL",
                                       "URL " + url + " does not exist")


def histogram(counts):
    numberOfBars = len(counts)
    width = int(canvas["width"])
    height = int(canvas["height"])
    heightBar = 0.75 * height
    widthBar = width - 20
    maxCounts = max(counts)
    barWidth = (width - 20) / len(counts)
    bottomGap = 10
    maxCount = int(max(counts))

    for i in range(numberOfBars):
        canvas.create_rectangle(i * widthBar / numberOfBars + 10, height - 20 - counts[i] * heightBar / maxCounts,
                                (i + 1) * widthBar / numberOfBars + 10, height - 20)
        canvas.create_text(i * barWidth + 10 + barWidth / 2,
                           (height - bottomGap) * (1 - counts[i] / (maxCount + 4)) - 8,
                           text=str(counts[i]))
        canvas.create_text(i * widthBar / numberOfBars + 10 + 0.5 * widthBar / numberOfBars, height - 10,
                           text=chr(i + ord('a')))


# Count each letter in the string
def countLetters(s):
    counts = 26 * [0]  # Create and initialize counts
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
    return counts


window = Tk()  # Create a window
window.title("Occurrence of Letters in a Histogram from URL")  # Set title

frame1 = Frame(window)  # Hold four labels for displaying cards
frame1.pack()
canvas = Canvas(frame1, width=500, height=200)
canvas.pack()

frame2 = Frame(window)  # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text="Enter a URL: ").pack(side=LEFT)
url = StringVar()
Entry(frame2, width=50, textvariable=url).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
