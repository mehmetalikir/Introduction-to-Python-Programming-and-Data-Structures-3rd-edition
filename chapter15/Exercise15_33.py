# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: Hilbert curve) The Hilbert curve, first described by German mathematician
David Hilbert in 1891, is a space-filling curve that visits every point in
a square grid with a size of 2 x 2,4 x 4,8 x 8,16 x 16 or any other power
of 2. Write a program that displays a Hilbert curve for the specified order, as
shown in Figure 15.18.'''

from tkinter import *


def main():
    # Create the main window
    window = Tk()
    window.title("Hilbert Curve")

    # Create a canvas to draw the Hilbert curve
    canvas = Canvas(window, width=400, height=400)
    canvas.pack()

    order = int(input("Enter an order: "))

    SIZE = 400
    length = SIZE

    for i in range(order):
        length = length / 2  # Get the right length for the order

    # Get the start point
    x = SIZE / 2 - length / 2
    y = SIZE / 2 - length / 2

    upperU(canvas, order, x, y, length)

    # Start the Tkinter event loop
    window.mainloop()


def upperU(canvas, order, x, y, length):
    if order > 0:
        leftU(canvas, order - 1, x, y, length)
        canvas.create_line(x, y, x, y + length)
        upperU(canvas, order - 1, x, y + length, length)
        canvas.create_line(x, y + length, x + length, y + length)
        upperU(canvas, order - 1, x + length, y + length, length)
        canvas.create_line(x + length, y + length, x + length, y)
        rightU(canvas, order - 1, x + length, y, length)


def leftU(canvas, order, x, y, length):
    if order > 0:
        upperU(canvas, order - 1, x, y, length)
        canvas.create_line(x, y, x + length, y)
        leftU(canvas, order - 1, x + length, y, length)
        canvas.create_line(x + length, y, x + length, y + length)
        leftU(canvas, order - 1, x + length, y + length, length)
        canvas.create_line(x + length, y + length, x, y + length)
        downU(canvas, order - 1, x, y + length, length)


def rightU(canvas, order, x, y, length):
    if order > 0:
        downU(canvas, order - 1, x, y, length)
        canvas.create_line(x, y, x, y + length)
        rightU(canvas, order - 1, x, y + length, length)
        canvas.create_line(x, y + length, x - length, y + length)
        rightU(canvas, order - 1, x - length, y + length, length)
        canvas.create_line(x - length, y + length, x - length, y)
        upperU(canvas, order - 1, x - length, y, length)


def downU(canvas, order, x, y, length):
    if order > 0:
        rightU(canvas, order - 1, x, y, length)
        canvas.create_line(x, y, x - length, y)
        downU(canvas, order - 1, x - length, y, length)
        canvas.create_line(x - length, y, x - length, y - length)
        downU(canvas, order - 1, x - length, y - length, length)
        canvas.create_line(x - length, y - length, x, y - length)
        leftU(canvas, order - 1, x, y - length, length)


main()
