# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display a bar chart) Write a program that uses a bar chart to display the percentages
of the overall grade represented by the project, quizzes, the midterm exam,
and the final exam, as shown in Figure 10.20a. Suppose that the project is 20 percent
of the grade and its value is displayed in red, quizzes are 10 percent and are
displayed in blue, the midterm exam is 30 percent and is displayed in green, and
the final exam is 40 percent and is displayed in orange.'''

from tkinter import *  # Import tkinter

# Constant
WIDTH = 600
HEIGHT = 300


class BarChart:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Bar Chart")  # Set a title

        self.canvas = Canvas(window, bg="white", width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.drawABar(20, 140, 120, 180, "red", "Project -- 20%")
        self.drawABar(140, 160, 240, 180, "blue", "Quizzes -- 10%")
        self.drawABar(260, 120, 360, 180, "green", "Midterm -- 30%")
        self.drawABar(380, 100, 480, 180, "orange", "Final -- 40%")

        window.mainloop()  # Create an event loop

    def drawABar(self, x0, y0, x1, y1, color, title):
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.canvas.create_text((x1 - 40), (y1 - 110), text=title)


BarChart()  # Create GUI
