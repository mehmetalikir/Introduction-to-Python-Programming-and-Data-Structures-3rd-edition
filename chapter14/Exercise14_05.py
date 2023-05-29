# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: Count the occurrences of each letter) Revise the preceding exercise to
display a histogram for the result, as shown in Figure 14.4. You need to display a
message in a message box if the file does not exist.'''

import tkinter.messagebox  # Import tkinter.messagebox
from tkinter import *  # Import tkinter
from tkinter.filedialog import askopenfilename


def showResult():
    analyzeFile(filename.get())


def analyzeFile(filename):
    try:
        inputFile = open(filename, "r")  # Open the file

        counts = 26 * [0]  # Create and initialize counts
        for line in inputFile:
            # Invoke the countLetters function to count each letter
            countLetters(line.lower(), counts)
        inputFile.close()  # Close file

        # Display a histogram for counts
        histogram(counts)
    except IOError:
        tkinter.messagebox.showwarning("Analyze File",
                                       "File " + filename + " does not exist")


# Count each letter in the string
def countLetters(line, counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1


def openFile():
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)


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


window = Tk()  # Create a window
window.title("Occurrence of Letters Histogram")  # Set title

frame1 = Frame(window)  # Hold four labels for displaying cards
frame1.pack()
canvas = Canvas(frame1, width=500, height=200)
canvas.pack()

frame2 = Frame(window)  # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text="Please enter a filename: ").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=40, textvariable=filename).pack(side=LEFT)
Button(frame2, text="Browse", command=openFile).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
