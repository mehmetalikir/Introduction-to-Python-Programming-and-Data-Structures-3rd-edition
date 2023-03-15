# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Palindrome number) Write a program that prompts the user to enter a three-digit
integer and determines whether it is a palindrome number. A number is palindrome
if it reads the same from right to left and from left to right.'''

# Prompt the user to enter a three-digit integer
number = int(input("Please enter a three-digit integer: "))
str = number

# Determine whether it is a palindrome number
digit1 = number % 10
number //=  10
digit2 = number % 10
number //=  10
digit3 = number
isPalindrome = digit1 == digit3

# Display result
if isPalindrome:
    print(str,"is a palindrome")
else:
    print(str,"is not a palindrome")
