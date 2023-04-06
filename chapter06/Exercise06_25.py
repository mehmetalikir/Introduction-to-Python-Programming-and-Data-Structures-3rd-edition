# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Emirp) An emirp (prime spelled backward) is a non-palindromic prime number
whose reversal is also a prime. For example, 17 is a prime and 71 is a prime, so 17
and 71 are emirps. Write a program that displays the first 100 emirps. Display 10
numbers per line, separated by exactly one space, as follows:
13 17 31 37 71 73 79 97 107 113
149 157 167 179 199 311 337 347 359 389'''


# Return the reversal of an integer
def reverse(number):
    number = str(number)
    reversed = ""

    for i in range(0, len(number), +1):
        reversed = number[i] + reversed

    return reversed


# Return true if number is a palindrome
def isPalindrome(number):

    if number == int(reverse(number)):  # Check whether number is palindrome
        return True
    else:
        return False

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not a prime
            return False
        divisor += 1

    return True  # Number is prime
def printEmirpNumbers():
    number = 2  # A number to be tested for emirp
    count = 0 # Count the number of emirp numbers

    # Repeatedly find emirp numbers
    while count <= 100:
        if isPrime(number) and not (isPalindrome(number)) and isPrime(int(reverse(number))): # Check whether number is emirp
            print(f"%-10s" % number, end = "")
            count += 1
            if count % 10 == 0:
                print() # Jump to the new line
        number += 1
def main():

    printEmirpNumbers()

main()



