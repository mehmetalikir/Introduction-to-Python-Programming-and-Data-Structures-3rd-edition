# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Geometry: two rectangles) Write a program that prompts the user to enter the
center x-, y-coordinates, width, and height of two rectangles and determines
whether the second rectangle is inside the first or overlaps with the first, as shown
in Figure 3.10. Test your program to cover all cases.'''

import math

# Prompt user to enter the center x-, y-coordinates, width, and height of two rectangles
r1X = float(input("Please enter r1's center x-coordinate: "))
r1Y = float(input("Please enter r1's center y-coordinate: "))
r1Width = float(input("Please enter r1's width: "))
r1Height = float(input("Please enter r1's height: "))
r2X = float(input("Please enter r2's center x-coordinate: "))
r2Y = float(input("Please enter r2's center y-coordinate: "))
r2Width = float(input("Please enter r2's width: "))
r2Height = float(input("Please enter r2's height: "))

# Determine whether the second rectangle is inside the first or overlaps with the first
if ((math.pow(math.pow(r2Y - r1Y, 2), .05) + r2Height / 2 <= r1Height / 2) and
        (math.pow(math.pow(r2X - r1X, 2), .05) + r2Width / 2 <= r1Width / 2) and
        (r1Height / 2 + r2Height / 2 <= r1Height) and
        (r1Width / 2 + r2Width / 2 <= r1Width)):
    print("r2 is inside r1")
elif ((r1X + r1Width / 2 > r2X - r2Width) or
      (r1Y + r1Height / 2 > r2Y - r2Height)):
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")
