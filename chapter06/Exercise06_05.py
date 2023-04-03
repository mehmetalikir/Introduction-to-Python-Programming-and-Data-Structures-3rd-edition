# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Sort three numbers) Write a method with the following header to display three
numbers in increasing order:

    def displaySortedNumbers(num1, num2, num3)

Write a test program that prompts the user to enter three numbers and invokes the
method to display them in increasing order.'''
def displaySortedNumbers(num1, num2, num3):

    # Sort them in increasing order
    if num2 < num1:
        num2, num1 = num1, num2 # Simultaneous assignment
    if num3 < num2:
        num3, num2 = num2, num3
    if num2 < num1:
        num2, num1 = num1, num2

    # Display result
    print("The sorted numbers in decreasing order are", num1, num2, num3)

def main():
    # Prompt the user for input
    num1 = float(input("Please enter number1: "))
    num2 = float(input("Please enter number2: "))
    num3 = float(input("Please enter number3: "))

    displaySortedNumbers(num1, num2, num3) # Invoke function

main()
