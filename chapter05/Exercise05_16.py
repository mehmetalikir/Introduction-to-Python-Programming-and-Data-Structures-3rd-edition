# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Compute the greatest common divisor) Listing 5.8, another solution for to find
the greatest common divisor of two integers n1 and n2 is as follows: First find d
to be the minimum of n1 and n2, and then check whether d, d-1, d-2, . . . , 2, or 1
is a divisor for both n1 and n2 in this order. The first such common divisor is the
greatest common divisor for n1 and n2.'''

# Prompts the user to enter two positive integers
n1 = int(input("n1 :"))
n2 = int(input("n2 :"))

# Compute GCD
gcd = 0
if n1 < n2:
    gcd = n1
else:
    gcd = n2

while n1 % gcd != 0 or n2 % gcd != 0:
    gcd -= 1

# Displays the GCD
print("The greatest common divisor for ", n1, "and ", n2, " is ", gcd)
