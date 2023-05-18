# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: The PieChart class) Develop a class named PieChart that extends
Canvas for displaying a pie chart using the following constructor:
PieChart(parent, data, width = 400, height = 300)
Where data is a list, each element in the list is a nested list that consists of a
value, a title for the value, and a color for the wedge in the pie chart. For example,
for data = [[40, "CS", "red"], [30, "IS", "blue"], [50,
"IT", "yellow"]], the pie chart is as shown in the left part of Figure 12.29.
For data = [[140, "Freshman", "red"], [130, "Sophomore",
"blue"], [150, "Junior", "yellow"], [80, "Senior",
"green"]], the pie chart is as shown in the right part of Figure 12.29. Write a
test program that displays two pie charts, as shown in Figure 12.29.'''

from tkinter import *  # Import tkinter

width = 600
height = 400
radius = 150


class PieChart(Canvas):
    def __init__(self, parent, data, width=400, height=300):
        super().__init__(parent, width=width, height=height)
        self.setData(data)

    def setData(self, data):
        self.__data = data
        self.drawPieChart()

    def drawPieChart(self):
        self.create_oval(width / 2 - radius, height / 2 - radius,
                         width / 2 + radius, height / 2 + radius)


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("PieChart Reusable Class")  # Set title

        canvas1 = PieChart(window, [[40, "CS", "red"], [30, "IS", "blue"], [50, "IT", "yellow"]], width=width,
                           height=height)
        canvas1.grid(row=1, column=1)
        canvas2 = PieChart(window,
                           [[140, "Freshman", "red"], [130, "Sophomore", "blue"], [150, "Junior", "yellow"],
                            [80, "Senior", "green"]],
                           width=width, height=height)
        canvas2.grid(row=1, column=2)

        window.mainloop()  # Create an event loop


MainGUI()
