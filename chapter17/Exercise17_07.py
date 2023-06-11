# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Turtle: Insertion sort animation) Write a program that animates the insertion sort
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
def InsertionSort(lst):
    for i in range(1, len(lst)):
        # insert lst[i] into a sorted sublist lst[0..i-1] so that
        #   lst[0..i] is sorted.
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            swap(lst, k + 1, k)
            k -= 1

        # Insert the current element into lst[k + 1]
        lst[k + 1] = currentElement


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

InsertionSort(list1)

turtle.done()
