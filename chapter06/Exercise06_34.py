# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: area of a regular polygon) Rewrite Programing Exercise 4.5 using
the following function to return the area of a regular polygon: '''

import math


def area(n, side):
    # Compute the area of the polygon
    area = (side * math.pow(n, 2) / (4 * math.tan(math.pi / side)))

    # Display its area
    print(f"The are of the polygon is {area}")


def main():
    # Prompt the user to enter the number of sides and their length of a regular polygon
    side = float(input("Please enter the number of sides: "))
    s = float(input("Please enter the length of a side: "))

    area(s, side)  # Invoke function


main()
