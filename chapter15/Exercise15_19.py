# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Decimal to binary) Write a recursive function that converts a decimal number
into a binary number as a string. The function header is as follows:

    def decimalToBinary(value):

Write a test program that prompts the user to enter a decimal number and displays
its binary equivalent.'''


def main():
    # Prompt the user to enter a decimal number
    decimal = int(input("Please enter a decimal number: "))

    binary = decimalToBinary(decimal) # Call the function

    # Display the value's binary equivalent
    print(f"The binary equivalent of {decimal} is {binary}")

# Convert a decimal number into a binary number as a string
def decimalToBinary(value):
    if value == 0:  # Base case: decimal value is 0
        return "0"
    elif value == 1:  # Base case: decimal value is 1
        return "1"
    else:
        # Recursive case: divide the decimal value by 2 and convert the quotient to binary
        return decimalToBinary(value // 2) + str(value % 2)


main()
