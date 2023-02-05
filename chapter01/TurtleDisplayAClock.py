# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@..com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise01_21
''' (Turtle: display a clock) Write s program that display a clock to show the time
9:15:00, as shown in Fugure 1.14c.'''

import turtle
turtle.speed(1)


# turtle draws a red line
point1 = (-79, 50)
point2 = (100, 50)
turtle.pencolor("black")

turtle.penup()
turtle.goto(point1)
turtle.pendown()
turtle.goto(point2)

turtle.pensize(2)
turtle.color("black")
turtle.penup()
turtle.goto(19, -90)
turtle.pendown()
turtle.circle(145)

