# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: Count the occurrences of each letter) Rewrite Listing 14.5 using a GUI
program to let the user enter the URL from an entry field, as shown in Figure 14.5.
Clicking the Show Result button displays the result in a text widget. You need to
display a message in a message box if the URL does not exist.'''

from tkinter import *  # Import tkinter
import tkinter.messagebox  # Import tkinter.messagebox
import urllib.request


def showResult():
    analyzeFile(url.get())


def analyzeFile(url):
    try:
        input = urllib.request.urlopen(url)
        s = str(input.read().decode())  # Read the content as string from the URL

        counts = countLetters(s.lower())

        # Display results
        for i in range(len(counts)):
            if counts[i] != 0:
                text.insert(END, chr(ord('a') + i) + " appears  " + str(counts[i])
                            + (" time" if counts[i] == 1 else " times") + "\n")

        input.close()  # Close file
    except ValueError:
        tkinter.messagebox.showwarning("Analyze URL",
                                       "URL " + url + " does not exist")

    # Count each letter in the string


def countLetters(s):
    counts = 26 * [0]  # Create and initialize counts
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
    return counts





window = Tk()  # Create a window
window.title("Occurrence of Letters from URL")  # Set title

frame1 = Frame(window)  # Hold four labels for displaying cards
frame1.pack()

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(frame1, width=60, height=10, wrap=WORD,
            yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)

frame2 = Frame(window)  # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text="Please enter a URL: ").pack(side=LEFT)
url = StringVar()
Entry(frame2, width=50, textvariable=url).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
