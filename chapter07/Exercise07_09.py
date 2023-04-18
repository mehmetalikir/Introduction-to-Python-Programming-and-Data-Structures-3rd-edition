# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Statistics: compute deviation) Programming Exercise 5.46 computes the standard
deviation of numbers. This exercise uses a different but equivalent formula to
compute the standard deviation of n numbers.

To compute the standard deviation with this formula, you have to store the individual
numbers using a list, so that they can be used after the mean is obtained. Do not use
the Python statistics functions in this program.
    Your program should contain the following functions:


    Write a test program that prompts the user to enter list of numbers in one
line and displays the mean and standard deviation, as shown in the following sample run:'''
import math


def main():
    # Create a list of numbers
    list1 = createList()

    # Displays the mean and standard deviation
    displayResult(list1)


def createList():
    # Prompt the user to enter list of numbers
    s = input("Please enter numbers: ")  # 1.9 2.5 3.7 2 1.5 6 3 4 5 2
    list1 = [float(x) for x in s.split(" ")]

    return list1


# Compute the mean and standard deviation
def displayResult(list1):
    print("The means is %.02f" % mean(list1))
    print("The standard deviation is ", deviation(list1))


# Compute the standard deviation of values
def deviation(x):
    sum = 0
    for y in x:
        sum += math.pow((y - mean(x)), 2)

    return math.sqrt(sum / (len(x) - 1))


# Compute the mean of a list of values
def mean(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]

    return sum / len(x)


main()  # Invoke main function
