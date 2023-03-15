# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Random point) Write a program that displays a random coordinate in a square.
The square is centered at (0, 0) and the length of each side is 100'''

import random

# Generate random points
x = random.randint(-50,50)
y = random.randint(-50,50)

# Display coordinate
print("Random coordinate: (", x, ",", y, ")")
