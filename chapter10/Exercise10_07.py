# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display old TV bars) Write a program that displays 7 vertical-colored bars as
shown in Figure 10.19c. Use white, yellow, cyan, green, magenta, red, and blue
colors for bars'''

from tkinter import *  # Import tkinter


class TVBars:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Old TV Bars")  # Set a title

        frame = Frame(window)
        frame.pack()

        canvas = Canvas(frame, width=400, height=400, bg="white")
        canvas.pack()


        for i in range(8):
            canvas.create_line(16 * i, 0 , 16 * i, 128, fill="red")
            for j in range(8):
                canvas.create_line(0, 16 * j, 128, 16 * j, fill="blue")



        window.mainloop()  # Create an event loop


TVBars()  # Create GUI