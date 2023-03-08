# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_26
''' (Turtle: draw four circles) Write a program that prompts the user to enter the
radius and draws four circles in the center of the screen, as shown in Figure 2.4a.'''

# Import Turtle
import turtle

# Prompt the user for input
radius = int(input("Please enter the radius of four circles: "))
diameter = radius * 2

# Slowest speed
turtle.speed(1)

# Turtle draws four circles
turtle.pensize(5)
turtle.color("black")
turtle.penup()
turtle.goto(-diameter, 0)
turtle.pendown()
turtle.circle(radius)

turtle.color("pink")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.circle(radius)

turtle.color("black")
turtle.penup()
turtle.goto(0, diameter)
turtle.pendown()
turtle.circle(radius)

turtle.color("green")
turtle.penup()
turtle.goto(-diameter, diameter)
turtle.pendown()
turtle.circle(radius)
