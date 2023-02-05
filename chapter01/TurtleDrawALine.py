#Exercise01_17
"""
(Turtle: draw a line)Write a program that draws a red line connecting two points(-39, 48)
and (50, -50) and display the coordinates of the two points,,
as shown in Figure 1.13b
"""
import turtle
# slowest speed
turtle.speed(1)

# turtle draws a red line
point1 = (-39, 48)
point2 = (50, -50)
turtle.pencolor("red")

turtle.penup()
turtle.goto(point1)
turtle.pendown()
turtle.goto(point2)



