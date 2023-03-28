# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Decimal to octal) Write a program that prompts the user to enter a decimal
integer and displays its corresponding octal value.'''

# Prompt the user to enter a decimal integer
decimal = int(input("Enter a decimal integer: "))

# Assign values
toOctal = ""

# Convert the decimal value to an octal value
while decimal > 0:
    toOctal = str( decimal % 8) + toOctal
    decimal //= 8

# Display result
print(toOctal)

#print(oct(decimal))


