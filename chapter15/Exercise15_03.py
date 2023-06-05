# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Countdown using recursion) Write a recursive function that counts down from
a given number to 0. The program should prompt the user for a number and
print a countdown in *'s from that number to 0 and then print "Blast off!". For
example, with an input of 4, the program should print:
****
***
**
*
Blast off!'''


# Count down from a given number to 0
def countdown(n):
    if n <= 0:
        print("Blast off!")  # Base case
    else:
        print("*" * n)
        countdown(n - 1)


# Prompt the user for a number
num = int(input("Please enter a number: "))

# print a countdown in *'s from that number to 0 then print "Blast off!"
countdown(num)
