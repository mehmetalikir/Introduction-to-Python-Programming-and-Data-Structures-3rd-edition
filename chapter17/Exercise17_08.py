# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Turtle: Bubble sort animation) Write a program that animates the Bubble sort
algorithm. Create a list that consists of 20 distinct numbers from 1 to 20 in
a random order. The list elements are displayed in a histogram, as shown in
Figure 17.17. If two elements are swapped, redisplay them in the histogram'''

import turtle
from random import shuffle


def drawHistogram(list):
    for i in range(len(list)):
        draw(list, i)


def draw(list, i):
    height = list[i] * HEIGHT / max(list)
    drawABar(-WIDTH / 2 + i * widthOfBar + 10,
             -HEIGHT / 2, widthOfBar - 5, height)
    drawAString(-WIDTH / 2 + i * widthOfBar + 18,
                -HEIGHT / 2 + height + 10, str(list[i]))


def drawABar(i, j, widthOfBar, height):
    turtle.penup()
    turtle.goto(i, j)
    turtle.setheading(90)  # Set orientation to north
    turtle.pendown()

    turtle.forward(height)  # Draw a vertical line
    turtle.right(90)  # Turn right 90 degrees
    turtle.forward(widthOfBar)  # Draw a horizontal line
    turtle.right(90)  # Turn right 90 degrees
    turtle.forward(height)  # Draw a vertical line


def drawAString(i, j, ch):
    turtle.penup()
    turtle.goto(i, j)
    turtle.setheading(90)  # Set orientation to north
    turtle.pendown()
    turtle.write(ch)


def swap(list, i, j):
    turtle.color("white")
    draw(list, j)
    draw(list, i)

    list[i], list[j] = list[j], list[i]
    turtle.color("black")
    draw(list, j)
    draw(list, i)


# The function for sorting the numbers
def bubbleSort(lst):
    needNextPass = True
    k = 1
    while k < len(lst) and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False
        for i in range(len(lst) - k):
            if lst[i] > lst[i + 1]:
                # swap lst[i] with lst[i + 1]
                # temp = lst[i]
                # lst[i] = lst[i + 1]
                # lst[i + 1] = temp
                swap(lst, i, i + 1)
                needNextPass = True  # Next pass still needed
        k += 1


list1 = list(range(1, 21))  # Create a list with elements 3, 4, 5
shuffle(list1)

turtle.hideturtle()
WIDTH = 600  # Width of the histogram
HEIGHT = 300  # Height of the histogram

# Draw a baseline
turtle.penup()
turtle.goto(-WIDTH / 2, -HEIGHT / 2)
turtle.pendown()
turtle.forward(WIDTH)

widthOfBar = WIDTH / len(list1)  # Width of each bar

turtle.speed(0)  # fast
drawHistogram(list1)

turtle.speed(0.5)  # slow

bubbleSort(list1)

turtle.done()
