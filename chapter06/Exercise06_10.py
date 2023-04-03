# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Use the isPrime Function) Listing 6.7, PrimeNumberFunction.py, provides
the isPrime(number) function for testing whether a number is prime. Use this
function to find the number of prime numbers less than 10,000.'''


# Check whether number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not a prime
            return False
        divisor += 1

    return True  # number is prime


def printPrimeNumbers():
    number = 2  # A number to be tested for primeness
    count = 0 # Count the number of prime numbers

    # Repeatedly find prime numbers
    while number < 10_000:

        # Print the prime number and increase the count
        if isPrime(number):
            print(number, end = " ")
            count += 1
            if count % 10 == 0:
                print() # Break line
        number += 1

def main():

    # Display result
    print("The prime numbers less than 10,000.")
    print("-----------------------------------")
    printPrimeNumbers()


main()  # Call the main function
