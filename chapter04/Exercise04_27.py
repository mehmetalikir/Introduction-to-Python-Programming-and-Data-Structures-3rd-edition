# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Phone key pads) The international standard letter/number mapping found on the
telephone is shown below:

Write a program that prompts the user to enter a letter and displays its corresponding
number.'''

# Prompt the use for input
c = str(input("Please enter an uppercase letter: ")).upper()

# Check its corresponding number
if 'Z'>= c >= 'W':
    number = 9
elif 'V'>= c >= 'T':
    number = 8
elif 'S'>= c >= 'P':
    number = 7
elif 'O'>= c >= 'M':
    number = 6
elif 'L'>= c >= 'J':
    number = 5
elif 'I'>= c >= 'G':
    number = 4
elif 'F'>= c >= 'D':
    number = 3
elif 'C'>= c >= 'A':
    number = 2
else:
    print("1 0 * #")

# Display result
print("The corresponding number is ", number)