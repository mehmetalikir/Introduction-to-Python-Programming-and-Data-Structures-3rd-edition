# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

# Exercise02_28
''' (Turtle: draw a rectangle) Write a program that prompts the user to enter the
center of a rectangle, its width and height, and then displays the rectangle, as
shown in Figure 2.5a.'''

# Import turtle
import turtle



# Prompt the user for inputs
width = int(input("Please enter width of the rectangle: "))
height = width / 2

# Slowest speed
turtle.speed(1)

# Draw the rectangle
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)
