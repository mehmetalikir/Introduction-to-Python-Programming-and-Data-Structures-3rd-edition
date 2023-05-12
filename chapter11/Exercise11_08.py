# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display animated text) Write a program that displays the animated text “Welcome
to Python Programing” word by word on screen. Display only one word at a time on the
screen, remove it, display the next word and so on, as shown in Figure 11.18a–b.
(Hint: Use a numeric variable to control the alternation'''

from tkinter import *  # Import tkinter

width = 200
height = 100


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Display animated text")  # Set a title

        sleepTime = 400
        canvas = Canvas(window, bg="white", width=width, height=height)
        canvas.pack()

        count = 0  # To control the alteration
        while True:
            if count == 0:
                canvas.delete("text")
                canvas.create_text(width / 2, height / 2, text="Welcome", tags="text")
                count += 1
            elif count == 1:
                canvas.delete("text")
                canvas.create_text(width / 2, height / 2, text="To", tags="text")
                count += 1
            elif count == 2:
                canvas.delete("text")
                canvas.create_text(width / 2, height / 2, text="Python", tags="text")
                count += 1
            elif count == 3:
                canvas.delete("text")
                canvas.create_text(width / 2, height / 2, text="Programming", tags="text")

                count = 0  # reset count

            canvas.after(sleepTime)  # Sleep for 400 milliseconds
            canvas.update()

        window.mainloop()  # Create an event loop


MainGUI()
