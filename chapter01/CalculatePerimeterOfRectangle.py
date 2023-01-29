"""(Area and perimeter of a rectangle) Write a program that displays the area and
perimeter of a rectangle with the width of 4.5 height of 7.9 using the fol-
lowing formula:
			area = width x height
			perimeter = 2 x (height + width)
"""
#Data fields
area = 4.5*7.9
perimeter = 2 * (4.5 + 7.9)

# Displays the area and perimeter of a rectangle
print("Area: {:,.2f}".format (area))
print("Perimeter: {:,.2f}".format(perimeter))

print("----------------------")
# Displays the area and perimeter of a rectangle by using round
print("Area: ", round(area,2))
print("Perimeter: ", round(perimeter,2))





