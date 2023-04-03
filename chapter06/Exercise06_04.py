# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display count of even and odd in an integer) Write a function with the following
header to display the count of even and odd in an integer:

def findEvenAndOdd(number):

Write a test program that prompts the user to enter integer and displays
the count of even and odd. For example, 456 contains 2 even (4 and 6) and 1 odd (5)
'''
def findEvenAndOdd(number):

    # Assign values
    evens = 0
    odds = 0

    # Check whether number is even or odd
    for i in range(0,len(str(number)), +1):
        n = number % 10

        if n % 2 == 0:
            evens += 1
        else:
            odds += 1

        number //= 10

    # Display result
    print("Number of even integers: ", evens)
    print("Number of odd integers: ", odds)

def main():
    # Prompt the user to enter an integer
    number = int(input("Please enter and integer: "))

    findEvenAndOdd(number) # Invoke function

main()







