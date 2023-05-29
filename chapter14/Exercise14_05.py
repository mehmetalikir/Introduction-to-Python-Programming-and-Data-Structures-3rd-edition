# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: Count the occurrences of each letter) Revise the preceding exercise to
display a histogram for the result, as shown in Figure 14.4. You need to display a
message in a message box if the file does not exist.'''


from tkinter import *  # Import tkinter
import tkinter.messagebox  # Import tkinter.messagebox
from tkinter.filedialog import askopenfilename


width = 340
height = 150
i = -1 # current index
def showResult():
    analyzeFile(filename.get())


def analyzeFile(filename):
    try:
        inputFile = open(filename, "r")  # Open the file

        counts = 26 * [0]  # Create and initialize counts
        for line in inputFile:
            # Invoke the countLetters function to count each letter
            countLetters(line.lower(), counts)


        # Display histogram
        maxCount = max(counts)
        normalizedCounts = [count / maxCount for count in counts]
        bottomGap = 10
        barWidth = (width - 20) / len(counts)

        for i in range(len(normalizedCounts)):
            if counts[i] != 0:
                canvas.create_rectangle(i * barWidth + 10, (height - bottomGap) * (1 - counts[i] / (maxCount + 4)),
                                        (i + 1) * barWidth + 10, height - bottomGap, tag="line")
                canvas.create_text(i * barWidth + 10 + barWidth / 2,
                                   (height - bottomGap) * (1 - counts[i] / (maxCount + 4)) - 8,
                                   text=str(counts[i]), tag="line")

        inputFile.close()  # Close file
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



window = Tk()  # Create a window
window.title("Occurrence of Letters")  # Set title

frame1 = Frame(window)  # Hold four labels for displaying cards
frame1.pack()

canvas = Canvas()
canvas.pack()

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(frame1, width=40, height=10, wrap=WORD,
            yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)

frame2 = Frame(window)  # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text="Please enter a filename: ").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text="Browse", command=openFile).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
