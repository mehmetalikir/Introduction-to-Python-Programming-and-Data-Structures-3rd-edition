# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Geometry display angles) Rewrite Listing 4.2, ComputeAngles.py, using the
following function for computing the distance between two points.

def distance(x1, y1, x2, y2, x3, y3):
'''

import math


def distance(x1, y1, x2, y2, x3, y3):
    a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
    b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
    c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

    A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
    B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
    C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

    print("The three angles are ", round(A * 100) / 100.0,
          round(B * 100) / 100.0, round(C * 100) / 100.0)


def main():

    # Prompt the user to enter coordinates
    x1 = float(input("Please enter x-coordinate for Point 1: "))
    y1 = float(input("Please enter y-coordinate for Point 1: "))
    x2 = float(input("Please enter x-coordinate for Point 2: "))
    y2 = float(input("Please enter y-coordinate for Point 2: "))
    x3 = float(input("Please enter x-coordinate for Point 3: "))
    y3 = float(input("Please enter y-coordinate for Point 3: "))

    distance(x1, y1, x2, y2, x3, y3)


main()
