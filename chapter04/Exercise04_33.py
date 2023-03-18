# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Random uppercase strings) Write a program that generates a random string of
four characters from the 26 uppercase letters'''

import random

# Randomize ASCII codes for uppercase
ch0 = chr(random.randint(65,90))
ch1 = chr(random.randint(65,90))
ch2 = chr(random.randint(65,90))
ch3 = chr(random.randint(65,90))

# Generate a random string of four characters from the 26 uppercase letters
s = str(ch0 + ch1 + ch2 + ch3)

# Display result
print("Generated random string:", s)



