# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Reverse number) Write a program that prompts the user to enter a four-digit
integer and displays the number in reverse order.'''

# Prompts the user to enter a four-digit integer
number = int(input("PLease enter a four-digit integer (ex: 1234): "))

# Reverse number
digit1 = number % 10
number //=  10
digit2 = number % 10
number //=  10
digit3 = number % 10
number //=  10
digit4 = number

# Display result
print("Reversed number: ", digit1,digit2,digit3,digit4)