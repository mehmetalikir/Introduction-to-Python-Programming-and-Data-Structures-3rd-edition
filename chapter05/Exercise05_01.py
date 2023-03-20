# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Count positive and negative numbers and compute the average of numbers) Write
a program that reads an unspecified number of integers, determines how many
positive and negative values have been read, and computes the total and average of
the input values (not counting zeros). Your program ends with the input 0. Display
the average as a floating-point number'''

# Prompt the user for input
number = int(input("Enter an integer, the input ends if it is 0: "))

# Keep reading number until the input is 0
sum = 0
evens = 0
odds = 0
while number != 0:
    sum += number
    number = int(input("Enter an integer, the input ends if it is 0: "))
    if number % 2 == 0:
        evens = evens + 1
    else:
        odds = odds + 1

# Display the average as a floating-point number
print("The number of evens is", evens)
print("The number of odds is", odds)
print("The sum is", sum)
print("The average is", sum / (evens + odds))



