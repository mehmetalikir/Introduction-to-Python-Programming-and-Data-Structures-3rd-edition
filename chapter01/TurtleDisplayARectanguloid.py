# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@..com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise01_20
''' (Turtle: display a rectanguloid) Write a program that displays a rectanguloid, as
shown in Figure 1.14b. '''

import turtle

# forming front square face
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)


# bottom left side
turtle.goto(50, 50)

# forming back square face
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)


# bottom right side
turtle.goto(150, 50)
turtle.goto(100, 0)

# top right side
turtle.goto(100, 100)
turtle.goto(150, 150)

# top left side
turtle.goto(50, 150)
turtle.goto(0, 100)