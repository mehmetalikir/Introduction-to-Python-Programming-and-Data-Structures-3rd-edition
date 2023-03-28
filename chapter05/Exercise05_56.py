# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Count uppercase letters) Write a program that prompts the user to enter a string
and displays the number of the uppercase letters in the string.'''

# Prompt the user to enter a string
s = input("Please enter a string: ")

# Assign values
count = 0
c = ''

# Count the number of uppercase letters
for i in range(0, len(s)):
    c = s[i]
    if 'A' <= c <= 'Z':
        count += 1

# Display result
print("The number of uppercase letter in Programming is fun is", count)
