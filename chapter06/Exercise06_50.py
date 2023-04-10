# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Decimal to hex) Write a function that parses a decimal numer into a hex number
as a string. The function headers are:

def dec2Hex(value):

See Appendix C, "Numbers Systems," for converting a decimal into a hex. Write
a test program that prompts the use to enter a decimal number and displays its
equivalent hex value.'''


def main():
    # Prompt the user to enter a decimal integer
    decimal = int(input("Please enter a decimal integer: "))

    hex = dec2Hex(decimal) # Invoke function

    # Display result
    if decimal == None:
        print("Incorrect decimal number")
    else:
        print("The hex value for decimal number",
              decimal, "is", hex)


# Convert decimal to hex
def dec2Hex(value):
    # Assign value
    hex = ""

    while value != 0:
        hexValue = value % 16

        #  Convert a decimal value to a hex digit
        hexChar = chr(hexValue + ord('0')) if 0 <= hexValue <= 9 \
            else chr(hexValue - 10 + ord('A'))

        hex = hexChar + hex
        value = value // 16

    return hex

main()  # Call the main function
