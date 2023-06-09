# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Check for prime numbers) In programing Exercise 15.7 you were asked to
implement a recursive function to determine whether a given number is a prime
number. Now rewrite this implementation to use an algorithm based on iteration
instead. The program should prompt the user for a number and print whether it is
prime or not.'''

def main():
    n = int(input("Please enter a whole number:"))

    if is_prime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")


# Check whether a given whole number is a prime number
def is_prime(n):
    if n <= 1:
        return False

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False

    return True


main()
