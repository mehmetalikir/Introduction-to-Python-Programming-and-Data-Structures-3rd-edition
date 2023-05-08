# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display a pie chart) Write a program that uses a pie chart to display the percentages
of the overall grade represented by the project, quizzes, the midterm exam,
and the final exam, as shown in Figure 10.26b. Suppose that project is weighted as
20 percent of the grade and is displayed in red, quizzes are 10 percent and are displayed
in blue, the midterm exam is 30 percent and is displayed in green, and the
final exam is 40 percent and is displayed in orange.'''

from tkinter import *  # Import tkinter
import math

# Constant
RADIUS = 100
WIDTH = 300
HEIGHT = 300


class PieChart:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Pie Chart")  # Set a title

        self.canvas = Canvas(window, bg="white", width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.drawAPie(0, 360 * 0.2, "red", "Project -- 20%")
        self.drawAPie(360 * 0.2, 360 * 0.1, "blue", "Quizzes -- 10%")
        self.drawAPie(360 * 0.2 + 360 * 0.1, 360 * 0.3, "green", "Midterm -- 30%")
        self.drawAPie(360 * 0.2 + 360 * 0.1 + 360 * 0.3, 360 * 0.4, "orange", "Final -- 40%")

        window.mainloop()  # Create an event loop

    def drawAPie(self, start, extent, color, title):
        self.canvas.create_arc(WIDTH / 2 - RADIUS, HEIGHT / 2 - RADIUS,
                               WIDTH / 2 + RADIUS, HEIGHT / 2 + RADIUS,
                               start=start, extent=extent, fill=color)
        x = WIDTH / 2 + RADIUS * math.cos(math.radians(extent / 2 + start))
        y = HEIGHT / 2 - RADIUS * math.sin(math.radians(extent / 2 + start))
        self.canvas.create_text(x, y, text=title)


PieChart()
