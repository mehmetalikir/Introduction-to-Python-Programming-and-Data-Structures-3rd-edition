# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Turtle: Recursive tree) Rewrite the recursive tree in Exercise 15.31 using Turtle,
as shown in Figure 15.17. Your program should prompt the user to enter the
order and display the corresponding fractal for the order.'''

import math
import turtle

from UsefulTurtleFunctions import drawLine

angleFactor = math.pi / 5
sizeFactor = 0.58


# Draw a snowflake with the specified order on one line
def paintBranch(depth, x1, y1, length, angle):
    if depth >= 0:
        x2 = x1 + math.cos(angle) * length
        y2 = y1 + math.sin(angle) * length

        # Draw the line
        drawLine(x1, y1, x2, y2)

        # Draw the left branch
        paintBranch(depth - 1, x2, y2, length * sizeFactor, angle + angleFactor)
        # Draw the right branch
        paintBranch(depth - 1, x2, y2, length * sizeFactor, angle - angleFactor)


def main():
    depth = float(input("Please enter a depth: "))
    paintBranch(depth, 0, -50, 200 / 3, math.pi / 2)

    turtle.done()


main()
