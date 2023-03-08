# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

# Exercise02_29
''' (Turtle: draw a circle) Write a program that prompts the user to enter the center and
radius of a circle, and then displays the circle and its area, as shown in Figure 2.5b.'''

import turtle

# Prompt the user for input
radius = int(input("Please enter the radius of the circle: "))
diameter = radius * 2

# Area of a circle = π × r2.
pi = 3.14
area = pi * (diameter ** 2)

# Slowest speed
turtle.speed(1)

# Turtle draws the circles
turtle.pensize(1)
turtle.color("black")
turtle.penup()
turtle.goto(-diameter, 0)
turtle.pendown()
turtle.circle(radius)
turtle.write(area, font=("Times", 12))

turtle.done