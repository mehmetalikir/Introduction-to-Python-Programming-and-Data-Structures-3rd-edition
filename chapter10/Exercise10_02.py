# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Create a calculator) Write a program that calculates the payback
amount of a loan at the given rate for a specified number of years. The
formula for the calculation is as follows:

    futureValue = investmentAmount * (1 + monthlyInterestRate) ** years * 12

Use text fields for users to enter the interest rate, years, and loan amount.
Display the payback amount in a text field when the user clicks the Calculate Loan button,
as shown in Figure 10.16b.'''

from tkinter import *  # Import tkinter


class Loan:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Loan Calculator")  # Set title

        # Create labels on the left side of GUI
        Label(window, text="Loan Amount").grid(row=1, column=1, sticky=W)
        Label(window, text="Loan Term(years)").grid(row=2, column=1, sticky=W)
        Label(window, text="Annual Interest Rate").grid(row=3, column=1, sticky=W)
        Label(window, text="Payback Amount").grid(row=4, column=1, sticky=W)

        # Create entries on the right side of GUI
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=1, column=2)
        self.loanTermVar = StringVar()
        Entry(window, textvariable=self.loanTermVar, justify=RIGHT).grid(row=2, column=2)
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=3, column=2)
        self.paybackAmountVar = StringVar()
        Entry(window, textvariable=self.paybackAmountVar, justify=RIGHT).grid(row=4, column=2)

        # Create calculate loan button on the bottom of GUI
        btCalculateLoan = Button(window, text="Calculate Loan", command=self.calculateLoan).grid(
            row=5, column=2, sticky=E)

        window.mainloop()  # Create an event loop

    def calculateLoan(self):
        monthlyIntersetRate = float(self.annualInterestRateVar.get()) / 1200

        futureValue = float(self.loanAmountVar.get()) * \
                      (1 + monthlyIntersetRate) ** (float(self.loanTermVar.get()) * 12)

        self.paybackAmountVar.set("{0:10.2f}".format(futureValue))


Loan()  # Create GUI
