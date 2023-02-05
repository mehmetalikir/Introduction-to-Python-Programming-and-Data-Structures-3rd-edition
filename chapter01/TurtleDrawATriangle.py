#Exercise01_14
''' (Turtle: draw a triangle) Write a program that draws four squares in the center
of the screen, as shown in Figure 1.12c'''

import turtle

# slowest speed
turtle.speed(1)

# turtle draws a triangle
turtle.left(-75)
turtle.forward(150)
turtle.right(-75)
turtle.forward(-150)
turtle.left(55)
turtle.forward(190)