# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Financial application: compute future tuition) Suppose that the tuition for a university
is $10,000 this year and increases 5% every year. In one year, the tuition
will be $10,500. Write a program that computes the tuition in 10 years and the
total cost of four years’ worth of tuition after the tenth year.'''

tuitionFee = 10_000  # Initialize variable
afterTenth = 0  # Initialize variable
totalCost = 0  # Initialize variable

# Computes the tuition in 10 years
count = 0
while count <= 14:
    tuitionFee += (tuitionFee * 0.05)

    if count == 9:
        afterTenth = tuitionFee
    if count > 9:
        totalCost += tuitionFee
    count += 1

print("Total cost of four years’ worth of tuition after the tenth year: ", round(totalCost, 2))
print("The tuition in 10 years", round(afterTenth, 2))
