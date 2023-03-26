# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Financial application: compute CD value) Suppose you put $10,000 into a CD
with an annual percentage yield of 5.75%. After one month, the CD is worth
        10000 + 10000 * 5.75 / 1200 = 10047.92
After two months, the CD is worth
        10047.91 + 10047.91 * 5.75 / 1200 = 10096.06
After three months, the CD is worth
        10096.06 + 10096.06 * 5.75 / 1200 = 10144.44
and so on.
Write a program that prompts the user to enter an amount (e.g., 10000), the
annual percentage yield (e.g., 5.75), and the number of months (e.g., 18) and
displays a table as shown in the sample run.'''


# Prompt the user to enter an amount
savingAmount = float(input("Please enter the initial deposit amount: "))

# Prompt the user to enter the annual percentage yield
percentageYield = float(input("Please enter the annual percentage yield: "))

# Prompt the user to enter the number of months
numberOfMonths = int(input("Please enter maturity period  (number of months): "))

# Display result
print(f"%-1s%20s" % ("Month","CD Value"))
for i in range(1, numberOfMonths+1, +1 ):
    savingAmount += savingAmount * (percentageYield / 1200)
    print(f"%-1d%24.2f" % (i,savingAmount))