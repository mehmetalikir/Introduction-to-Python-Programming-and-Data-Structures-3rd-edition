# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Determining if a number is prime) Write a recursive function that checks
whether a given whole number is a prime number. The main program should
prompt the user for a whole number and print whether it is a prime number'''


def main():
    n = int(input("Please enter a whole number:"))

    if isPrime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")


# Check whether a given whole number is a prime number
def isPrime(n, divisor=2):  # Assign values

    if n <= 1:
        return False  # Base case
    if divisor * divisor > n:
        return True  # Base case
    if n % divisor == 0:
        return False
    return isPrime(n, divisor + 1)  # Recursive call


main()
