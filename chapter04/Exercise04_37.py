# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Generate vehicle plate numbers) Assume a vehicle plate number consists of three
uppercase letters followed by four digits. Write a program to generate a plate
number.'''

import random

# Randomize letters for uppercase
ch0 = chr(random.randint(65,90))
ch1 = chr(random.randint(65,90))
ch2 = chr(random.randint(65,90))

# Randomize numbers
num1 = str(random.randint(0,9))
num2 = str(random.randint(0,9))
num3 = str(random.randint(0,9))
num4 = str(random.randint(0,9))

# Generate a random string of tree letters and four numbers
s = str(ch0 + ch1 + ch2 + num1 + num2 + num3 + num4)

# Display result
print("Generated random string:", s)