# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_17
#(Health application: compute BMI)
"""
It can be calculated by taking your weight in kilograms
and dividing it by the square of your height in meters.
one pound is 0.45359237 kg
one inch is 0.0254 m.
"""
#Enter weight in pounds
w = float(input("Enter weight in pounds (for example: 95.5):\t")) \
    * 0.45359237

#Enter height in inches
h = float(input("Enter height in inches (for example: 50):\t")) \
    * 0.0254

#Calculation the BMI:
bmi = w / (h ** 2)

print("The BMI is:",bmi)
