# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Product of the digits in an integer) Write a function that computes the product
of the digits in an integer. Use the following function header:

def productDigits(n):

For example, productDigits(234) returns 24 (2 * 3 * 4). (Hint: Use the % operator
to extract digits, and the // operator to remove the extracted digit. For instance,
to extract 4 from 234, use 234 % 10 (= 4). To remove 4 from 234, use 234 / 10
(= 23). Use a loop to repeatedly extract and remove the digit until all the digits
are extracted. Write a test program that prompts the user to enter an integer and
displays the sum of all its digits.'''

def productDigits(n):
    # Assign values
    product = 1

    # Repeatedly extract and remove the digits
    while n != 0:
        product *= n % 10
        n //= 10

    # Return value
    return product
def main():
    # Prompt the user enter an integer
    n = int(input("Please enter an integer: "))

    # Invoke function and display return
    print(f"The product of digits for {n} is", productDigits(n))

main()
