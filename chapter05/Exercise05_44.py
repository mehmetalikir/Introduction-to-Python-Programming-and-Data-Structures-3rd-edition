# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Decimal to binary) Write a program that prompts the user to enter a decimal
integer and displays its corresponding binary value.'''

# Prompt the user to enter a decimal integer
decimal = int(input("Enter a decimal integer: "))

# Assign values
toBinary = ""

# Convert the decimal number to a binary number
while decimal >= 1:
    if decimal % 2 == 0:
        toBinary = "0" + toBinary
    else:
        toBinary = "1" + toBinary

    decimal /= 2

# Display result
print(toBinary)

#print(bin(decimal))
