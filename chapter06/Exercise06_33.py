# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: area of a hexagon) Write a program with function that return the area
of hexagon. Prompt the user to enter the side of hexagon.
((3√3 * s^2) / 2  )'''
import math


# Function that return the area of hexagon
def area(s):
    return (3 * math.sqrt(3) *
            (s * s)) / 2


def main():
    # Prompt the user to enter the side of hexagon.
    s = int(input("Please enter the side of hexagon: "))

    # Display result
    print(f"Area of hexagon is %.2f " % area(s))


main()
