# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_15
#(Geometry: area of an octagon)
"""
Write a program that prompts the user
to enter the side of an octagon and displays its area.
The formula for computing the area of an octagon is:
Area = 2s²(1 + (2 ** 0.5)), where s is the length of a side.
"""
#The length of the side:
s = float(input("Enter the side of an octagon:\t"))

#The area of the octagon:
area = 2 * s ** 2 * (1 + (2 ** 0.5))
print("The area of the octagon, (where the length of a side is:", \
      s, "):", area)

