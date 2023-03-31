# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Palindrome integer) Write the methods with the following headers

Use the reverse method to implement isPalindrome. A number is a palindrome
if its reversal is the same as itself. Write a test program that prompts the
user to enter an integer and reports whether the integer is a palindrome.'''


# Return the reversal of an integer, i.e. reverse(456) returns 654
def reverse(number):
    number = str(number)
    reversed = ""

    for i in range(0, len(number), +1):
        reversed = number[i] + reversed

    return reversed


# Return true if number is a palindrome
def isPalindrome(number):

    # Check whether number is palindrome
    if number == int(reverse(number)):
        return True
    else:
        return False

def main():

    # Prompt the user enter an integer:
    number = int(input("Please enter a positive integer: "))

    # Display result
    if isPalindrome(number):  # Invoke function
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")


main()
