# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Conversions between centimeters and inches) Write a module that contains the
following two functions:

# Convert from centimeters to inches
def cmsToInches(centimeters):

# Convert from inches to centimeters
def inchesToCms(inches):

The formula for the conversion are:

centimeters = inches / 2.54
inches = 2.54 * centimeters

Write a test program that invokes these functions to display the following tables:
'''

# Convert from centimeters to inches
def cmsToInches(centimeters):
    return 2.54 * centimeters
# Convert from inches to centimeters
def inchesToCms(inches):
    return inches / 2.54
def main():
    # Print header of tables
    print("Centimeters      Inches  |   Inches      Centimeters")
    print("----------------------------------------------------")
    j = 50
    for i in range(1, 20, +2):
        # Display result
        print(f"%-1d%18.3f%7s%6d%18.2f" % (i, inchesToCms(i), "|", (j), cmsToInches(j)))
        j += 3


main()
