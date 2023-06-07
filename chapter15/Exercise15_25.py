# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: Koch snowflake fractal ) Section 15.8 presented the Sierpinski triangle
fractal. In this exercise, you will write a program to display another fractal,
called the Koch snowflake, named after a famous Swedish mathematician. A
Koch snowflake is created as follows:

    1. Begin with an equilateral triangle, which is considered to be the Koch fractal
    of order (or level) 0, as shown in Figure 15.14a.
    2. Divide each line in the shape into three equal line segments and draw an outward
    equilateral triangle with the middle line segment as the base to create a
    Koch fractal of order 1, as shown in Figure 15.14b.
    3. Repeat Step 2 to create a Koch fractal of order 2, 3, ..., and so on, as shown in
    Figure 15.14c–d.'''

import math
import tkinter as tk


class KochSnowflakeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Koch Snowflake Fractal")

        self.canvas_width = 500
        self.canvas_height = 500
        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        p1 = [0, self.canvas_height // 2]
        p2 = [self.canvas_width, self.canvas_height // 2]
        p3 = [self.canvas_width // 2, self.canvas_height]

        self.order = tk.IntVar()
        self.order.set(0)

        order_label = tk.Label(self.window, text="Order:")
        order_label.pack()
        order_entry = tk.Entry(self.window, textvariable=self.order)
        order_entry.pack()

        draw_button = tk.Button(self.window, text="Draw", command=self.draw_fractal)
        draw_button.pack()

        self.draw_base_triangle(p1, p2, p3)

        self.window.mainloop()

    def draw_base_triangle(self, p1, p2, p3):
        # Draw the initial equilateral triangle
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1])
        self.canvas.create_line(p2[0], p2[1], p3[0], p3[1])
        self.canvas.create_line(p3[0], p3[1], p1[0], p1[1])

    def draw_fractal(self):
        # Clear the canvas and draw the fractal based on user input
        self.canvas.delete("line")
        p1 = [0, self.canvas_height // 2]
        p2 = [self.canvas_width, self.canvas_height // 2]
        p3 = [self.canvas_width // 2, self.canvas_height]

        order = self.order.get()
        self.display_koch_snowflake(order, p1, p2)
        self.display_koch_snowflake(order, p2, p3)
        self.display_koch_snowflake(order, p3, p1)

    def display_koch_snowflake(self, order, p1, p2):
        if order == 0:
            # Base case: draw a line segment
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="line")
        else:
            deltaX = p2[0] - p1[0]
            deltaY = p2[1] - p1[1]

            x = [p1[0] + deltaX / 3, p1[1] + deltaY / 3]
            y = [p1[0] + deltaX * 2 / 3, p1[1] + deltaY * 2 / 3]
            z = [
                ((p1[0] + p2[0]) / 2 - math.cos(math.radians(30)) * (p1[1] - p2[1]) / 3),
                ((p1[1] + p2[1]) / 2 - math.cos(math.radians(30)) * (p2[0] - p1[0]) / 3)
            ]

            # Recursive calls to display the snowflake fractal
            self.display_koch_snowflake(order - 1, p1, x)
            self.display_koch_snowflake(order - 1, x, z)
            self.display_koch_snowflake(order - 1, z, y)
            self.display_koch_snowflake(order - 1, y, p2)


KochSnowflakeGUI()
