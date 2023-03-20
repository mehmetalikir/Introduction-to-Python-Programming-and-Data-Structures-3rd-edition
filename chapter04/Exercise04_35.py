# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Slope-intercept form) Write a program that prompts the user to enter the coordinates
of two points(x1, y1) and (x2,y2) and displays the line equation in the slope-intercept
form, i.e, y = mx + b. For a review of line equations, see http://www.purplemath.com/modules/strtlneq.htm.
m and b can be computed using the following formula:
        m = (y2 - y1) / (x2 - x1) b = y1 - mx1
Don't display m if it is 1 and don't display b if it is 0.
'''
import sys

# Prompts the user to enter the coordinates of two points(x1, y1) and (x2,y2)
x1 = float(input("Enter the X-ordinate for the first point: "))
y1 = float(input("Enter the Y-ordinate for the first point: "))
x2 = float(input("Enter the X-ordinate for the second point: "))
y2 = float(input("Enter the Y-ordinate for the second point: "))

# Slope - Intercept
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1

# Don't display m if it is 1 and don't display b if it is 0
if m == 1 and b == 0:
    sys.exit(1)

# Displays the line equation in the slope-intercept form
if b == 0:
    print("Equation of Line is: ", "y = ", m, "x")
elif m == 1:
    print("Equation of Line is: ", "y = ", "x +", b)
else:
    print("Equation of Line is: ", "y = ", m, "x +", b)