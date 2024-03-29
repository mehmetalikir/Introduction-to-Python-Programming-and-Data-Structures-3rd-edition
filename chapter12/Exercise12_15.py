# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: Julia set) The preceding exercise describes Mandelbrot sets. The Mandelbrot
set consists of the complex c value such that the sequence ...
is bounded with fixed and c varying. If we fix c and vary the ...
point (x, y) is said to be in a Julia set for a fixed complex value c if the function
stays bounded. Write a program that draws a Julia set as shown
in Figure 12.26b. Note that you only need to revise the count method in Exercise
12.14 by using a fixed c value ... '''
from tkinter import *  # Import tkinter


# Convert a decimal to a hex as a string
def toHex(decimalValue):
    hex = ""

    while decimalValue != 0:
        hexValue = decimalValue % 16
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16

    if len(hex) < 2:
        hex = "0" + hex

    return hex


# Convert an integer to a single hex digit in a character
def toHexChar(hexValue):
    if hexValue <= 9 and hexValue >= 0:
        return chr(hexValue + ord('0'))
    else:  # hexValue <= 15 && hexValue >= 10
        return chr(hexValue - 10 + ord('A'))


COUNT_LIMIT = 60


# Paint a Julia set image in the canvas
def paint():
    x = -2.0
    while x < 2.0:
        y = -2.0
        while y < 2.0:
            c = count(complex(x, y))
            if c == COUNT_LIMIT:
                color = "red"  # c is in a Mandelbrot set
            else:
                color = "#" + toHex(c * 37 % 256) + toHex(
                    c * 58 % 256) + toHex(c * 159 % 256)

            # print(color)
            # Fill a tiny rectangle with the specified color
            canvas.create_rectangle(x * 100 + 200, y * 100 + 200,
                                    x * 100 + 200 + 5, y * 100 + 200 + 5, fill=color)
            y += 0.05
        x += 0.05


# Returns the iteration count
def count(c):
    z = complex(-0.3, 0.6)  # z0

    for i in range(COUNT_LIMIT):
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2: return i  # The sequence is unbounded

    return COUNT_LIMIT  # Indicate a bounded sequence


window = Tk()  # Create a window
window.title("Julia Set")  # Set a title

width = 400  # Width of the canvas
height = 400  # Height of the canvas
canvas = Canvas(window, width=width, height=height)
canvas.pack()

Button(window, text="Display", command=paint).pack()

window.mainloop()  # Create an event loop
