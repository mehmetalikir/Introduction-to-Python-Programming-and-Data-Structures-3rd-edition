# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Decimal to hex) Write a program that prompts the user to enter an integer between
0 and 15 and displays its corresponding hex number.'''

# Prompt the user to enter an integer between 0 and 15
decimal = int(input("Enter a decimal value (0 to 15): "))

# Display its corresponding hex number
if 0 <= decimal <= 9:
    print("The hex value is " , decimal)
elif 10 <= decimal <= 15:
    print("The hex value is ", chr(ord('A') - 10 + decimal))
else:
    print(decimal, " is an invalid input")