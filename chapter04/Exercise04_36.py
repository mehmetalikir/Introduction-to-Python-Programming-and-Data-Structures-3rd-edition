# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Check SSN) Write a program that prompts the user to enter a Social Security
number in the format DDD-DD-DDDD, where D is a digit. Your program should
check whether the input is valid.'''

c = str(input("Please enter a string for SSN: "))
isValid = c[0:2].isdigit() and c[4:5].isdigit() and c[7:10].isdigit() and c[3].startswith('-') and c[6].startswith('-')

if isValid:
    print("The input is valid")
else:
    print("Invalid SSN")