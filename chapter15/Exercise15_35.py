# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: Sierpinski triangle) Revise Listing 15.9, SierpinskiTriangle.py, to display
the filled Sierpinski triangles, as shown in Figure 15.21.'''

from tkinter import *


def displayTriangles(canvas, order, p1, p2, p3):
    if order == 0:
        # Draw a triangle to connect three points
        canvas.create_polygon(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], fill="black")
    else:
        # Get the midpoint on each edge in the triangle
        p12 = midpoint(p1, p2)
        p23 = midpoint(p2, p3)
        p31 = midpoint(p3, p1)

        # Recursively display three triangles
        displayTriangles(canvas, order - 1, p1, p12, p31)
        displayTriangles(canvas, order - 1, p12, p2, p23)
        displayTriangles(canvas, order - 1, p31, p23, p3)


def midpoint(p1, p2):
    p = [0, 0]
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p


def main():
    # Create the main window
    window = Tk()
    window.title("Sierpinski Triangle")

    # Create a canvas to draw the Sierpinski triangle
    canvas = Canvas(window, width=400, height=400)
    canvas.pack()

    p1 = [200, 50]
    p2 = [50, 350]
    p3 = [350, 350]

    order = int(input("Please enter an order: "))
    displayTriangles(canvas, order, p1, p2, p3)

    # Start the Tkinter event loop
    window.mainloop()


main()
