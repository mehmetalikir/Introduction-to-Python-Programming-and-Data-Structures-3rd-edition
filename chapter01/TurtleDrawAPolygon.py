# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@..com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise01_19
''' (Turtle: draw a polygon) Write a program that draws a polygon that connects the
points (40, -69.28), (-40, -69.28), (-80, -9.8), (-40, 69), (40, 69),
and (80, 0) in this order, as shown Figure 1.14a.'''

import turtle
turtle.speed(1)

# points
points1 = (40, -69.28)
points2 = (-40, -69.28)
points3 = (-80, -9.8)
points4 = (-40, 69)
points5 = (40, 69)
points6 = (80, 0)

# turtle draws polygon
turtle.penup()
turtle.goto(points1)
turtle.pendown()
turtle.goto(points2)
turtle.pendown()
turtle.goto(points3)
turtle.pendown()
turtle.goto(points4)
turtle.pendown()
turtle.goto(points5)
turtle.pendown()
turtle.goto(points6)
turtle.pendown()
turtle.goto(points1)

