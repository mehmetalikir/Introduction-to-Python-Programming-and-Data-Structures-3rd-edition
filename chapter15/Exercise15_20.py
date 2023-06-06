# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Decimal to hex) Write a recursive function that converts a decimal number into
a hex number as a string. The function header is as follows:

    def decimalToHex(value):

Write a test program that prompts the user to enter a decimal number and displays
its hex equivalent.'''


def main():
    # Prompt the user to enter a decimal number
    decimal = int(input("Please enter a decimal integer: "))

    # Display the value's hex equivalent
    print(str(decimal) + " is hexadecimal " + decimalToHex(decimal))


# Convert a decimal number into hex
def decimalToHex(value):
    if value == 0:  # Base case: decimal value is 0
        return "0"
    elif value < 0:
        return "-" + decimalToHex(-value)
    else:
        hexChars = "0123456789ABCDEF"  # String of hexadecimal characters
        remainder = value % 16  # Remainder when dividing value by 16
        quotient = value // 16  # Quotient of value divided by 16

        if quotient == 0:  # Base case: quotient is 0
            return hexChars[remainder]  # Return the hexadecimal character based on the remainder
        else:  # Recursive case: quotient is not 0
            # Recursively call decimalToHex on the quotient and concatenate it with the hexadecimal character
            return decimalToHex(quotient) + hexChars[remainder]


main()
