# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Health application: BMI) Revise Listing 3.5, ComputeAndInterpretBMI.py, to
let users enter their weight in pound and their in feet and inches. For example,
if a person is 5 feet and 10 inches, you will enter 5 for feet and 10 for inches.'''

# Prompt the user to enter weight in pounds
weight = float(input("Please enter weight in pounds: "))

# Prompt the user to enter height in inches
height = float(input("Please enter height in inches"))

KILOGRAMS_PER_POUND = 0.45359237 # Constant
METERS_PER_INCH = 0.0254 # Constant

# Compute BMI
weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)

#Display result
print("BMI is", bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")