# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_02
''' (Compute the volume of a cube)
Write a program that reads in the side of a cube and computes the area in square meters and volume in cubie meters using the following formulas:
area = 6 * side * side
volume = side * side * side'''
side = float(input("Enter a side of the cube:\t"))
area = 6 * (side ** 2)
volume = side ** 3
print("""
Area of the cube: {:,.3f}
Volume of the cube: {:,.3f}""".format(area, volume))



