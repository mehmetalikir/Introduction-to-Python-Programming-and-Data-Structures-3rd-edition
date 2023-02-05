#Exercise01_16
''' (Turtle: draw four circles) Write a program that draws four circles in the center
of the screen, as shown in Figure 1.13a'''

import turtle

# slowest speed
turtle.speed(1)

# turtle draws four circles
turtle.pensize(5)
turtle.color("black")
turtle.penup()
turtle.goto(-110, 0)
turtle.pendown()
turtle.circle(55)

turtle.color("black")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.circle(55)

turtle.color("black")
turtle.penup()
turtle.goto(0, 110)
turtle.pendown()
turtle.circle(55)

turtle.color("black")
turtle.penup()
turtle.goto(-110, 110)
turtle.pendown()
turtle.circle(55)





