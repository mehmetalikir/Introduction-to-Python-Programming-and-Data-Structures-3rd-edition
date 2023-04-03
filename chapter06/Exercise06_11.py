# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Financial application: compute commissions) Write a method that computes
the commission, using the scheme in Programming Exercise 5.39. The header of the
method is as follows:

def computeCommission(salesAmount):

Write a test program that displays the following table:

Sales Amount    Commission
10000           900.0
15000           1500.0
...
95000           11100.0
100000          11700.0'''


def computeCommission(salesAmount):

    # Print header of table
    print("Sales Amount         Commission")

    # Compute commission
    while salesAmount <= 100_000:
        if salesAmount < 10_000:
            commission = salesAmount * 8
        elif salesAmount <= 10_000:
            commission = 400 + (salesAmount - 5_000) * 0.1
        else:
            commission = 900 + (salesAmount - 10_000) * 0.12

        # Display result
        print("%-7d%21.1f" % (salesAmount,commission))
        salesAmount += 5000

def main():
    computeCommission(10000)

main()

