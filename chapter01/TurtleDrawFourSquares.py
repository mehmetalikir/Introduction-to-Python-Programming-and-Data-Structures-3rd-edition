#Exercise01_12
''' (Turtle: draw four squares) Write a program that draws four squares in the center
of the screen, as shown in Figure 1.12a'''

import turtle

# slowest speed
turtle.speed(1)

# turtle draw perimeter of square
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)

# turtle draws inner edges of square
turtle.right(180)
turtle.forward(75)

turtle.left(90)
turtle.forward(75)

turtle.right(90)
turtle.forward(75)