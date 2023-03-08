# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_23
'''(Slope of a line) Write a program that prompts the user to enter the coordinates
of two points (x1, y1) and (x2, y2) and displays the slope of the line connects the
two points. The formula of the slope is (y2 - y1) / (x2 - x1)'''

#Prompt the user for input
x1 = float(input("Please enter x-coordinate of Point 1: "))
y1 = float(input("Please enter y-coordinate of Point 1: "))
x2 = float(input("Please enter x-coordinate of Point 2: "))
y2 = float(input("Please enter y-coordinate of Point 2: "))

#Compute result
result = (y2 - y1) / (x2 - x1)

#Display results
print("The slope for the line that connects two points (", x1, ",", y1,") and", "(", x2, ",", y2, ") is", result)