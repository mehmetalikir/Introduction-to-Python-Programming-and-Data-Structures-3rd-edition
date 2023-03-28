# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Statistics: compute mean and standard deviation) In business applications, you
are often asked to compute the mean and standard deviation of data. The mean is
simply the average of the numbers. The standard deviation is a statistic that tells
you how tightly all the various data are clustered around the mean in a set of data.
For example, what is the average age of the students in a class? How close are the
ages? If all the students are the same age, the deviation is 0.
Write a program that prompts the user to enter ten numbers, and displays the
mean and standard deviations of these numbers using the following formula:'''
import math

# Assign values
standardDeviation, average, sum, number1, number2 = 0, 0, 0, 0, 0

for i in range(0,10):
    # Prompt the user to enter ten numbers
    number1 = float(input("Please enter a number: "))
    sum += number1
    number2 += math.pow(number1,1)

# Compute mean and standard deviation
average = sum / 10
standardDeviation = math.sqrt((number2 -(math.pow(number1, 2) / 10)) / 9)

# Display result
print("The mean is: %.2f" % average)
print("The standard deviation is %.5f" % standardDeviation)