# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Conversion from inches to centimeters) Write a program that displays the following
table (note that 1 inch is 2.54 centimeters):'''

inch = 1 # Initialize variable

# Display header for table
print("Inches      Centimeters")

# Display table
while inch <= 50:
    print(inch, "          ", format((inch * 2.54), ".2f"))
    inch += 1


