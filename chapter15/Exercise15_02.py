# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Fibonacci numbers) Rewrite the fib function in Listing 15.2 using iterations.
(Hint: To compute fib(n) without recursion, you need to obtain fib(n - 2)
and fib(n - 1) first.) Let f0 and f1 denote the two previous Fibonacci numbers.
The current Fibonacci number would then be f0 + f1. The algorithm can be
described as follows:
    f0 = 0 # For fibs(0)
    f1 = 1 # For fib(1)
    for i in range(2, n + 1):
        currentFib = f0 + f1
        f0 = f1
        f1 = currentFib
    # After the loop, currentFib is fib(n)
Write a test program that prompts the user to enter an index and displays its
Fibonacci number.'''


def main():
    index = int(input("Please enter an index for Fibonacci number: "))
    print(f"The Fibonacci number at index {index} is ", str(fib(index)))


def fib(n):
    f0 = 0  # For fibs(0)
    f1 = 1  # For fib(1)

    if n == 0:
        return 0
    if n == 1:
        return 1

    for i in range(2, n + 1):
        currentFib = f0 + f1
        f0 = f1
        f1 = currentFib

    return f1


main()
